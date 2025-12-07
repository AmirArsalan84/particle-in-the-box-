import numpy as np
import matplotlib.pyplot as plt

# ابتدا طول جعبه و عدد کوانتومی رو از کاربر دریافت میکنیم
L = float(input("Enter the length of the well (L): "))
n = int(input("Enter the Quantum number (n): "))

hbar = 1.054571817e-34
m = 9.1093837e-31

# برای حل عددی معادله دیفرانسیل شبکه نقاط رو تعریف میکنیم
N = 100
x = np.linspace(0, L, N)
dx = x[1] - x[0] #دیفرانسیل طول برای حل عددی

# حل با روابط اصلی یا حل آنالیزی
E = (n**2 * np.pi**2 * hbar**2) / (2 * m * L**2)
psi_exact = np.sqrt(2/L) * np.sin(n * np.pi * x / L)

#حل با استفاده از مشتق دوم (به دست امده از بسط تیلور)
psi = np.sqrt(2/L) * np.sin(n * np.pi * x / L)
psi_dd = np.zeros_like(psi)
psi_dd[1:-1] = (psi[2:] - 2*psi[1:-1] + psi[:-2])/dx**2
psi_approx = []
psi_approx.append(0)
psi_approx.append(1e-6)
c = 2*m*E*(dx**2)/hbar**2

for i in range (1 , N-1) :
    psi_approx_next = psi_approx[i] * (2-c) - psi_approx[i-1]
    psi_approx.append(psi_approx_next)

#باید تقریب به دست آمده را نرمال کنیم یعنی به ضریبی آن را تقسیم کنیم که شرط بهنجارش تابع موج ارضا شود
np.array(psi_approx)
norm = np.sqrt(np.sum(np.pow(psi_approx,2))*dx)
psi_approx = psi_approx/norm 


plt.figure(figsize=(12, 5))

#رسم تابع موج
plt.subplot(1, 2, 1)
plt.plot(x, psi_exact, 'b-', label='Analytical (Exact)', linewidth=2)
plt.plot(x, psi_approx , 'r--', label='Approximation', linewidth=1)
plt.title(f"Wavefunction (n={n})")
plt.xlabel("x")
plt.ylabel("$\psi(x)$")
plt.legend()

#رسم چگالی احتمال
plt.subplot(1, 2, 2)
plt.plot(x, psi_exact**2, 'g-', label='$|\psi|^2$ Analytical')
plt.fill_between(x, psi_exact**2, color='green', alpha=0.3)
plt.title("Probability Density")
plt.xlabel("x")
plt.ylabel("$|\psi(x)|^2$")
plt.legend()

plt.show()

print(f"Energy : {E}")
