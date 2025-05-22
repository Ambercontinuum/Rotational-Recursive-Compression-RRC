# Rotational Recursive Compression (RRC)

**Author:** Amber Anson  
**License:** AGPLv3 with custom commercial terms  
**Repo:** [github.com/AmberContinuum/Rotational-Recursive-Compression-RRC](https://github.com/AmberContinuum/Rotational-Recursive-Compression-RRC)

---

## Overview

Rotational Recursive Compression (RRC) is a novel approach to matrix multiplication that reimagines computational flow using a recursive, geometry-based framework. Developed through intuition, symbolic modeling, and nontraditional cognition, RRC compresses the matrix multiplication process by leveraging 3D tensor embedding, symmetry-aware logic, and rotational index mapping.

This repository contains the validated implementation of the RRC algorithm that parity-matches NumPy's standard dot product while laying the groundwork for FLOP-optimized extensions.

---

## What's Included

- **`rrc_simulation.py`**  
  A working Python implementation of RRC for `2×2` and `4×4` matrices with comparison output vs. NumPy dot product.
  
- **`RRC_Proof.md`**  
  Step-by-step explanation of the symmetry merge kernel, rotation maps, and contributions.

- **`FLOP_Ledger.csv`**  
  Documentation of theoretical FLOP count by operation category (arithmetic, indexing, merge reuse).

- **`RotationalRecursiveCompression.pdf`**  
  The latest academic whitepaper describing the RRC model, cognitive origin, and theoretical underpinnings.

- **`LICENSE_AGPLv3_AmberAnson.txt`**  
  Open-source license with attribution and equity terms for derivative works.

---

## Core Features

- **Rotation Coverage Lemma**  
  Uses 6 dihedral axis rotations to expose all necessary scalar products across 3D index mappings.

- **Symmetric Partial Sum Reuse**  
  Collapses mirrored contributions to reduce redundant operations in future optimized versions.

- **Recursive Merge Logic**  
  Contributions are indexed via geometric alignment rather than row-by-row traversal.

---

## Getting Started

To test the RRC method:

```bash
python rrc_simulation.py
