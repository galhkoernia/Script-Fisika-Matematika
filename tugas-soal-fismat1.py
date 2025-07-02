#Tugas Fisika Matematika IV {ICT}
#<!- Soal Nomor 1 ->
# Soal: Pesawat terbang harus menghindari zona bahaya yang didefinisikan oleh fungsi penalti P(x, y).
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

a, b   = 0, 10
y0, yN = 0, 0
N      = 100
x      = np.linspace(a, b, N)
dx     = x[1] - x[0]

def P(x, y):
    x  = np.asarray(x)
    y  = np.asarray(y)
    if x.shape != y.shape:
        raise ValueError(f"Shape mismatch: x has shape {x.shape}, y has shape {y.shape}")
    r1 = np.exp(-((x-5)**2 + (y-5)**2) / 2)
    r2 = np.exp(-((x-5)**2 + (y-3)**2) / 1.5)
    return r1 + 5*r1 + 8 * r2

def functional(y):
    y       = np.asarray(y)
    dy      = np.diff(y) / dx
    avg_y   = (y[:-1] + y[1:]) / 2
    avg_x   = (x[:-1] + x[1:]) / 2
    arc     = np.sqrt(1 + dy**2)
    penalty = P(avg_x, avg_y)
    return np.sum(arc * penalty * dx)

def full_y(vars):
    return np.concatenate(([y0], vars, [yN]))

def objective(vars):
    y = full_y(vars)
    return functional(y)

y_initial   = np.linspace(y0, yN, N)
y_vars_init = y_initial[1:-1]
result      = minimize(objective, y_vars_init, method='L-BFGS-B')
y_optimal   = full_y(result.x)

X, Y        = np.meshgrid(x, x)
Z           = P(X, Y)

# Visualisasi
X, Y               = np.meshgrid(x, np.linspace(-2, 7, 200))
Z                  = P(X, Y)
plt.figure(figsize = (7, 5))
plt.contourf(X, Y, Z, levels=50, cmap='hot')
plt.plot(x, y_optimal, 'cyan', lw=2, label='Lintasan Optimal')
plt.title("Jalur Pesawat Menghindari Zona Bahaya")
plt.xlabel("x")
plt.ylabel("y")
plt.colorbar(label="Penalti P(x, y)")
plt.legend()
plt.grid(True)
plt.show()