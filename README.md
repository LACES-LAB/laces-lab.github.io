# LACES Website

## Importing publications
1. export bibtex file from zotero
2. ```console
    academic import --bibtex mypubs.bib --publication-dir content/publications
   ```
3. Edit publications, add PDFs

Publication types:

0 = Uncategorized;
1 = Conference paper;
2 = Journal article;
3 = Preprint / Working Paper;
4 = Report;
5 = Book;
6 = Book section;
7 = Thesis;
8 = Patent

## Checking spelling

Tips [here](https://www.manuel-strehl.de/check_markdown_spelling_with_aspell)

```bash
for file in *.md
do
    aspell check --mode=markdown --lang=en "$file"
done

```
