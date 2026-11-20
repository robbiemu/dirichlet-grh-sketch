# Understanding the proposed proof of Dirichlet GRH

This repository is a playground for exploring Levent Alpöge’s proposed proof of the generalized Riemann hypothesis for Dirichlet L-functions. We use it to work through the arguments, trace individual steps in the released Lean source, and record what we can verify.

Codex wrote these notes as an independent exposition.

- **The proof sketch** explains why a zero to the right of the critical line would force a weighted prime sum above a threshold in every sufficiently late interval $[Y,Y^{3/2}]$, and how Alpöge proposes to construct arbitrarily late intervals on which the sum stays below that threshold. [Four-page sketch (PDF)](proof-sketch.pdf) · [TeX source](proof-sketch.tex)
- **A prime sum and its zeros** starts with the character table modulo four and works through the argument for readers new to analytic number theory, automorphic forms or Lean. Eight figures accompany the derivations, from the first prime sum to the local divisibility calculation and the final window estimate. [Illustrated companion (PDF)](companion/companion.pdf) · [TeX, figures and data](companion/)
- **The lift estimate** follows the valuations through a chain of theta lifts, identifies the common fractional ideal by which the periods can be divided, and works out the four error terms that lead to $H_\psi(x) \le x^{1/2+9\varepsilon}$. [Worked lift estimate (PDF)](lift-estimate.pdf) · [TeX source](lift-estimate.tex)

Alpöge claims an unconditional proof. Here we reconstruct the valuation induction, the cancellations and the exponent calculation from the specified inputs. Independent verification of the automorphic period identities and norm bounds, their simultaneous realization on whole windows, and the full Lean build remains open in this playground. The notes link individual steps to the source. [Alpöge’s announcement](https://alpo.ge/remark.pdf) · [Lean source at the revision used for the notes](https://github.com/TomasOrtega/RH/tree/a6ac91a412dcbaab31801355ec5707024a71bf65/extracted/lean)

## Build the PDFs

The published PDFs were typeset with pdfLaTeX from TeX Live 2026. A full TeX Live installation includes `latexmk` and the required packages, including the New PX, Source Sans and Inconsolata fonts. From the repository root, run

```sh
latexmk -g -interaction=nonstopmode -halt-on-error
```

The repository’s `.latexmkrc` selects pdfLaTeX for the two short notes. The command writes `proof-sketch.pdf` and `lift-estimate.pdf` in the same directory. Both sources are self-contained and can be built offline with the TeX packages installed. The illustrated companion has its own [instructions for rebuilding the figures, data and PDF](companion/README.md#rebuild).
