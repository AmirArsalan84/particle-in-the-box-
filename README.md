Solving the One-Dimensional Infinite Potential Well Using Analytical and Numerical Methods

This project solves the time-independent Schrödinger equation for a one-dimensional infinite potential well using two methods:

Analytical (Exact) Solution

Numerical Solution using Taylor expansion and discretization of the second derivative.

The goal is to compare the exact wave function with the numerical approximation and to examine the structure of quantized energies.

1. Physics of the Problem: Infinite Potential Well

The potential:

𝑉
(
𝑥
)
=
{
0
,
	
0
<
𝑥
<
𝐿


∞
,
	
otherwise
V(x)={
0,
∞,
	​

0<x<L
otherwise
	​


The particle cannot escape the well, so the boundary conditions are:

𝜓
(
0
)
=
0
,
𝜓
(
𝐿
)
=
0
ψ(0)=0,ψ(L)=0
2. Time-Independent Schrödinger Equation

Inside the well (
𝑉
=
0
V=0):

−
ℏ
2
2
𝑚
𝑑
2
𝜓
𝑑
𝑥
2
=
𝐸
𝜓
−
2m
ℏ
2
	​

dx
2
d
2
ψ
	​

=Eψ

or equivalently:

𝑑
2
𝜓
𝑑
𝑥
2
=
−
𝑘
2
𝜓
dx
2
d
2
ψ
	​

=−k
2
ψ

where

𝑘
=
2
𝑚
𝐸
ℏ
k=
ℏ
2mE
	​

	​

3. Analytical Solution

General solution:

𝜓
(
𝑥
)
=
𝐶
1
sin
⁡
(
𝑘
𝑥
)
+
𝐶
2
cos
⁡
(
𝑘
𝑥
)
ψ(x)=C
1
	​

sin(kx)+C
2
	​

cos(kx)

Boundary condition 
𝜓
(
0
)
=
0
⇒
𝐶
2
=
0
ψ(0)=0⇒C
2
	​

=0:

𝜓
(
𝑥
)
=
𝐶
1
sin
⁡
(
𝑘
𝑥
)
ψ(x)=C
1
	​

sin(kx)

Boundary condition 
𝜓
(
𝐿
)
=
0
⇒
sin
⁡
(
𝑘
𝐿
)
=
0
ψ(L)=0⇒sin(kL)=0:

𝑘
𝐿
=
𝑛
𝜋
,
𝑛
=
1
,
2
,
3
,
…
kL=nπ,n=1,2,3,…

So:

𝑘
=
𝑛
𝜋
𝐿
k=
L
nπ
	​


Allowed energies:

𝐸
𝑛
=
𝑛
2
𝜋
2
ℏ
2
2
𝑚
𝐿
2
E
n
	​

=
2mL
2
n
2
π
2
ℏ
2
	​


Normalized wave function:

𝜓
𝑛
(
𝑥
)
=
2
𝐿
 
sin
⁡
(
𝑛
𝜋
𝑥
𝐿
)
ψ
n
	​

(x)=
L
2
	​

	​

sin(
L
nπx
	​

)
4. Numerical Second Derivative Using Taylor Expansion

Divide the interval into points:

𝑥
0
,
𝑥
1
,
𝑥
2
,
…
,
𝑥
𝑁
−
1
x
0
	​

,x
1
	​

,x
2
	​

,…,x
N−1
	​


with spacing:

𝑑
𝑥
=
𝑥
𝑖
+
1
−
𝑥
𝑖
dx=x
i+1
	​

−x
i
	​


Taylor expansion for 
𝜓
(
𝑥
)
ψ(x):

𝜓
(
𝑥
+
𝑑
𝑥
)
=
𝜓
(
𝑥
)
+
𝜓
′
(
𝑥
)
𝑑
𝑥
+
1
2
𝜓
′
′
(
𝑥
)
𝑑
𝑥
2
+
…
ψ(x+dx)=ψ(x)+ψ
′
(x)dx+
2
1
	​

ψ
′′
(x)dx
2
+…
𝜓
(
𝑥
−
𝑑
𝑥
)
=
𝜓
(
𝑥
)
−
𝜓
′
(
𝑥
)
𝑑
𝑥
+
1
2
𝜓
′
′
(
𝑥
)
𝑑
𝑥
2
+
…
ψ(x−dx)=ψ(x)−ψ
′
(x)dx+
2
1
	​

ψ
′′
(x)dx
2
+…

Adding these:

𝜓
(
𝑥
+
𝑑
𝑥
)
+
𝜓
(
𝑥
−
𝑑
𝑥
)
=
2
𝜓
(
𝑥
)
+
𝜓
′
′
(
𝑥
)
𝑑
𝑥
2
+
𝑂
(
𝑑
𝑥
4
)
ψ(x+dx)+ψ(x−dx)=2ψ(x)+ψ
′′
(x)dx
2
+O(dx
4
)

Numerical second derivative:

𝜓
′
′
(
𝑥
)
≈
𝜓
(
𝑥
+
𝑑
𝑥
)
−
2
𝜓
(
𝑥
)
+
𝜓
(
𝑥
−
𝑑
𝑥
)
𝑑
𝑥
2
ψ
′′
(x)≈
dx
2
ψ(x+dx)−2ψ(x)+ψ(x−dx)
	​

5. Discretization of the Schrödinger Equation

Inside the well:

𝜓
′
′
(
𝑥
)
=
−
𝑘
2
𝜓
(
𝑥
)
ψ
′′
(x)=−k
2
ψ(x)

Substitute the numerical second derivative:

𝜓
𝑖
+
1
−
2
𝜓
𝑖
+
𝜓
𝑖
−
1
𝑑
𝑥
2
=
−
𝑘
2
𝜓
𝑖
dx
2
ψ
i+1
	​

−2ψ
i
	​

+ψ
i−1
	​

	​

=−k
2
ψ
i
	​


Multiply by 
𝑑
𝑥
2
dx
2
:

𝜓
𝑖
+
1
=
(
2
−
𝑘
2
𝑑
𝑥
2
)
𝜓
𝑖
−
𝜓
𝑖
−
1
ψ
i+1
	​

=(2−k
2
dx
2
)ψ
i
	​

−ψ
i−1
	​


Since 
𝑘
2
=
2
𝑚
𝐸
ℏ
2
k
2
=
ℏ
2
2mE
	​

, define:

𝑐
=
𝑘
2
𝑑
𝑥
2
=
2
𝑚
𝐸
𝑑
𝑥
2
ℏ
2
c=k
2
dx
2
=
ℏ
2
2mEdx
2
	​


Recurrence formula:

𝜓
𝑖
+
1
=
(
2
−
𝑐
)
𝜓
𝑖
−
𝜓
𝑖
−
1
ψ
i+1
	​

=(2−c)ψ
i
	​

−ψ
i−1
	​

6. Initial Values for Numerical Solution

Since 
𝜓
(
0
)
=
0
ψ(0)=0:

𝜓
0
=
0
ψ
0
	​

=0

To avoid the sequence being entirely zero, use a small initial value:

𝜓
1
=
𝜖
ψ
1
	​

=ϵ
7. Normalization of the Wave Function

Normalization condition:

∫
0
𝐿
∣
𝜓
(
𝑥
)
∣
2
𝑑
𝑥
=
1
∫
0
L
	​

∣ψ(x)∣
2
dx=1

In the numerical approximation:

∑
𝑖
𝜓
𝑖
2
𝑑
𝑥
=
1
i
∑
	​

ψ
i
2
	​

dx=1

Normalize:

𝜓
𝑖
←
𝜓
𝑖
∑
𝑗
𝜓
𝑗
2
𝑑
𝑥
ψ
i
	​

←
∑
j
	​

ψ
j
2
	​

dx
	​

ψ
i
	​

	​

8. Program Features and Inputs

Inputs

Well length 
𝐿
L (from the user)

Quantum number 
𝑛
n (which energy state to calculate)

Features

Compute analytical energy: 
𝐸
𝑛
=
𝑛
2
𝜋
2
ℏ
2
2
𝑚
𝐿
2
E
n
	​

=
2mL
2
n
2
π
2
ℏ
2
	​


Compute exact wave function 
𝜓
𝑛
(
𝑥
)
ψ
n
	​

(x)

Solve Schrödinger equation numerically using second derivative discretization

Automatic normalization of the numerical wave function

Plot: exact and numerical wave functions, probability density 
∣
𝜓
∣
2
∣ψ∣
2
, and direct comparison

9. Project Outputs

At the end, the program produces:

Analytical wave function

Numerical (approximate) wave function

Comparison plot

Probability density

Quantized energy of the chosen state
