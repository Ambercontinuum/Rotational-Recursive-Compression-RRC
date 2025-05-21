
import numpy as np

def R_index(i, j, k, n, axis, dir_):
    if axis == 'z' and dir_ == 1:
        return j, n - 1 - i, k
    elif axis == 'z' and dir_ == -1:
        return n - 1 - j, i, k
    elif axis == 'x' and dir_ == 1:
        return i, n - 1 - k, j
    elif axis == 'x' and dir_ == -1:
        return i, k, n - 1 - j
    elif axis == 'y' and dir_ == 1:
        return k, j, n - 1 - i
    elif axis == 'y' and dir_ == -1:
        return n - 1 - k, j, i
    return i, j, k

def rotate_tensor(tensor, axis, dir_):
    n = tensor.shape[0]
    rotated = np.zeros_like(tensor)
    for i in range(n):
        for j in range(n):
            i_, j_, k_ = R_index(i, j, 0, n, axis, dir_)
            rotated[i_, j_, 0] = tensor[i, j, 0]
    return rotated

def rrc_multiply(A, B):
    n = A.shape[0]
    A_tensor, B_tensor = A[:, :, np.newaxis], B[:, :, np.newaxis]
    C = np.zeros((n, n))
    axes = [('+z', 1), ('-z', -1), ('+y', 1), ('-y', -1), ('+x', 1), ('-x', -1)]

    # Each GOU computes one or more elements of C
    contributions = {(i, j): 0 for i in range(n) for j in range(n)}
    for axis, dir_ in axes:
        A_rot = rotate_tensor(A_tensor, axis[1], dir_)
        B_rot = rotate_tensor(B_tensor, axis[1], dir_)
        for i in range(n):
            for j in range(n):
                sum_ = 0
                for k in range(n):
                    sum_ += A_rot[i, k, 0] * B_rot[k, j, 0]
                contributions[(i, j)] += sum_

    for (i, j), value in contributions.items():
        C[i, j] = value / len(axes)  # Normalize since each term appears multiple times
    return C

# Example usage
if __name__ == "__main__":
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    C = rrc_multiply(A, B)
    print("Computed C:")
    print(C)
