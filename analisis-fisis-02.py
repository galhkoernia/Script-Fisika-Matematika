import numpy as np
import matplotlib.pyplot as plt

# Definisi waktu kontinu & sinyal kontinu
t = np.linspace(0, 1, 1000)

xa = 4 * np.cos(3 * np.pi * t) + 6 * np.sin(2 * np.pi * t)

# Visualisasi Sinyal Analog
plt.figure(figsize=(6, 4))
plt.plot(t, xa, label=r'$x_a(t) = 4\cos(3\pi t) + 6\sin(2\pi t)$')
plt.title('Sinyal Analog x_a(t) dari t=0 sampai t=1')
plt.xlabel('t (detik)')
plt.ylabel('x_a(t)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


# Gambarkan pulsa diskrit dengan metode sampling
import numpy as np
fs          = 1000
Ts          = 1 / fs
t_sampled   = np.arange(0, 1, Ts)
xa_sampled  = 4 * np.cos(3 * np.pi * t_sampled) + 6 * np.sin(2 * np.pi * t_sampled)

# Visualisasi sinyal diskrit (sampling)
plt.figure(figsize=(8, 4))
plt.stem(t_sampled, xa_sampled, basefmt=" ", linefmt='blue', markerfmt='bo')
plt.title('Sinyal Diskrit Hasil Sampling dari x_a(t)')
plt.xlabel('t (detik)')
plt.ylabel('x[n]')
plt.grid(True)
plt.tight_layout()
plt.show()