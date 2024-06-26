---
title: Machine Learning Constitutive Response of Multiscale Fibrous Materials
image:
  placement: 1
  filename: HPC_Biomechanics.png
  focal_point: 'Center'
  preview_only: false
weight: 3
---
  Hi-fidelity multiscale simulations using frameworks such as [MuMFiM]({{< relref "/projects/mumfim/index.md" >}})
  are necessary to develop an understanding of fibrous materials on an
  engineering or biological scale. However, they require significant computational
  resources and HPC expertise that are out of reach for most biomechanicians.
  This project seeks to develop constitutive models for fibrous materials making
  use of machine learning methodologies.

  This has led to the development of a framework for using neural-network hyperelastic materials in [MuMFiM]({{< relref "/projects/mumfim/index.md" >}})
  and a set of physics constrained neural-networks that can estimate the constitutive response of fibrous materials.

  In an example test case, a model of a FCL that took 432 GPU-hours on 72-NVIDIA V100
  GPUs could be solved in less than 30 minutes on a m1-macbook pro laptop. By 
  continuing to incorporate the complex fiber network physics into these machine
  learned models, more of the biomechanics community can access the benefits of
  high-fidelity multiscale simulations.
