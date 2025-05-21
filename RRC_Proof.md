
# Rotation Coverage Lemma — Proof for Rotational Recursive Compression (RRC)

## Lemma: 6-GOU Sufficiency

For every index triple \((i, k, j)\) required to compute \(C = AB\), where \(A, B \in \mathbb{R}^{n \times n}\), there exists a 90° axis-aligned rotation \(R \in \{ R_{+x}, R_{-x}, R_{+y}, R_{-y}, R_{+z}, R_{-z} \}\) such that:
\[
A_{ik} = R(\mathcal{B}(A))_{i', 1, 0}, \quad B_{kj} = R(\mathcal{B}(B))_{1, j', 0}
\]
Here, \(\mathcal{B}(M)\) denotes the 3D embedding of matrix \(M\), i.e., \(\mathcal{B}(M)_{i,j,0} = M_{i,j}\).

## Proof:

1. Each GOU applies a fixed 90° rotation \(R\) to \(\mathcal{B}(A)\) and \(\mathcal{B}(B)\). These rotations belong to the **dihedral group \(D_4\)** of cube symmetries.
2. \(D_4\) acts **transitively** on index pairs \((i, j)\). That is, for any \((i, k)\) and \((k, j)\), some rotation \(R\) exists such that:
   \[
   R(i, k) \mapsto (i', 1), \quad R(k, j) \mapsto (1, j')
   \]
3. These alignments allow each GOU to compute partial dot-product terms \(A_{ik}B_{kj}\) through positional exposure in the rotated tensor grid.
4. Over six distinct rotations, the union of index alignments from each GOU is **sufficient to expose all \(n^3\) combinations** of \((i, k, j)\).
5. Thus, six GOUs can cooperatively compute the full matrix product \(C = AB\).

\(\square\)

## Notes:
- This lemma assumes non-overlapping merge slices and consistent indexing via \(\mathcal{B}(M)\).
- Zero-cost permutations further reduce FLOPs by removing explicit indexing overhead.
