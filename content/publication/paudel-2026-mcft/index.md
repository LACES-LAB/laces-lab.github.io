---
title: 'A Stochastic Conservative Field Transfer Method for Black-box Multiscale and Multiphysics Coupling'
date: '2026-02-01'
draft: false
publishDate: '2026-02-28'
authors:
- Abhiyan Paudel
- Cameron W. Smith
- Jacob Merson
publication_types:
- 'preprint'
abstract: >
  This paper introduces a new method for performing field transfer operations in black-box
  coupling, when source discretization information is not available. This approach uses a
  stochastic approximation of the Galerkin projection which leads to a method that
  asymptotically provides conservation. Error in the accuracy and conservation has been
  compared to the mesh intersection method and radial basis functions on a simple domain, as
  well as on meshes of the LTX fusion reactor. For all cases tested, our new method provides
  higher accuracy and less conservation error than radial basis functions and can be used
  for black-box coupling, unlike the mesh-intersection method. Additionally, we demonstrate
  the implementation and performance of our method on an NVIDIA A100 GPU, showing that the
  cost is competitive with the mesh intersection method.
featured: false
publication: ''
---
