import numpy as np
import matplotlib.pyplot as plt

# Waktu
t = np.linspace(0, 5, 1000)

# Fungsi arus i(t) dan tegangan v(t)
i_t = 10 * np.sin(2 * t)
v_t = 1000 * np.sin(2 * t) - 4998 * np.cos(2 * t)

# Plot i(t) dan v(t)
plt.figure(figsize=(10, 6))
plt.plot(t, i_t, label='i(t) = 10 sin(2t)', linestyle='--', color='blue')
plt.plot(t, v_t, label='v(t) = 1000 sin(2t) - 4998 cos(2t)', color='red')
plt.title('Respons Tegangan dan Arus pada Rangkaian RLC')
plt.xlabel('Waktu (s)')
plt.ylabel('Arus (A) dan Tegangan (V)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
