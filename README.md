\documentclass[12pt]{article}
\usepackage{amsmath, amssymb}
\usepackage{geometry}
\geometry{margin=1in}

\begin{document}

\section*{Solving the One-Dimensional Infinite Potential Well Using Analytical and Numerical Methods}

This project solves the time-independent Schr\"odinger equation for a one-dimensional infinite potential well using two methods:

\begin{itemize}
    \item Analytical (Exact) Solution
    \item Numerical Solution using Taylor expansion and discretization of the second derivative
\end{itemize}

The goal is to compare the exact wave function with the numerical approximation and to examine the structure of quantized energies.

\section*{1. Physics of the Problem: Infinite Potential Well}

The potential:

\[
V(x) =
\begin{cases} 
0, & 0 < x < L \\
\infty, & \text{otherwise}
\end{cases}
\]

The particle cannot escape the well, so the boundary conditions are:

\[
\psi(0) = 0, \quad \psi(L) = 0
\]

\section*{2. Time-Independent Schr\"odinger Equation}

\[
-\frac{\hbar^2}{2 m} \frac{d^2 \psi}{dx^2} + V(x) \psi = E \psi
\]

Inside the well, \(V = 0\):

\[
\frac{d^2 \psi}{dx^2} = -k^2 \psi
\]

where

\[
k = \frac{\sqrt{2 m E}}{\hbar}
\]

\section*{3. Analytical Solution}

General solution:

\[
\psi(x) = C_1 \sin(kx) + C_2 \cos(kx)
\]

Boundary condition \(\psi(0) = 0\) implies \(C_2 = 0\):

\[
\psi(x) = C_1 \sin(kx)
\]

Boundary condition \(\psi(L) = 0\) implies \(\sin(kL) = 0\):

\[
k L = n \pi, \quad n = 1,2,3,\dots
\]

So:

\[
k = \frac{n \pi}{L}
\]

Allowed energies:

\[
E_n = \frac{n^2 \pi^2 \hbar^2}{2 m L^2}
\]

Normalized wave function:

\[
\psi_n(x) = \sqrt{\frac{2}{L}} \, \sin\left(\frac{n \pi x}{L}\right)
\]

\section*{4. Numerical Second Derivative Using Taylor Expansion}

Divide the interval into points:

\[
x_0, x_1, x_2, \dots, x_{N-1}
\]

with spacing:

\[
dx = x_{i+1} - x_i
\]

Taylor expansion for \(\psi(x)\):

\[
\psi(x+dx) = \psi(x) + \psi'(x) dx + \frac{1}{2} \psi''(x) dx^2 + \dots
\]

\[
\psi(x-dx) = \psi(x) - \psi'(x) dx + \frac{1}{2} \psi''(x) dx^2 + \dots
\]

Adding these:

\[
\psi(x+dx) + \psi(x-dx) = 2 \psi(x) + \psi''(x) dx^2 + O(dx^4)
\]

Numerical second derivative:

\[
\psi''(x) \approx \frac{\psi(x+dx) - 2 \psi(x) + \psi(x-dx)}{dx^2}
\]

This is the basis for numerical Schr\"odinger solvers.

\section*{5. Discretization of the Schr\"odinger Equation}

Inside the well:

\[
\psi''(x) = -k^2 \psi(x)
\]

Using the numerical second derivative:

\[
\frac{\psi_{i+1} - 2\psi_i + \psi_{i-1}}{dx^2} = -k^2 \psi_i
\]

Multiply both sides by \(dx^2\):

\[
\psi_{i+1} = (2 - k^2 dx^2) \psi_i - \psi_{i-1}
\]

Since \( k^2 = \frac{2 m E}{\hbar^2} \), define:

\[
c = k^2 dx^2 = \frac{2 m E dx^2}{\hbar^2}
\]

Recurrence formula:

\[
\psi_{i+1} = (2 - c) \psi_i - \psi_{i-1}
\]

This is the formula used in the numerical code.

\section*{6. Initial Values for Numerical Solution}

Since \(\psi(0) = 0\):

\[
\psi_0 = 0
\]

To avoid the sequence being entirely zero, use a small initial value:

\[
\psi_1 = \epsilon
\]

These two values are all the algorithm needs; the rest are generated using the recurrence relation.

\section*{7. Normalization of the Wave Function}

Normalization condition:

\[
\int_0^L |\psi(x)|^2 dx = 1
\]

Numerical approximation:

\[
\sum_i \psi_i^2 \, dx = 1
\]

Normalize:

\[
\psi_i \leftarrow \frac{\psi_i}{\sqrt{\sum_j \psi_j^2 dx}}
\]

\section*{8. Program Features and Inputs}

\textbf{Inputs}  
\begin{itemize}
    \item Well length \(L\) (from the user)  
    \item Quantum number \(n\) (which energy state to calculate)
\end{itemize}

\textbf{Features}  
\begin{itemize}
    \item Compute analytical energy: \(E_n = \frac{n^2 \pi^2 \hbar^2}{2 m L^2}\)  
    \item Compute exact wave function \(\psi_n(x)\)  
    \item Solve Schr\"odinger equation numerically using second derivative discretization  
    \item Automatic normalization of the numerical wave function  
    \item Plot: exact and numerical wave functions, probability density \(|\psi|^2\), and direct comparison
\end{itemize}

\section*{9. Project Outputs}

At the end, the program produces:  
\begin{itemize}
    \item Analytical wave function  
    \item Numerical (approximate) wave function  
    \item Comparison plot  
    \item Probability density  
    \item Quantized energy of the chosen state
\end{itemize}

\end{document}
