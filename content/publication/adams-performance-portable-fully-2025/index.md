---
title: 'A Performance Portable, Fully Implicit Landau Collision Operator with Batched Linear Solvers'
date: '2025-04-30'
draft: false
publishDate: '2026-02-28'
authors:
- Mark F. Adams
- Peng Wang
- Jacob Merson
- Kevin Huck
- Matthew G. Knepley
publication_types:
- 'article-journal'
abstract: >
  Modern accelerators use hierarchical parallel programming models that enable massive
  multithreading within a processing element (PE), with multiple PEs per device driven by
  traditional processes. Batching is a technique for exposing PE-level parallelism in
  algorithms that have traditionally run on MPI processes or multiple threads within a
  single process. Opportunities for batching arise in, for example, kinetic discretizations
  of magnetized plasmas where collisions are advanced in velocity space at each spatial
  point independently. This paper builds on previous work on a high-performance, fully
  nonlinear, Landau collision operator by batching the linear solver, as well as batching
  the spatial point problems and adding new support for multiple grids for multiscale,
  multispecies problems. An anisotropic relaxation verification test that agrees well with
  previously published results and analytical models is presented. The performance results
  from NVIDIA A100 and AMD MI250X nodes are presented with hardware utilization analysis for
  each architecture. The entire implicit Landau operator time advance is implemented in
  Kokkos for performance portability, running entirely on the device and is available in the
  PETSc numerical library.
featured: false
publication: 'SIAM Journal on Scientific Computing'
doi: 10.1137/24M1640252
---
