Solving the One-Dimensional Infinite Potential Well Using Analytical and Numerical Methods

This project solves the time-independent Schrödinger equation for a one-dimensional infinite potential well using two methods:

Analytical (Exact) Solution

Numerical Solution using Taylor expansion and discretization of the second derivative.

The goal is to compare the exact wave function with the numerical approximation and to examine the structure of quantized energies.

1. Physics of the Problem: Infinite Potential Well

The potential:

V(x) = { 0       , 0 < x < L
         ∞       , otherwise }


The particle cannot escape the well, so the boundary conditions are:

ψ(0) = 0, ψ(L) = 0

2. Time-Independent Schrödinger Equation
-(ℏ^2 / 2m) * d²ψ/dx² + V(x) ψ = E ψ


Inside the well (V = 0):

d²ψ/dx² = -k² ψ


where

k = √(2 m E) / ℏ

3. Analytical Solution

General solution:

ψ(x) = C1 sin(kx) + C2 cos(kx)


Boundary condition ψ(0) = 0 ⇒ C2 = 0:

ψ(x) = C1 sin(kx)


Boundary condition ψ(L) = 0 ⇒ sin(kL) = 0:

k L = n π, n = 1,2,3,...


So:

k = n π / L


Allowed energies:

E_n = (n² π² ℏ²) / (2 m L²)


Normalized wave function:

ψ_n(x) = √(2/L) * sin(n π x / L)

4. Numerical Second Derivative Using Taylor Expansion

Divide the interval into points:

x0, x1, x2, ..., x_{N-1}


with spacing:

dx = x_{i+1} - x_i


Taylor expansion for ψ(x):

ψ(x+dx) = ψ(x) + ψ'(x) dx + 1/2 ψ''(x) dx² + ...
ψ(x-dx) = ψ(x) - ψ'(x) dx + 1/2 ψ''(x) dx² + ...


Adding these:

ψ(x+dx) + ψ(x-dx) = 2 ψ(x) + ψ''(x) dx² + O(dx⁴)


Numerical second derivative:

ψ''(x) ≈ (ψ(x+dx) - 2 ψ(x) + ψ(x-dx)) / dx²


This forms the basis for numerical Schrödinger solvers.

5. Discretization of the Schrödinger Equation

Inside the well:

ψ''(x) = -k² ψ(x)


Using the numerical second derivative:

(ψ_{i+1} - 2ψ_i + ψ_{i-1}) / dx² = -k² ψ_i


Multiply both sides by dx²:

ψ_{i+1} = (2 - k² dx²) ψ_i - ψ_{i-1}


Since k² = 2 m E / ℏ², define:

c = k² dx² = 2 m E dx² / ℏ²


The recurrence formula:

ψ_{i+1} = (2 - c) ψ_i - ψ_{i-1}


This is the formula used in the numerical code.

6. Initial Values for Numerical Solution

Since ψ(0) = 0:

ψ_0 = 0


To avoid the entire sequence being zero, use a small initial value:

ψ_1 = ε


These two values are all the algorithm needs; the rest of the points are generated using the recurrence relation.

7. Normalization of the Wave Function

Normalization condition:

∫₀ᴸ |ψ(x)|² dx = 1


In the numerical approximation:

Σ_i ψ_i² dx = 1


So normalize:

ψ_i ← ψ_i / √(Σ_j ψ_j² dx)

8. Program Features and Inputs

Inputs

Well length: L (from the user)

Quantum number: n (which energy state to calculate)

Features

Compute analytical energy: E_n = n² π² ℏ² / (2 m L²)

Compute exact wave function ψ_n(x)

Solve Schrödinger equation numerically using second derivative discretization

Automatic normalization of the numerical wave function

Plot:

Exact and numerical wave functions

Probability density |ψ|²

Direct comparison between analytical and numerical solutions

9. Project Outputs

At the end, the program produces:

Analytical wave function

Numerical (approximate) wave function

Comparison plot

Probability density

Quantized energy of the chosen state
