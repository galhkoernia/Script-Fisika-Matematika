# FISMAT IV - ICT
import numpy as np
import matplotlib.pyplot as plt

# <-- Matriks -->>
A = np.array([
    [1, 2, 3],
    [7, 8, 9],
    [9, 7, 6]
])
B = np.array([
    [2, 3, 6],
    [7, 4, 2],
    [6, 7, 9]
])

print("A =", A)
print("B =", B)
print("A+B=", A+B)
print("A-B=", A-B)
print("A*B=", A*B)
print("A/B=", A/B)
print("np.dot(A,B)=", np.dot(A,B))
print("np.cross(A,B)=", np.cross(A,B))

# <<-- Matriks Transpose -->>
# Matriks 
A = np.array([
    [1, 2, 3],
    [7, 8, 9],
    [9, 7, 6]
])
B = np.array([
    [2, 3, 6],
    [7, 4, 2],
    [6, 7, 9]
])
# A
A_trans = np.transpose(A)
print("A_trans=", A_trans)

A_Inv = np.linalg.inv(A)
print("A_Inv=", A_Inv)

A_det = np.linalg.det(A)
print("A_det=", A_det)

# B
B_trans = np.transpose(B)
print("B_trans=", B_trans)

B_Inv = np.linalg.inv(B)
print("B_Inv=", B_Inv)

B_det = np.linalg.det(B)
print("B_det=", B_det)

# <-- Metode Cramer -->>

A1 = np.array (
    [2, -1, 3, 4],
    [1, 0, -2, 7],
    [3, -3, 1, 5],
    [2, 1, 4, 4
])

B1 = np.array([9, 11, 8, 10])

I = np.linalg.solve(A1, B1)
print("(I1, I2, I3, I4) =", I)

# <-- Operasi Vektor -->>

vctr = np.array([1, 2, 4])
print("vctr=",vctr)
magnitude = np.linalg.norm(vctr)
print("magnitude=", magnitude)
vctr_unit=vctr/magnitude
print("vektor satuan=", vctr_unit)

# <-- Transvormasi -->>
import numpy as np
import matplotlib.pyplot as plt

v = [2, 4]
w = [4, 2]
array = np.array([[0, 0, v[0], v[1]],
    [0, 0, w[0], w[1]]
])

X, Y, V, W = array.T

plt.figure()
plt.ylabel("Y-axis")
plt.xlabel("X-axis")
ax = plt.gca()
ax.annotate(f"[{V[0]},{W[0]}]", (X[0] + V[0], Y[0] + W[0]), fontsize=14)
ax.scatter(X[0] + V[0], Y[0] + W[0], c="red")
ax.annotate(f"[{V[1]},{W[1]}]", (X[1] + V[1], Y[1] + W[1]), fontsize=14)
ax.scatter(X[1] + V[1], Y[1] + W[1], c="blue")
ax.quiver(X, Y, V, W, angles="xy", scale_units="xy", color=["r", "b"], scale=1)
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
plt.grid()
plt.draw()
plt.show()

# <<-- Transformasi Vektor -->
# Horizontal Vektor
A2 = [5, 7, 9]
vector = np.array(A2)
print("vector=", vector)

# Vertical Vektor

lst = [10,20,30,40,50,60,70,80,90,100]
vctr = np.array(lst)

print("Vector created from list:")
print(vctr)


# Orde 2
A = np.array([[1, 2], [3, 4]])

print("\nMatrix A:")
print(A)

# Operasi matriks Tensor

# Vektor Eigen dan Nilai Eigen
from numpy.linalg import eig

I = np.array([
    [4, 2, 0],
    [2, 3, -1],
    [0, -1, 5]
])

W, V = eig(I)

print("Nilai Eigen =", W)
print("Vektor Eigen =")
print(V)

# Tensor Inersia
A = np.matrix([[1, 2], [3, 4]])
plt.inshow(A, interpolation='nearest', cmap='gray')
plt.title("Tensor Inersia")
plt.show()