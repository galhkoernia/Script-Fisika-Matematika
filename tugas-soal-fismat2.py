#Tugas Fisika Matematika IV {ICT}
#<!- Soal Nomor 2 ->
# Soal: Mencari bentuk lintasan landasan miring yang meminimalkangaya gesektotal selama peluncurankendaraan berat atau roket.
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

a, b   = 0, 10
y0, yN = 0, 5
N      = 100
x      = np.linspace(a, b, N)
dx     = x[1] - x[0]

def mu(y):
    return 0.1 + 0.5 * y
def N_force(dy):
    return 9.8 / np.sqrt(1 + dy**2)
def functional(y):
    y      = np.asarray(y)
    dy     = np.diff(y) / dx
    avg_y  = (y[:-1] + y[1:]) / 2
    mu_val = mu(avg_y)
    N_val  = N_force(dy)
    arc    = np.sqrt(1 + dy**2)
    return np.sum(mu_val * N_val * arc * dx)
def full_y(vars):
    return np.concatenate(([y0], vars, [yN]))
def objective(vars):
    y = full_y(vars)
    return functional(y)

y_initial   = np.linspace(y0, yN, N)
y_vars_init = y_initial[1:-1]
result      = minimize(objective, y_vars_init, method='L-BFGS-B')
y_optimal   = full_y(result.x)

# Visualisasi
plt.figure(figsize=(7, 5))
plt.plot(x, y_optimal, 'cyan', lw=2, label='Lintasan Optimal')
plt.title("Lintasan untuk Meminimalkan Gaya Gesek Total")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()