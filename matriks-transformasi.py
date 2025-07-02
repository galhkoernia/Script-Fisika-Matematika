# <-- soal nomor 2 3 -->>
# Soal 2
import numpy as np

A = np.array([[3, 4, 1], 
              [2, -7, -1], 
              [8, 1, 5]])

B = np.array([[8, 1, 5], 
              [2, -7, -1], 
              [3, 4, 1]])

A_inv = np.linalg.inv(A)
E1 = np.dot(B, A_inv)
print("Matriks E1:")
print(E1)

# Soal 3
import numpy as np
import matplotlib.pyplot as plt

theta = np.radians(60)
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta),  np.cos(theta)]])

P_x = np.array([[1, 0],
                [0, 0]])

M_y = np.array([[-1, 0],
                [0,  1]])

T = M_y * P_x * R

print("T=", T)
print("Matriks Transformasi Total:")
print(T)

v = np.array([2, 3])

v_trans = T * v

plt.figure(figsize=(6,6))
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', color='r', scale=1, label="Vektor Asli")
plt.quiver(0, 0, v_trans[0], v_trans[1], angles='xy', scale_units='xy', color='b', scale=1, label="Vektor Transformasi")

plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.grid()
plt.legend()
plt.title("Matriks Transformasi")
plt.show()