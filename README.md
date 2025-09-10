# hyperpopy: Poisson Hyperplane Model Package

[![PyPI version](https://badge.fury.io/py/hyperpopy.svg)](https://badge.fury.io/py/hyperpopy)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python package for the Poisson hyperplane model. analytic_utils contains helper functions for calculating the conditional probability functions in the Poisson model, including the main result of the PRL paper "Multipoint Correlations in Poisson Media." generation_utils.py contains helper functions for plotting and generating realizations of the Poisson model, and mc_utils.py contains helper functions for Monte Carlo simulations. The most important functions in this package are color_distribution from analytic_utils.py, which calculates the CPF, and hyperplane_colorer_2d from generation_utils, which generates and plots realizations of two-dimensional Poisson media.

The examples folder contains code to reproduce plots from the PRL paper, and serves as a tutorial for how to use the functions in this package.


## Installation

```bash
pip install --upgrade hyperpopy
```

## Quick Start

```python
import hyperpopy
import numpy as np

# Calculate the arrival rate of a Poisson hyperplane process
rate_2d = hyperpopy.rate(2, 1.0)  # 2D, radius 1.0
print(f"2D Poisson rate: {rate_2d}")

# Generate a 2D visualization of the Poisson hyperplane process
fig = hyperpopy.plot_hyperplanes_color_2d(
    radius=10,
    grid_resolution=100,
    colorcutoffs=np.array([0.5]),
    cmap_list=hyperpopy.frozen_lake_colors
)

# Calculate color distribution for given points
points = np.array([[0, 0], [1, 0], [0, 1]])
colors = (0, 1, 0)  # Known colors for first two points
color_dist = (0.5, 0.5)  # Equal probability for each color

prob_dist = hyperpopy.color_distribution(points, colors, color_dist)
print(f"Color probabilities: {prob_dist}")
```

## Key Functions

### Analytical Utilities
- `rate(dimension, radius)`: Calculate Poisson hyperplane arrival rate
- `color_distribution(points, colors, color_dist)`: Compute conditional color probabilities
- `hitrate_1d/2d/3d(points)`: Calculate hit rates for convex hulls
- `slash_rates(points)`: Return rates of hyperplane partitions

### Generation & Visualization
- `sample_from_ball(dimension, num_points)`: Sample points from unit ball
- `plot_hyperplanes_color_2d()`: Generate 2D Poisson hyperplane visualizations
- `hyperplane_partition(points, gridpoints)`: Partition space using hyperplanes

### Monte Carlo Simulation
- `monte_carlo_hyperplane_partitions()`: Estimate connectivity distributions
- `plot_mc_colors_with_errorbars()`: Plot convergence with error bars
- `probability_landscape()`: Visualize probability landscapes in 2D/3D

## Examples

See the `examples/` directory for comprehensive examples including:
- Figure generation from research papers
- Monte Carlo convergence analysis
- Probability landscape visualization
- Chord length statistics

## Citation

If you use this package in your research, please cite the main paper at https://doi.org/10.1103/325k-g4dr, the paper's
data repository at 10.5281/zenodo.16990033, and this package at 10.5281/zenodo.17095969.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Links

- [GitHub Repository](https://github.com/AlecShelley/hyperpopy)
- [PyPI Package](https://pypi.org/project/hyperpopy/)
