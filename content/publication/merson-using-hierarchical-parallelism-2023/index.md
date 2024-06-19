---
title: Using Hierarchical Parallelism to Accelerate the Solution of Many Small Partial
  Differential Equations
date: '2023-05-01'
draft: false
publishDate: '2023-08-04T21:18:58.040195Z'
authors:
- Jacob Merson
- Mark S. Shephard
publication_types:
- 'paper-conference'
abstract: >
  This paper presents efforts to improve the hierarchical 
  parallelism of a two scale simulation code. Two methods
  to improve the GPU parallel performance were developed and 
  compared. The first used the NVIDIA Multi-Process Serviceand
  the second moved the entire sub-problem loop into a 
  single kernel using Kokkos hierarchical parallelism and a 
  PackedView data structure. Both approaches improved parallel 
  performance with the second method providing the greatest improvements.
featured: false
publication: 'arXiv'
tags:
- Computer Science - Distributed
- Parallel
- and Cluster Computing
- Computer Science - Mathematical Software
doi: 10.48550/arXiv.2305.07030
links:
- name: arXiv
  url: https://arxiv.org/abs/2305.07030
---

