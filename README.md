# Understanding the proposed proof of Dirichlet GRH

This repository is a playground for exploring Levent Alpöge’s proposed proof of the generalized Riemann hypothesis for Dirichlet L-functions. We use it to work through the arguments, trace individual steps in the released Lean source, and record what we can verify.

Codex wrote the four-page sketch as an independent exposition. [Read the four-page sketch (PDF)](proof-sketch.pdf) · [TeX source](proof-sketch.tex)

A zero to the right of the critical line would force a weighted prime sum to exceed a threshold somewhere in every sufficiently late interval of the form $[Y,Y^{3/2}]$. The proposed theta-lift construction is meant to produce arbitrarily late intervals on which the sum stays at or below that threshold throughout. The sketch works through this contradiction and identifies the uniform estimates the construction needs. Those estimates and the full Lean build remain unverified in this exposition.

The PDF links individual mathematical steps to the released source. [Alpöge’s announcement](https://alpo.ge/remark.pdf) · [Lean source at the revision used for the sketch](https://github.com/TomasOrtega/RH/tree/a6ac91a412dcbaab31801355ec5707024a71bf65/extracted/lean)

## Build the PDF

The published copy was typeset with pdfLaTeX from TeX Live 2026. A full TeX Live installation includes `latexmk` and the required packages, including the New PX, Source Sans and Inconsolata fonts. From the repository root, run

```sh
latexmk -g -interaction=nonstopmode -halt-on-error
```

The repository’s `.latexmkrc` selects pdfLaTeX and `proof-sketch.tex`. The command writes `proof-sketch.pdf` in the same directory. The source is self-contained and can be built offline with the TeX packages installed.
