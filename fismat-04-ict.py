import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Discretisasi domain
N = 100
x = np.linspace(0, 1, N)  # Kita anggap L = 1
dx = x[1] - x[0]

# Fungsional: J[r] = ∫ (1 / r^4) dx
def functional3(r):
    integrand = 1 / r**4
    return np.sum(integrand) * dx

# Tebakan awal: radius konstan
r0 = np.ones(N) * 0.5

# Batas radius untuk mencegah pembagian oleh nol atau radius tidak realistis
bounds = [(0.1, 2.0) for _ in range(N)]  # batas minimum dan maksimum radius

# Optimisasi
res = minimize(functional3, r0, bounds=bounds, method='L-BFGS-B')
r_opt = res.x

# Plot hasil profil radius optimal
plt.figure(figsize=(10, 5))
plt.plot(x, r0, 'k--', label="Radius awal")
plt.plot(x, r_opt, 'b-', label="Radius optimal (minim resistansi)")
plt.xlabel("x (panjang pipa)")
plt.ylabel("r(x) (radius)")
plt.title("Profil Radius Pipa Optimal untuk Minimalkan Energi yang Hilang")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()