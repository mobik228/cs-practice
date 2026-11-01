import numpy as np

def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    matrix = np.array(values, dtype=float)
    ln = len(values)
    if ln % width != 0:
        return []
    matrix = matrix.reshape(ln//width, width)
    return matrix.tolist()



def block(matrix: list[list[float]], rows: list[int], columns: list[int]) -> list[list[float]]:
    if len(matrix) == 0:
        return []
    arr = np.asarray(matrix, dtype=float)
    part = arr[np.ix_(rows, columns)]
    return part.tolist()

def column_means(matrix: list[list[float]]) -> list[float]:
    if len(matrix) == 0:
        return []
    arr = np.asarray(matrix, dtype=float)
    avg = arr.mean(axis=0)
    return np.round(avg, 6).tolist()


def column_range(matrix: list[list[float]], column: int) -> float:
    if len(matrix) == 0:
        return 0.0
    arr = np.asarray(matrix, dtype=float)
    part = arr[:, column]
    res = max(part) - min(part)
    return round(float(res), 6)


if __name__ == '__main__':
    print(reshape_rows([12, 14.5, 11, 13, 15.5, 10.5], 3))
    # [[12.0, 14.5, 11.0], [13.0, 15.5, 10.5]]

    print(block([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [0, 2], [1, 2]))
    # [[2.0, 3.0], [8.0, 9.0]]

    print(column_means([[1, 2], [3, 4], [5, 6]]) ) # [3.0, 4.0]
    print(column_range([[1, 2], [5, 7]], 1))  # 5.0
