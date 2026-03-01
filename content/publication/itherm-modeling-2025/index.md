---
title: 'A Multiscale Workflow for Thermal Analysis of 3DI Chip Stacks'
date: '2025-05-01'
draft: false
publishDate: '2026-02-28'
authors:
- Max Bloomfield
- Theodorian Borca-Tasciuc
- Amogh Wasti
- Zongmin Yang
- Matthew Galarza
- Timothy Chainer
- Prabudhya Chowdhury
- Aakrati Jain
- Jacob Merson
publication_types:
- 'paper-conference'
abstract: >
  Thermally aware design of 2.5 D and 3 D advanced packaging systems will require fast,
  accurate, and powerful thermal analysis of chiplets, stacks, and packages. These systems
  contain multiple materials with non-linear heat transfer properties and geometric feature
  sizes that span many orders of magnitude. The smallest heterostructures in the front and
  back ends of the line present significant thermal modeling and analysis challenges in
  isolation. Replicated millions or billions of times in a chiplet stack, these structures
  present a near insurmountable hurdle to meeting the speed and accuracy needed of analysis
  in the design process. Additionally, establishing precise parameter values for the
  materials in these systems, when size and temperature dependencies create significant
  deviations from bulk properties, further complicates the problem. To address these issues,
  we have developed a multiscale methodology that advances the current state of the field by
  enabling die-scale simulations that capture phenomena arising from the structural details
  of the BEOL metallization stack. Taking advantage of the large length-scale separation
  between the BEOL features and the die-level structures, we employ a hierarchical,
  multiscale, finite-element approach. This hierarchical method uses a standard finite
  element method (FEM) formulation on a die or package scale, using computational
  homogenization to obtain effective thermal conductivities in the BEOL. Referring to
  industry-standard layout and design files, we construct and solve a locally appropriate
  subscale FEM problem in a representative volume element (RVE) at every quadrature point in
  the macroscale FEM problem. To accomplish this calculation, in our multiscale workflow,
  all geometric models of these RVEs are automatically constructed, meshed, and used to
  compute homogenized, anisotropic, thermal conductivities from the relevant GDSII or OASIS
  files based on the FEM integration point locations. Here, we make use of a direct, static-
  condensation based method to extract the full thermal conductivity tensor.
featured: false
publication: 'The Intersociety Conference on Thermal and Thermomechanical Phenomena in Electronic Systems'
doi: 10.1109/ITherm55376.2025.11235683
---
