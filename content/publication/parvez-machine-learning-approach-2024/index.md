---
title: 'A Physics Preserving Neural Network Based Approach for Constitutive Modeling of Isotropic Fibrous Materials'
date: '2024-12-18'
draft: false
publishDate: '2026-02-28'
authors:
- Nishan Parvez
- Jacob Merson
publication_types:
- 'article-journal'
abstract: >
  We develop a new neural network based material model for discrete fibrous materials that
  strictly enforces constitutive constraints such as polyconvexity, frame-indifference, and
  the symmetry of the stress and material stiffness. Additionally, we show that the accuracy
  of the stress and material stiffness predictions is significantly improved for this neural
  network by using a Sobolev minimization strategy that includes derivative terms. We obtain
  a normalized mean square error of 0.15% for the strain energy density, 0.815% averaged
  across the components of the stress, and 5.4% averaged across the components of the
  stiffness tensor. This machine-learned constitutive model was deployed in a finite element
  simulation of a facet capsular ligament. The displacement fields and stress–strain curves
  were compared to a multiscale simulation that required running on a GPU-based
  supercomputer. The new approach maintained upward of 85% accuracy in stress up to 70%
  strain while reducing the computation cost by orders of magnitude.
featured: false
publication: 'Engineering with Computers'
doi: 10.1007/s00366-024-02095-8
---
