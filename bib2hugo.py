#!/usr/bin/env python3
"""
bib2hugo.py - Generate Hugo website publication entries from a BibLaTeX file.

Usage:
    python bib2hugo.py <bib_file> <output_dir> [options]

Options:
    --update         Overwrite existing index.md files (default: skip existing)
    --dry-run        Print what would be created without writing files
    --filter TYPE    Only process entries matching a type: journal, conference, all (default: all)
    --authors-dir    Path to Hugo authors directory (default: <repo>/content/authors)
    --aliases-file   Path to author aliases YAML file (default: <repo>/author_aliases.yaml)

--- EXTENDING THE BIB FILE ---

Add these custom fields to any bib entry to control website generation:

    abstract = {Full paper abstract for display on the website.}
    website-url = {https://example.com/preprint.pdf}
    website-url-name = {PDF}          % name for the link (default: URL)
    website-featured = {true}         % mark as a featured publication
    website-key = {my-custom-folder}  % override the auto-generated folder name
    website-skip = {true}             % exclude this entry from the website
    website-tags = {tag1, tag2}       % comma-separated tags

--- AUTHOR ALIASES ---

Create author_aliases.yaml in the repo root to map name variants to the
canonical name used in content/authors/*/  _index.md.  Example:

    "Jacob S. Merson": "Jacob Merson"
    "Merson, J.": "Jacob Merson"
    "Md Fuad Hasibul Hasan": "Fuad Hasan"

The script also performs automatic fuzzy matching (same last name + compatible
first name), so many aliases are resolved without an explicit entry.

--- WHICH ENTRIES ARE INCLUDED ---

By default the script creates website entries for:
  - @article                            (journal papers, published or submitted)
  - @inproceedings / @incollection      (conference proceedings)
  - @misc with keyword "peerreview"     (peer-reviewed conference papers)

Talks, posters, invited lectures, and patents are excluded unless
you add  website-skip = {false}  to force inclusion.
"""

import re
import sys
import argparse
import textwrap
from dataclasses import dataclass
from datetime import date
from pathlib import Path

import yaml
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode


# ---------------------------------------------------------------------------
# Author resolution
# ---------------------------------------------------------------------------

@dataclass
class AuthorProfile:
    slug: str        # directory name, e.g. "jacob-merson"
    title: str       # display name, e.g. "Jacob Merson"
    first_name: str  # e.g. "Jacob"
    last_name: str   # e.g. "Merson"


def load_author_profiles(authors_dir: Path) -> list:
    """Load Hugo author profiles from content/authors/*/  _index.md."""
    profiles = []
    for md_file in sorted(authors_dir.glob('*/_index.md')):
        slug = md_file.parent.name
        content = md_file.read_text(encoding='utf-8')
        m = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not m:
            continue
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError:
            continue
        title = (fm.get('title') or '').strip()
        first_name = (fm.get('first_name') or '').strip()
        last_name = (fm.get('last_name') or '').strip()
        if title:
            profiles.append(AuthorProfile(slug, title, first_name, last_name))
    return profiles


