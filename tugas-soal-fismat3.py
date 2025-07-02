#Tugas Fisika Matematika IV {ICT}
#<!- Soal Nomor 3 ->
# Soal: Menentukan profil radius pipa r(x) yang meminimalkan kehilangan energi akibat resistansi fluida
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

L    = 10
N    = 100
x    = np.linspace(0, L, N)
dx   = x[1] - x[0]

def objective(r):
    return np.sum(1.0 / r**4) * dx
def constraint_volume(r):
    volume_target = 5.0
    return np.sum(r**2) * dx - volume_target

r_min  = 0.1
r_max  = 2.0
r_init = np.ones(N) * 1.0

constraints = {'type': 'eq', 'fun': constraint_volume}
bounds      = [(r_min, r_max) for _ in range(N)]
result      = minimize(objective, r_init, method='SLSQP', bounds=bounds, constraints=constraints)
r_optimal   = result.x

# visualisasi
plt.figure(figsize=(7, 5))
plt.plot(x, r_optimal, label='Profil Radius Optimal', color='blue')
plt.xlabel('x (panjang pipa)')
plt.ylabel('r(x) (radius)')
plt.title('Profil Radius Pipa yang Meminimalkan Kehilangan Energi')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()