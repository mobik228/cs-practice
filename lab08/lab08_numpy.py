import numpy as np
#1 задание
print('---------------1 задание---------------------')
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
print('---------------2 задание---------------------')
# задание 2
print(f"третий элемент {hours[2]}, последний элемент {hours[-1]}, элементы с индексами 2–5 {hours[1:5]},"
      f"массив в обратном порядке {hours[::-1]}, каждый второй элемент {hours[::2]}")
print('---------------3 задание---------------------')
# задание 3
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])
print(f"Значение из 2-й строки и 3-го столбца: {temperatures[1, 2]}, первая строка {temperatures[0, :]},"
      f"последний столбец {temperatures[:, 3]}, первые две строки без первого столбца {temperatures[:2, 1:]}"
      f" центральный фрагмент 2×2 {temperatures[:2, 1:3]}")
print('---------------4 задание---------------------')
# задание 4
matrix = np.arange(1, 26).reshape(5, 5)
print(f"изначальная матрица {matrix}, shape {matrix.shape}")
print(f'первые три строки {matrix[0:3]}, shape {matrix[0:3].shape}')
print(f" последние две строки {matrix[-2:]}, shape {matrix[-2:].shape}")
print(f"первые два столбца {matrix[:, :2]}, shape {matrix[:, :2].shape}")
print(f'фрагмент из строк с индексами 1–3 и столбцов 2–4 '
      f'{matrix[0:3, 1:4]}, shape {matrix[0:3, 1:4].shape} ')
print(f'угловой блок 2×2 в правом нижнем углу {matrix[3:, 3:]}, shape {matrix[3:, 3:].shape}')
print('---------------5 задание---------------------')
#задание 5
changed_hours = hours.copy()
print(changed_hours)
changed_hours[1:4] = 99
changed_hours[::2] = -1
print(changed_hours)
print('------matrix----------------')
changed_matrix = matrix.copy()
print(changed_matrix)
changed_matrix[1:2, :] = 0
changed_matrix[:, -1:] = -1
changed_matrix[1:4, 1:4] = 100
print(changed_matrix)
#.copy(): в NumPy срезы не создают новый массив, а возвращают представление (view) — ссылку на ту же самую область памяти
print('---------------задание 6 ____________')
numbers = np.arange(0, 12)
table = numbers.reshape(3, 4)
transposed = table.T
print(numbers)
print(table)
print(transposed)
# 3 * 4 = 12 а 5 * 3 = 15