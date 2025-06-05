from qutip import *
import numpy as np
import matplotlib.pyplot as plt

# Параметры
T1 = 50  # релаксация (условные нс)
T2 = 30  # декогеренция
w = 2 * np.pi * 1.0  # частота кубита (в ГГц)
times = np.linspace(0, 100, 200)

# Начальное состояние — суперпозиция |+>
psi0 = (basis(2, 0) + basis(2, 1)).unit()

# Гамильтониан: вращение вокруг оси Z
H = 0.5 * w * sigmaz()

# Коллапс-операторы для T1 и T2
c_ops = []
if T1 > 0.0:
    c_ops.append(np.sqrt(1.0 / T1) * sigmam())
if T2 > 0.0:
    c_ops.append(np.sqrt(1.0 / T2 - 1.0 / (2 * T1)) * sigmaz())

# Эволюция
result = mesolve(H, psi0, times, c_ops, [sigmax(), sigmay(), sigmaz()])

# График
plt.plot(times, result.expect[0], label="⟨X⟩")
plt.plot(times, result.expect[1], label="⟨Y⟩")
plt.plot(times, result.expect[2], label="⟨Z⟩")
plt.title("Эволюция кубита (с учётом T1 и T2)")
plt.xlabel("Время (нс)")
plt.ylabel("Ожидаемое значение")
plt.legend()
plt.grid()
plt.show()