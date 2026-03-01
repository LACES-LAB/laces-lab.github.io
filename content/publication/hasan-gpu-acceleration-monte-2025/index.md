---
title: 'GPU Acceleration of Monte Carlo Tallies on Unstructured Meshes in OpenMC with PUMI-Tally'
date: '2025-04-26'
draft: false
publishDate: '2026-02-28'
authors:
- Fuad Hasan
- Cameron W. Smith
- Mark S. Shephard
- R. Michael Churchill
- George J. Wilkie
- Paul K. Romano
- Patrick C. Shriwise
- Jacob Merson
publication_types:
- 'preprint'
abstract: >
  Unstructured mesh tallies are a bottleneck in Monte Carlo neutral particle transport
  simulations of fusion reactors. This paper introduces the PUMI-Tally library that takes
  advantage of mesh adjacency information to accelerate these tallies on CPUs and GPUs. For
  a fixed source simulation using track-length tallies, we achieved a speed-up of 19.7X on
  an NVIDIA A100, and 9.2X using OpenMP on 128 threads of two AMD EPYC 7763 CPUs on NERSC
  Perlmutter. On the Empire AI alpha system, we achieved a speed-up of 20X using an NVIDIA
  H100 and 96 threads of an Intel Xenon 8568Y+. Our method showed better scaling with number
  of particles and number of elements. Additionally, we observed a 199X reduction in the
  number of allocations during initialization and the first three iterations, with a similar
  overall memory consumption. And, our hybrid CPU/GPU method demonstrated a 6.69X
  improvement in the energy consumption over the current approach.
featured: false
publication: 'arXiv'
doi: 10.48550/arXiv.2504.19048
links:
- name: arXiv
  url: https://arxiv.org/abs/2504.19048
---
