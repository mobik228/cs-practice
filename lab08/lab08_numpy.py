import numpy as np
# 1 задание

hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity_mat = np.eye(3, dtype=int)
print(hours)
print(hours.shape)
print(hours.ndim)
print(hours.size)
print(hours.dtype)
# задание 2
print(f"третий элемент {hours[2]}, последний элемент {hours[-1]}, элементы с индексами 2–5 {hours[1:5]},"
      f"массив в обратном порядке {hours[::-1]}, каждый второй элемент {hours[::2]}")
# задание 3
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])
print(f"Значение из 2-й строки и 3-го столбца: {temperatures[1, 2]}, первая строка {temperatures[0, :]},"
      f"последний столбец {temperatures[:, 3]}, первые две строки без первого столбца {temperatures[:2, 1:]}"
      f" центральный фрагмент 2×2 {temperatures[:2, 1:]}")