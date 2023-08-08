---
title: Multiscale Modeling of Fibrous Materials (MuMFiM)
github: SCOREC/mumfim
graphicalabstract: mumfim-overview.png
abstract: >
  Fibrous materials are common in engineering and biology with applications 
  ranging from geotextiles to the extracellular matrix, collagen and actin gels.
  Modeling these materials on the engineering or biological scale is difficult
  because they move nonaffinely, are nonlocal, and heterogeneous. On one end of 
  the spectrum, discrete network models can capture these micromechanics, but 
  due to computational cost are precluded from modeling structures at the scales
  of interest. On the other end, continuum models can rapidly simulate biological
  or engineering scale behavior, but cannot capture the micromechanical
  complexity which is important for understanding disease progression.
 

  MuMFiM is a multiscale framework for high performance simulations of fibrous 
  materials. It is able to fill the gap between computational cost and capturing
  fiber micromechanics. To do this, it uses a FE2 finite element method and 
  specialized data-parallel solvers that are optimized to run on GPUs
  combined with MPI distributed parallel solvers. Together, this enables
  computations on models that are directly constructed from various imaging
  modalities.

weight: 2
---