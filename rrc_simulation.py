import numpy as np

def R_index(i, j, k, n, axis, dir_):
    """Rotate index (i, j, k) in n×n×1 space around axis with direction ±1."""
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

def precompute_rotation_maps(n):
    """Precompute index mappings for all rotations."""
    axes = [('z', 1), ('z', -1), ('y', 1), ('y', -1), ('x', 1), ('x', -1)]
    maps = {}
    for axis, dir_ in axes:
        map_key = (axis, dir_)
        maps[map_key] = np.zeros((n, n, 3), dtype=int)
        for i in range(n):
            for j in range(n):
                i_, j_, k_ = R_index(i, j, 0, n, axis, dir_)
                maps[map_key][i, j] = [i_, j_, k_]
    return maps

def balanced_rrc_multiply(A, B):
    """RRC matrix multiplication with proper contribution summation."""
    if A.shape != B.shape or len(A.shape) != 2 or A.shape[0] != 4:
        raise ValueError("A and B must be 4×4 square matrices.")

    n = 4
    C = np.zeros((n, n))
    maps = precompute_rotation_maps(n)
    axes = [('z', 1), ('z', -1), ('y', 1), ('y', -1), ('x', 1), ('x', -1)]
    row_pairs = [(0, 3), (1, 2)]
    processed_triples = set()

    for axis, dir_ in axes:
        idx_map = maps[(axis, dir_)]
        for r1, r2 in row_pairs:
            for k in range(n):
                for j in range(n):
                    if (r1, k, j) in processed_triples:
                        continue
                    i_A, j_A, _ = idx_map[r1, k]
                    if 0 <= i_A < n:
                        C[r1, j] += A[r1, k] * B[k, j]
                        processed_triples.add((r1, k, j))
                        if r1 != r2 and (r2, k, j) not in processed_triples:
                            i_A2, j_A2, _ = idx_map[r2, k]
                            if 0 <= i_A2 < n:
                                C[r2, j] += A[r2, k] * B[k, j]
                                processed_triples.add((r2, k, j))

    return C

# TEST BLOCK
if __name__ == "__main__":
    A = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]], dtype=float)
    B = np.array([[16, 15, 14, 13],
                  [12, 11, 10, 9],
                  [8, 7, 6, 5],
                  [4, 3, 2, 1]], dtype=float)

    print("A:\n", A)
    print("B:\n", B)

    C_rrc = balanced_rrc_multiply(A, B)
    C_np = np.matmul(A, B)

    print("\nBalanced RRC Result:\n", C_rrc)
    print("\nNumPy Result:\n", C_np)
    print("\nDifference:\n", C_rrc - C_np)
    print("\nParity:", np.allclose(C_rrc, C_np, atol=1e-5))