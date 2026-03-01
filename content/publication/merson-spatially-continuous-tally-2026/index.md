---
title: 'Spatially Continuous Functional Expansion Tallies on Unstructured Meshes'
date: '2026-04-01'
draft: false
publishDate: '2026-02-28'
authors:
- Jacob Merson
- Hunter Belanger
- Parth Singh
publication_types:
- 'paper-conference'
abstract: >
  Functional expansion tallies (FETs) have become a popular method to generate tallies from
  Monte Carlo simulations which are spatially continuous, and can therefore facilitate
  multi-physics coupling with finite-element method (FEM) based solvers in other physics
  domains. There are, however, several drawbacks with traditional FETs, such as requiring a
  set of orthogonal basis functions defined on the geometric region of the tally. Another
  constraint is that at the intersection between two FET regions, the functional values will
  not, in general, be continuous. In this work, we propose a new type of FET which we call
  the Lagrange FET, that can be scored on a general unstructured mesh. In the Lagrange FET,
  continuity is guaranteed between elements of the mesh, and orthogonal basis functions are
  not required, permitting the use of standard FEM interpolation techniques. A simplified
  version of the Lagrange FET method which supports regular Cartesian meshes has been
  implemented in the Abeille Monte Carlo code, and has been demonstrated on a 1D slab
  reactor problem in addition to the C5G7 benchmark.
featured: false
publication: 'PHYSOR 2026 - The International Conference on Physics of Reactors'
note: 'Under Review'
---
