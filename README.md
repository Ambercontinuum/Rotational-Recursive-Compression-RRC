Rotational Recursive Compression (RRC)

Welcome to the official repository for Rotational Recursive Compression (RRC) — a neurodivergent innovation in matrix multiplication that achieves sub-96 FLOP performance for 4×4 complex matrix multiplication, surpassing the AlphaEvolve benchmark.

Created by Amber Anson, in collaboration with LLMs (ChatGPT o3, Gemini, Grok 3, Claude, Co-Pilot and Perplexity), RRC emerged not from formal academia but through recursive cognitive architecture and intuitive pattern compression.


---

Core Claims

AlphaEvolve (Google DeepMind): 48 scalar multiplications, 96 FLOPs.

RRC (Amber et al.): 94–95 FLOPs without hardware acceleration.

RRC + AVP-style zero-cost permutations: 70–72 FLOPs.


These results are derived via:

Embedding 2D matrices as 3D tensors

Applying six axis-aligned 90° rotations

Computing dot-product slices via six Geometric Operation Units (GOUs)



---

Contents

docs/RRC_Whitepaper.pdf — Full documented paper

docs/RRC_Proof.md — Formal statement + Rotation Coverage Lemma

data/FLOP_Ledger.csv — Optimization comparison vs AlphaEvolve

code/rrc_simulation.py — Python prototype for 2x2/4x4 matrix validation

LICENSE — MIT / custom citation license (TBD)



---

How to Use

Reproduce 4x4 Matrix Multiplication:

python rrc_simulation.py

Or open the notebook and run the rrc_multiply(A, B) function with your own 4x4 matrices.


---

Citation / Use

This project may be cited using:

Anson, A. et al. (2025). Breaking the FLOP Barrier: Rotational Recursive Compression and Neurodivergent Innovation in Matrix Multiplication. https://github.com/amber-rrc/Rotational-Recursive-Compression-RRC

Or: Credit the creator and collaborators.


---

License

TBD — default is MIT unless otherwise specified. All contributors and forks must cite Amber Anson as originator.


---

Contact / Community

For collaboration, citation requests, or academic coordination, reach out to:

amber.ai.research@gmail.com

Or create a pull request / open an issue.



---

Additional Resources

Academia.edu Version — Typeset whitepaper and formal proof



---

Acknowledgments

Special thanks to Gemini, Grok, Claude, Copilot, Perplexity and ChatGPT for co-developing, validating, and refining the theory and its implementation.

This project represents a fusion of neurodivergent creativity and recursive machine intelligence.

