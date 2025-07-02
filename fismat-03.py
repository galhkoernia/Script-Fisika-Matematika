import numpy as np
from scipy.integrate import simpson
import matplotlib.pyplot as plt

# Datawh
L = 20
terms = 10
x = np.linspace(0, L, 1000)

# Fungsi potongan untuk F(x)
F = lambda x: np.piecewise(x,
                           [((x >= 0) & (x < 10)), ((x >= 10) & (x <= 20))],
                           [lambda x: 0, lambda x: 100])

# Koefisien Fourier
a0 = 0
an = lambda n: 0
bn = lambda n: (2 / L) * simpson(F(x) * np.sin(n * np.pi * x / L), x=x)

# bn untuk  n
bn_values = [bn(n) for n in range(1, terms + 1)]

# Nilai y
y = 5

# Fungsi Fourier
T = lambda x: sum([
    bn_values[n - 1] * np.sin(n * np.pi * x / L) * np.exp(-n * np.pi * y / L)
    for n in range(1, terms + 1)
])

T_values = np.array([T(xi) for xi in x])

# Plotting
plt.plot(x, F(x), label="F(x) Batas Nilai", linestyle='--')
plt.plot(x, T_values, label="Solusi Fourier untuk y = 5")
plt.grid()
plt.xlabel("$x$")
plt.ylabel("$T(x, y)$")
plt.legend(loc='best', prop={'size': 10})
plt.title("Deret Fourier Semi-Infinite")
plt.show()


# Definisi Fungsi
L     = 4
terms = 5
x     = np.arange(-L, L, 0.001)

F = lambda x : np.piecewise(x,
                      [((x >= 0) & (x < 2)), ((x >= 2) & (x < 4)),
                       ((x >= -4) & (x < -2)), ((x >= -2) & (x < 0))],
                      [lambda x : 3*x - 1, 5, lambda x : 5, lambda x : 3 * x + 1])
# Perhitungan
a0 = 1/1 * simps(F(x), x)
an = lambda n: 1/L * simps(F(x) * np.cos(np.pi * n * x / L), x)
bn = lambda n: 1/L * simps(F(x) * np.sin(np.pi * n * x / L), x)
print('a0 =', a0)
print('an =', [an(n) for n in range(1, terms+1)])
print('bn =', [bn(n) for n in range(1, terms+1)])

s = a0/2 + sum([an(n) * np.cos(np.pi * n * x / L) + bn(n) * np.sin(np.pi * n * x / L) for n in range(1, terms+1)])

# Plotting
plt.plot(x, s, label="Fourier")
plt.grid()
plt.ylim(-10, 10)
plt.xlabel("$x$")
plt.ylabel("$y=f(x)$")
plt.legend(loc='best', prop={'size':10})
plt.title("Deret Fourier (n=5)")
plt.show()

# Fuction to plot the Fourier series
# Data
L = 20
terms = 10
x = np.linspace(0, L, 1000)
dx = x[1] - x[0]

# Fungsi batas bawah y = 0
def boundary_condition(x):
    return np.piecewise(
        x,
        [((x >= 0) & (x < 10)), ((x >= 10) & (x <= 20))],
        [lambda x: 0, lambda x: 100]
    )

# Fungsi Fourier bn
def bn(n):
    F = boundary_condition(x)
    integrand = F * np.sin(n * np.pi * x / L)

# Koefisien bn untuk n
bn_values = [bn(n) for n in range(1, terms + 1)]

# Solusi Fourier T(x, y)
def T(x, y):
    result = np.zeros_like(x)
    for n in range(1, terms + 1):
        result += bn_values[n - 1] * np.sin(n * np.pi * x / L) * np.exp(-n * np.pi * y / L)
    return result
plt.figure(figsize=(10, 6))

# Plotting
for y in [0, 5, 10]:
    T_values = T(x, y)
    plt.plot(x, T_values, label=f"$y = {y}$")

plt.plot(x, boundary_condition(x), 'k--', label="Kondisi Batas (y=0)")  # Plot kondisi batas
plt.grid()
plt.xlabel("$x$ (Posisi disepanjang Plat)")
plt.ylabel("$T(x, y)$ (Suhu)")
plt.title("Distribusi Suhu pada Pelat Semi-Tak Hingga")
plt.legend(loc='best')
plt.show()