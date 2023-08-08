---
title: 'MuMFiM: Multiscale Modeling of Fibrous Materials'
date: '2023-01-01'
draft: false
publishDate: '2023-08-04T21:18:57.895511Z'
authors:
- Jacob Merson
- Catalin Picu
- Mark S. Shephard
publication_types:
- '3'
abstract: >
  This article presents MuMFiM, an open source application for multiscale 
  modeling of fibrous materials on massively parallel computers. MuMFiM uses 
  two scales to represent fibrous materials such as biological network materials 
  (extracellular matrix, connective tissue, etc.). It is designed to make use 
  of multiple levels of parallelism, including distributed parallelism of the 
  macro and microscales as well as GPU accelerated data-parallelism of the microscale. 
  Scaling results of the GPU accelerated microscale show that solving microscale problems 
  concurrently on the GPU can lead to a 1000x speedup over the solution of a single 
  RVE on the GPU. In addition, we show nearly optimal strong and weak scaling results 
  of MuMFiM on up to 128 nodes of AiMOS (Rensselaer Polytechnic Institute) which is composed 
  of IBM AC922 nodes with 6 Volta V100 GPU and 2 20 core Power 9 CPUs each. We also show how 
  MuMFiM can be used to solve problems of interest to the broader engineering community, 
  in particular providing an example of the facet capsule ligament (FCL) of the human 
  spine undergoing uniaxial extension.
featured: false
publication: 'arXiv'
tags:
- dissertation-nocite
links:
- name: arXiv
  url: https://arxiv.org/abs/2306.09427
---
