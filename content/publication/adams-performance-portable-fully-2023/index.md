---
title: A Performance Portable, Fully Implicit Landau Collision Operator with Batched
  Linear Solvers
date: '2023-05-01'
draft: false
publishDate: '2023-08-04T21:18:57.767838Z'
authors:
- Mark F. Adams
- Peng Wang
- Jacob Merson
- Matthew G. Knepley
publication_types:
- 'article'
abstract: >
  Modern accelerators use hierarchical parallel programming models
  that enable massive multithreading within a processing element (PE),
  with multiple PEs per device driven by traditional
  processes. Batching is a technique for exposing PE-level parallelism in
  algorithms that previously ran on entire processes or multiple threads
  within a single MPI process. Kinetic discretizations of magnetized plasmas,
  for example, advance the Vlasov-Maxwell system, which is then followed by a
  fully implicit time advance of a collision operator. These collision advances
  are independent at each spatial point and are well suited to batch processing.
 

  This paper builds on previous work on a high-performance, fully nonlinear
  Landau collision operator by batching the linear solver, as well as batching
  the spatial point problems and adding new support for multiple grids for
  highly multiscale, multi-species problems. An anisotropic relaxation
  verification test that agrees well with previous published results and
  analytical solutions is presented. The performance resutls from an NVIDIA A100
  node and early results from an AMD MI250X node is presented with a detailed
  hardware utilization analysis on the A100. For portability, the entire Landau
  operator time advance is implemented in the Kokkos language and the entire solver
  is available in the PETSc numerical library. '
featured: false
publication: 'arXiv'
tags:
- Physics - Plasma Physics
doi: 10.48550/arXiv.2209.03228
links:
- name: arXiv
  url: https://arxiv.org/abs/2209.03228
---

