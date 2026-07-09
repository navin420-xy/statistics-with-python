# statistics-with-python
# Probability Density Function (PDF) Calculator

This project calculates the Probability Density Function (PDF) of a normal distribution using the mathematical formula instead of scipy.stats.norm.pdf().

## Formula

f(x) = (1 / (σ√(2π))) × e^(-0.5 × ((x - μ) / σ)^2)

## Requirements

pip install numpy

## Example

Mean = 50
Standard Deviation = 10
X = 60

Output:
0.024197072451914336