def load_aliases(aliases_file: Path) -> dict:
    """Load explicit author name aliases from a YAML file.

    Format (YAML mapping):
        "Jacob S. Merson": "Jacob Merson"
        "Md Fuad Hasibul Hasan": "Fuad Hasan"
    """
    if not aliases_file.exists():
        return {}
    with open(aliases_file, encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data if isinstance(data, dict) else {}


def first_names_compatible(a: str, b: str) -> bool:
    """Return True if two first-name strings plausibly belong to the same person.

    Handles:
      - Exact match: "Jacob" == "Jacob"
      - Middle initial: "Jacob S." ~ "Jacob"  (same first word)
      - Single initial: "J." ~ "Jacob"
    """
    wa = a.strip().split()
    wb = b.strip().split()
    if not wa or not wb:
        return False
    fa = wa[0].rstrip('.')
    fb = wb[0].rstrip('.')
    if fa.lower() == fb.lower():
        return True
    # One side is just an initial
    if len(fa) == 1 and fb.lower().startswith(fa.lower()):
        return True
    if len(fb) == 1 and fa.lower().startswith(fb.lower()):
        return True
    return False


def resolve_author(name: str, profiles: list, aliases: dict):
    """Resolve a parsed author name to its canonical Hugo profile title.

    Returns (canonical_name, profile_or_None, method)
    method is one of: 'exact', 'alias', 'fuzzy', 'unknown-same-last', 'unknown'
    """
    # 1. Explicit alias
    if name in aliases:
        canonical = aliases[name]
        for p in profiles:
            if p.title == canonical:
                return canonical, p, 'alias'
        return canonical, None, 'alias'

    # 2. Exact match against profile titles
    for p in profiles:
        if p.title == name:
            return name, p, 'exact'

    # 3. Fuzzy: same last name + compatible first name
    parts = name.rsplit(' ', 1)
    if len(parts) == 2:
        first_in, last_in = parts
    else:
        first_in, last_in = '', parts[0]

    same_last = [p for p in profiles if p.last_name.lower() == last_in.lower()]
    if same_last:
        compatible = [p for p in same_last
                      if first_names_compatible(first_in, p.first_name)]
        if len(compatible) == 1:
            return compatible[0].title, compatible[0], 'fuzzy'
        # Same last name exists but no compatible first → likely needs an alias
        return name, None, 'unknown-same-last'

    return name, None, 'unknown'


# ---------------------------------------------------------------------------
# BibLaTeX helpers
# ---------------------------------------------------------------------------

def camel_to_kebab(name: str) -> str:
    """Convert a camelCase/PascalCase cite key to a kebab-case folder name."""
    s = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1-\2', name)
    s = re.sub(r'([a-z0-9])([A-Z])', r'\1-\2', s)
    s = re.sub(r'([a-zA-Z])(\d)', r'\1-\2', s)
    return s.lower()


def parse_date(date_str: str) -> str:
    """Return an ISO date string (YYYY-MM-DD) from a BibLaTeX date value."""
    date_str = date_str.strip().split('/')[0].strip()
    parts = date_str.split('-')
    if len(parts) == 1:
        return f"{parts[0]}-01-01"
    elif len(parts) == 2:
        return f"{parts[0]}-{parts[1]}-01"
    return f"{parts[0]}-{parts[1]}-{parts[2]}"


def parse_authors(author_str: str) -> list:
    """Return a list of author names in First Last order."""
    result = []
    for a in re.split(r'\s+and\s+', author_str, flags=re.IGNORECASE):
        a = a.strip()
        if not a:
            continue
        if ',' in a:
            last, first = a.split(',', 1)
            result.append(f"{first.strip()} {last.strip()}")
        else:
            result.append(a)
    return result


def clean_latex(text: str) -> str:
    """Strip common LaTeX markup from text."""
    text = re.sub(r'\\(?:emph|textbf|textit|textrm|text)\{([^}]*)\}', r'\1', text)
    text = re.sub(r'\{([^}]*)\}', r'\1', text)
    text = re.sub(r'\\[a-zA-Z]+\s*', '', text)
    return re.sub(r'\s+', ' ', text).strip()


def get_keywords(entry: dict) -> list:
    return [k.strip().lower() for k in entry.get('keywords', '').split(',') if k.strip()]


def is_preprint(entry: dict) -> bool:
    if entry.get('ENTRYTYPE', '').lower() != 'article':
        return False
    kws = get_keywords(entry)
    return 'submitted' in kws or 'inprep' in kws


def pub_type_from_entry(entry: dict) -> str:
    etype = entry.get('ENTRYTYPE', '').lower()
    if etype == 'incollection':
        return 'chapter'
    if etype in ('inproceedings', 'proceedings'):
        return 'paper-conference'
    if etype == 'misc':
        return 'paper-conference'
    if is_preprint(entry):
        return 'preprint'
    return 'article-journal'


def venue_from_entry(entry: dict) -> str:
    etype = entry.get('ENTRYTYPE', '').lower()
    if is_preprint(entry):
        eprint = entry.get('eprint', '').strip()
        if eprint and entry.get('eprinttype', '').strip().lower() == 'arxiv':
            return 'arXiv'
        return ''
    if etype == 'article':
        venue = entry.get('journaltitle', entry.get('journal', ''))
    elif etype in ('inproceedings', 'proceedings'):
        venue = entry.get('booktitle', entry.get('eventtitle', entry.get('location', '')))
    elif etype == 'incollection':
        venue = entry.get('booktitle', '')
    elif etype == 'misc':
        venue = entry.get('eventtitle', entry.get('location', ''))
    else:
        venue = entry.get('journaltitle', entry.get('location', ''))
    return clean_latex(venue)


def should_include(entry: dict) -> bool:
    explicit = entry.get('website-skip', '').strip().lower()
    if explicit == 'true':
        return False
    if explicit == 'false':
        return True
    etype = entry.get('ENTRYTYPE', '').lower()
    kws = get_keywords(entry)
    if etype == 'article':
        return 'journal' in kws
    if etype in ('inproceedings', 'incollection', 'proceedings'):
        return True
    if etype == 'misc':
        return 'peerreview' in kws
    return False


def folder_name(entry: dict) -> str:
    override = entry.get('website-key', '').strip()
    return override if override else camel_to_kebab(entry.get('ID', 'unknown'))


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_entry(entry: dict, profiles: list, aliases: dict) -> list:
    """Return a list of (level, message) warning tuples for an entry."""
    warnings = []
    eid = entry.get('ID', '?')
    etype = entry.get('ENTRYTYPE', '').lower()

    # 1. Missing abstract
    abstract = entry.get('abstract', '').strip()
    if not abstract:
        warnings.append(('WARN', f"{eid}: missing abstract"))

    # 2. Author resolution
    raw_authors = parse_authors(entry.get('author', ''))
    for name in raw_authors:
        _, profile, method = resolve_author(name, profiles, aliases)
        if method == 'fuzzy':
            warnings.append(('INFO', f"{eid}: '{name}' auto-matched to '{profile.title}'"))
        elif method == 'unknown-same-last':
            # Same last name exists but no first-name match — likely needs an alias
            last = name.rsplit(' ', 1)[-1]
            same = [p.title for p in profiles if p.last_name.lower() == last.lower()]
            warnings.append((
                'WARN',
                f"{eid}: '{name}' not matched — possible alias needed for: {', '.join(same)}"
            ))
        # 'exact', 'alias', 'unknown' → no warning for unknown (external collaborators)

    return warnings


# ---------------------------------------------------------------------------
# Output generation
# ---------------------------------------------------------------------------

def yaml_str(value: str) -> str:
    return f"'{value.replace(chr(39), chr(39)+chr(39))}'"


def render_index_md(entry: dict, profiles: list, aliases: dict) -> str:
    """Render the full content of an index.md file for a publication entry."""
    title = clean_latex(entry.get('title', ''))
    pub_date = parse_date(entry.get('date', entry.get('year', '2000')))
    today = date.today().isoformat()

    # Resolve author names to canonical Hugo profile titles where possible
    raw_authors = parse_authors(entry.get('author', ''))
    authors = []
    for name in raw_authors:
        canonical, _, _ = resolve_author(name, profiles, aliases)
        authors.append(canonical)

    pub_type = pub_type_from_entry(entry)
    publication = venue_from_entry(entry)
    doi = entry.get('doi', '').strip()
    abstract = entry.get('abstract', '').strip()
    featured = entry.get('website-featured', '').strip().lower() == 'true'
    tags = [t.strip() for t in entry.get('website-tags', '').split(',') if t.strip()]
    note = clean_latex(entry.get('note', '').strip())

    links = []
    eprint = entry.get('eprint', '').strip()
    if eprint and entry.get('eprinttype', '').strip().lower() == 'arxiv':
        links.append(('arXiv', f'https://arxiv.org/abs/{eprint}'))
    web_url = entry.get('website-url', entry.get('url', '')).strip()
    if web_url:
        links.append((entry.get('website-url-name', 'URL').strip(), web_url))

    lines = ['---']
    lines.append(f'title: {yaml_str(title)}')
    lines.append(f"date: '{pub_date}'")
    lines.append('draft: false')
    lines.append(f"publishDate: '{today}'")
    lines.append('authors:')
    for a in authors:
        lines.append(f'- {a}')
    lines.append('publication_types:')
    lines.append(f'- {yaml_str(pub_type)}')
    if abstract:
        lines.append('abstract: >')
        for line in textwrap.fill(abstract, width=90).splitlines():
            lines.append(f'  {line}')
    else:
        lines.append('abstract: ')
    lines.append(f'featured: {"true" if featured else "false"}')
    lines.append(f'publication: {yaml_str(publication)}')
    if tags:
        lines.append('tags:')
        for t in tags:
            lines.append(f'- {t}')
    if doi:
        lines.append(f'doi: {doi}')
    if note:
        lines.append(f'note: {yaml_str(note)}')
    if links:
        lines.append('links:')
        for lname, lurl in links:
            lines.append(f'- name: {lname}')
            lines.append(f'  url: {lurl}')
    lines.append('---')
    lines.append('')
    return '\n'.join(lines)


def reconstruct_bib(entry: dict) -> str:
    """Reconstruct a clean BibTeX entry, stripping website-specific fields."""
    skip_fields = {
        'ENTRYTYPE', 'ID', 'author_an',
        'website-key', 'website-skip', 'website-featured',
        'website-tags', 'website-url', 'website-url-name',
        'abstract',
    }
    etype = entry.get('ENTRYTYPE', 'misc')
    eid = entry.get('ID', 'unknown')
    lines = [f'@{etype}{{{eid},']
    for key, value in entry.items():
        if key in skip_fields:
            continue
        out_key = 'author+an' if key == 'author_an' else key
        lines.append(f'  {out_key} = {{{value}}},')
    lines.append('}')
    lines.append('')
    return '\n'.join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def load_bib(bib_path: Path) -> list:
    parser = BibTexParser(common_strings=True)
    parser.customization = convert_to_unicode
    parser.ignore_nonstandard_types = False
    with open(bib_path, encoding='utf-8') as f:
        text = f.read()
    text = re.sub(r'\bauthor\+an\b', 'author_an', text)
    db = bibtexparser.loads(text, parser=parser)
    return db.entries


def process_bib(bib_path: Path, output_dir: Path, authors_dir: Path,
                aliases_file: Path, update: bool, dry_run: bool,
                filter_type: str, verbose: bool = True,
                list_skipped: bool = False) -> None:

    entries = load_bib(bib_path)
    profiles = load_author_profiles(authors_dir) if authors_dir.exists() else []
    aliases = load_aliases(aliases_file)

    if verbose and profiles:
        print(f"Loaded {len(profiles)} author profiles, {len(aliases)} explicit aliases.\n")

    created = []
    skipped_exists = []
    skipped_type = []
    all_warnings = []   # (level, entry_id, message)

    for entry in entries:
        if not should_include(entry):
            skipped_type.append(entry.get('ID', '?'))
            continue

        kws = get_keywords(entry)
        if filter_type == 'journal' and 'journal' not in kws:
            skipped_type.append(entry.get('ID', '?'))
            continue
        if filter_type == 'conference' and 'conference' not in kws:
            skipped_type.append(entry.get('ID', '?'))
            continue

        # Collect warnings for this entry regardless of whether we write it
        for level, msg in validate_entry(entry, profiles, aliases):
            all_warnings.append((level, msg))

        fname = folder_name(entry)
        dest = output_dir / fname
        index_path = dest / 'index.md'

        if index_path.exists() and not update:
            skipped_exists.append(fname)
            continue

        index_content = render_index_md(entry, profiles, aliases)
        cite_content = reconstruct_bib(entry)

        if dry_run:
            print(f"[DRY RUN] Would create: {dest}/")
            print(f"  title: {clean_latex(entry.get('title', ''))}")
            created.append(fname)
            continue

        dest.mkdir(parents=True, exist_ok=True)
        index_path.write_text(index_content, encoding='utf-8')
        (dest / 'cite.bib').write_text(cite_content, encoding='utf-8')
        created.append(fname)
        if verbose:
            print(f"  + {fname}")

    # Print warnings grouped by level
    if verbose and all_warnings:
        # Separate by level for readability
        for level in ('WARN', 'INFO'):
            msgs = [m for l, m in all_warnings if l == level]
            if not msgs:
                continue
            label = {'WARN': 'Warnings', 'INFO': 'Info'}[level]
            print(f"\n{label}:")
            for m in msgs:
                print(f"  [{level}] {m}")

    if verbose:
        print(f"\nSummary ({bib_path.name}):")
        print(f"  Created/updated : {len(created)}")
        print(f"  Skipped (exists): {len(skipped_exists)}")
        print(f"  Excluded (type) : {len(skipped_type)}")
        if list_skipped:
            if skipped_exists:
                print("\n  Skipped (already exist):")
                for f in skipped_exists:
                    print(f"    ~ {f}")
            if skipped_type:
                print("\n  Excluded (type/keyword filter):")
                for f in skipped_type:
                    print(f"    - {f}")
        if skipped_exists:
            print("\n  Use --update to overwrite existing entries.")


def main():
    # Paths derived from the known project layout:
    #   ~/Documents/merson-biosketch-new-template/sections/publications.bib  (source of truth)
    #   ~/code/laces/                                                         (Hugo site root)
    repo_dir = Path(__file__).parent
    default_bib    = Path('~/Documents/merson-biosketch-new-template/sections/publications.bib')
    default_out    = repo_dir / 'content/publication'
    default_authors = repo_dir / 'content/authors'
    default_aliases = repo_dir / 'author_aliases.yaml'

    parser = argparse.ArgumentParser(
        description='Generate Hugo publication entries from a BibLaTeX file.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument('bib_file', nargs='?',
                        default=str(default_bib),
                        help=f'Path to the .bib file (default: {default_bib})')
    parser.add_argument('output_dir', nargs='?',
                        default=str(default_out),
                        help=f'Output directory (default: {default_out})')
    parser.add_argument('--authors-dir',
                        default=str(default_authors),
                        help=f'Hugo authors directory (default: {default_authors})')
    parser.add_argument('--aliases-file',
                        default=str(default_aliases),
                        help=f'Author aliases YAML file (default: {default_aliases})')
    parser.add_argument('--update', action='store_true',
                        help='Overwrite existing index.md files')
    parser.add_argument('--dry-run', action='store_true',
                        help='Print what would be created without writing files')
    parser.add_argument('--filter', choices=['journal', 'conference', 'all'],
                        default='all', dest='filter_type')
    parser.add_argument('--quiet', action='store_true', help='Suppress output')
    parser.add_argument('--list-skipped', action='store_true',
                        help='List all skipped and excluded entry IDs in the summary')
    args = parser.parse_args()

    bib_path = Path(args.bib_file).expanduser()
    if not bib_path.exists():
        print(f"Error: bib file not found: {bib_path}", file=sys.stderr)
        sys.exit(1)

    output_dir = Path(args.output_dir).expanduser()
    if not args.dry_run:
        output_dir.mkdir(parents=True, exist_ok=True)

    process_bib(
        bib_path=bib_path,
        output_dir=output_dir,
        authors_dir=Path(args.authors_dir).expanduser(),
        aliases_file=Path(args.aliases_file).expanduser(),
        update=args.update,
        dry_run=args.dry_run,
        filter_type=args.filter_type,
        verbose=not args.quiet,
        list_skipped=args.list_skipped,
    )


if __name__ == '__main__':
    main()
