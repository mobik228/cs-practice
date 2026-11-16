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
