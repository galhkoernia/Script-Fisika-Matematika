#Tugas Fisika Matematika IV {ICT}
#<!- Soal Nomor 5 ->
# Soal: Menentukan lintasan partikel dari titik A ke B yang melewati suatu medan potensialdua dimensi V(x, y)
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

a,b  = 0, 10
N    = 100
x    = np.linspace(a, b, N)
dx   = x[1] - x[0]
m    = 1.0

def V(x, y):
    return np.exp(-((x - 3)**2 + (y - 2)**2)) + np.exp(-((x - 7)**2 + (y - 3)**2))
def functional(y):
    dy_dx     = np.gradient(y, dx)
    kinetic   = 0.5 * m * (1 + dy_dx**2)
    potential = V(x, y)
    return np.sum((kinetic + potential) * dx)
def constraint_start_end(y):
    return [y[0] - ya, y[-1] - yb]

constraints   = ({
    'type': 'eq',
    'fun': lambda y: y[0] - ya
}, {
    'type': 'eq',
    'fun': lambda y: y[-1] - yb
})
ya, yb    = 0.0, 5.0
y_initial = np.linspace(ya, yb, N)
result    = minimize(functional, y_initial, method='SLSQP', constraints=constraints, options={'disp': True, 'maxiter': 500})
y_optimal = result.x


# Visualisasi
X, Y      = np.meshgrid(x, x)
plt.figure(figsize=(7, 5))
plt.plot(x, y_optimal, label='Lintasan Optimal')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Lintasan Partikel dalam Medan Potensial V(x, y)')
plt.grid(True)
plt.legend()
plt.show()