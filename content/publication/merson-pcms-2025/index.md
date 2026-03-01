---
title: 'PCMS: Parallel Coupler for Multimodel Simulations'
date: '2025-08-21'
draft: false
publishDate: '2026-02-28'
authors:
- Jacob Merson
- Cameron W. Smith
- Mark S. Shephard
- Fuad Hasan
- Abhiyan Paudel
- Angel Castillo-Crooke
- Joyal Mathew
- Mohammad Elahi
publication_types:
- 'preprint'
abstract: >
  This paper presents the Parallel Coupler for Multimodel Simulations (PCMS), a new GPU
  accelerated generalized coupling framework for coupling simulation codes on leadership
  class supercomputers. PCMS includes distributed control and field mapping methods for up
  to five dimensions. For field mapping PCMS can utilize discretization and field
  information to accommodate physics constraints. PCMS is demonstrated with a coupling of
  the gyrokinetic microturbulence code XGC with a Monte Carlo neutral transport code DEGAS2
  and with a 5D distribution function coupling of an energetic particle transport code
  (GNET) to a gyrokinetic microturbulence code (GTC). A scaling study is also presented to
  stress the rendezvous and PCMS APIs.  It demonstrates an efficiency of 85% on up to 2,080
  GPUs of Frontier; 16-2048 processes for the application being scaled and a fixed 16
  processes each for the coupler and the second application.
featured: false
publication: 'arXiv'
doi: 10.48550/arXiv.2510.18838
note: 'Under Review'
links:
- name: arXiv
  url: https://arxiv.org/abs/2510.18838
---
