---
title: Parallel Coupler for Multimodel Simulations (PCMS)
graphicalabstract: coupler-overview.png
weight: 1
image:
  placement: 1
  filename: coupler-overview.png
  focal_point: 'Center'
  preview_only: false
  alt_text: A diagram showing the structure of PCMS. It uses an intermediate representation of fields to improve scalability of new couplings.
---
Fusion power promises to be one of the most transformative technologies of our time, 
however, many fundamental questions about plasma physics and reactor operation remain. 
Answering these questions requires exascale multiscale and multiphysics simulations and a
broad range of domain and computational expertise. Over the past 50 years, large teams have 
invested thousands of person-hours into the development of software that can efficiently 
simulate the physics in specific portions of the reactor volume that use fundamentally 
different discretizations, time-stepping methods, mathematical models, and so forth. 
Given the need for specialized numerics in each part of the reactor volume, and the 
expertise required to do so, it is not feasible to develop a new multiphysics code 
that encompasses the entire reactor volume using a homogenized framework. Currently, 
coupling methods exist for specific applications (i.e., core-edge), but do not scale to 
the needs of full-device, or full-plant modeling. This Project develops a new framework for 
tight-coupling of distinct codes at-scale on exascale supercomputers. It will describe the 
approach for data-transfer, parallel control, and interrogation-based field transfer operations.
