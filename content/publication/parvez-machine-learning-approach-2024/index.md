---
title: A Machine Learning Approach for Multiscale Modeling of Biological Tissues
date: '2024-05-16'
draft: false
publishDate: '2024-05-16'
authors:
- Nishan Parvez
- Jacob Merson
publication_types:
- 'article'
abstract: >
  We develop a new neural network architecture that strictly enforces constitutive constraints such as polyconvexity, frame-indifference, and the symmetry of the stress and material stiffness. Additionally, we show that the accuracy of the stress and material stiffness predictions is significantly improved for this neural network by using a Sobolev minimization strategy that includes derivative terms. Using our neural network, we model the constitutive behavior of fibrous-type discrete network material. With Sobolev minimization, we obtain a normalized mean square error of 0.15% for the strain energy density, 0.815% averaged across the components of the stress, and 5.4% averaged across the components of the stiffness tensor. This machine-learned constitutive model was deployed in a finite element simulation of a facet capsular ligament. The displacement fields and stress-strain curves were compared to a multiscale simulation that required running on a GPU-based supercomputer. The new approach maintained upward of 85% accuracy in stress up to 70% strain while reducing the computation cost by orders of magnitude.
featured: false
publication: 'arXiv'
tags:
doi: 10.48550/arXiv.2403.13357
links:
- name: arXiv
  url: https://arxiv.org/abs/2403.13357
---

