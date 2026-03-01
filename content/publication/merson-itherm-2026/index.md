---
title: 'Accelerated Transient Multiscale Workflow for Thermal Analysis of 3DHI Chip Stack'
date: '2026-05-01'
draft: false
publishDate: '2026-02-28'
authors:
- Mohammad Elahi
- Max Bloomfield
- Theodorian Borca-Tasciuc
- Jacob Merson
publication_types:
- 'paper-conference'
abstract: >
  Modern package designs make use of technologies such as backside power delivery (BSPD) and
  3D stacked chiplets that require accounting for the heterogeneity in back end of the line
  (BEOL) structures in hot-spot prediction. Multiscale homogenization strategies have been
  demonstrated to be effective for steady-state simulations, however accurate 3D transient
  simulations that include BEOL structures remain an open challenge.  In this work, we
  demonstrate a transient thermal workflow that accounts for the 3D heterogeneous structures
  in the BEOL for problems with strong- and weak- temporal scale separation under the
  assumption of temperature independent constitutive properties. Our workflow, based on
  Bloomfield et. al. 2025, automatically extracts, meshes, and homogenizes thermal
  properties from GDSII and OASIS files to construct thermal property maps.  Property maps
  (heat capacity and conductivity) have been generated for a 1 mm$\times$1 mm SoC-style
  model die that was constructed with LibreLane for 100$\times$100 grids with 5 $μ m
  \times$5 $μ m$ representative volume elements (RVEs), and 50$\times$50 grids with 10 $μ
  m\times$ 10 $μ m$ RVEs. The expressions for a transient effective conductivity are
  provided and a demonstration of the impact of the transient effects are provided for a
  single RVE. Finally, transient conductivity maps have been provided for a time integration
  timestep of \(Δ t=0.001\).
featured: false
publication: 'The Intersociety Conference on Thermal and Thermomechanical Phenomena in Electronic Systems'
note: 'Under Review'
---
