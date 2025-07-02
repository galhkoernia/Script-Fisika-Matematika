import numpy as np
import matplotlib.pyplot as plt

#2a Definisi Sinyal x(n)
def x(n):
    result = []
    for ni in n:
        if -4 <= ni <= -2:
            result.append(2 + ni / 2)
        elif 0 <= ni <= 4:
            result.append(np.cos(ni * np.pi / 4))
        else:
            result.append(0)
    return np.array(result)

# Rentang nilai n
n = np.arange(-5, 6)
x_n = x(n)

# visualisasi Sinyal x(n)
plt.figure(figsize=(6, 4))
plt.stem(n, x_n, basefmt=" ", linefmt='b-', markerfmt='bo')
plt.title('Sinyal Diskrit x(n)')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.xticks(np.arange(-5, 6, 1))
plt.show()

#2b Definisi sinyal X(n)
def x(n):
    result = []
    for ni in n:
        if -4 <= ni <= -2:
            result.append(2 + ni / 2)
        elif 0 <= ni <= 4:
            result.append(np.cos(ni * np.pi / 4))
        else:
            result.append(0)
    return np.array(result)

# Rentang n
n = np.arange(-10, 11)

# Transformasi lipat lalu geser --> x (-n - 3)
x_shift_then_flip = x(-n - 3)

# Visualisasi Sinyal x(-n - 3)
plt.figure(figsize=(6, 4))
plt.stem(n, x_shift_then_flip, basefmt=" ", linefmt='g-', markerfmt='go')
plt.title('Transformasi : dilipat lalu digeser ke kanan 3 satuan')
plt.xlabel('n')
plt.ylabel('x(-n - 3)')
plt.grid(True)
plt.xticks(np.arange(-10, 11, 1))
plt.show()

#2c Definisi Sinyal x(-(n-3))
def x(n):
    result = []
    for ni in n:
        if -4 <= ni <= -2:
            result.append(2 + ni / 2)
        elif 0 <= ni <= 4:
            result.append(np.cos(ni * np.pi / 4))
        else:
            result.append(0)
    return np.array(result)

n = np.arange(-10, 11)
x_flip_after_shift = x(-(n - 3))

plt.figure(figsize=(6, 4))
plt.stem(n, x_flip_after_shift, basefmt=" ", linefmt='r-', markerfmt='ro')
plt.title('Transformasi: Geser ke Kanan 3 Satuan lalu Lipat)')
plt.xlabel('n')
plt.ylabel('x(-(n+3))')
plt.grid(True)
plt.xticks(np.arange(-10, 11, 1))
plt.show()

