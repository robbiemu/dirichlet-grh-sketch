# A prime sum and its zeros

[Read the illustrated companion (PDF)](companion.pdf) · [Read the TeX source](companion.tex) · [Four-page sketch](https://github.com/robbiemu/dirichlet-grh-sketch/blob/67229c2f8412210e319691c1e4b45fde81027a0d/proof-sketch.pdf) · [Worked lift estimate](https://github.com/robbiemu/dirichlet-grh-sketch/blob/67229c2f8412210e319691c1e4b45fde81027a0d/lift-estimate.pdf)

This companion to Levent Alpöge’s proposed proof of Dirichlet GRH assumes calculus, linear algebra and familiarity with finite groups. It begins by reading a character from a number line, using its weights in a series and locating the critical strip in the complex plane. Along the way readers compute a conductor from a character table, follow a prime in the Gaussian integers, extract a weight by integration and restrict a cohomology class to a subgroup.

The analytic chapters derive how a hypothetical zero forces a large value of a smoothed prime sum on each sufficiently late window. The arithmetic chapters trace the valuation gained at each theta lift, the fractional ideal that divides the periods and the four error terms that give the conditional exponent $1/2+9\varepsilon$. The closing pages explain which estimates must hold together on whole windows and how to inspect the final Lean declarations. The companion checks the displayed reductions and examples. The uniform arithmetic construction and full Lean build remain unverified here.

## Figures

The figures are separate vector PDFs. Each has a standalone TeX source in the same directory. The numerical plots include their data and a standard-library Python generator.

| Figure | What it shows | Reproducible source |
| --- | --- | --- |
| [Character weights on the number line](figures/character-line.pdf) | Period four and the weights of two products | [Diagram](figures/character-line.tex) |
| [Where a zero could lie](figures/critical-plane.pdf) | The critical strip, its middle line and two sample inputs | [Diagram](figures/critical-plane.tex) |
| [Symmetries in the upper half-plane](figures/theta-plane.pdf) | A shift by two preserves the theta value and inversion takes the input to a different point | [Diagram](figures/theta-plane.tex) |
| [Two window claims](figures/windows.pdf) | The arithmetic window bound and the prediction from a zero on the same interval | [Diagram](figures/windows.tex) |
| [Residue classes](figures/residue-classes.pdf) | Sorting odd primes through 13 modulo four gives a signed difference of two minus three | [Diagram](figures/residue-classes.tex) |
| [Units modulo four](figures/units-modulo-four.pdf) | Multiplication gives an inverse for each of the classes 1 and 3 | [Diagram](figures/units-modulo-four.tex) |
| [Prime ramps](figures/prime-ramp.pdf) | Prime-power sums for the character that gives every integer weight 1 | [Plot](figures/prime-ramp.tex) · [Data](figures/prime-ramp.dat) |
| [Critical strip](figures/strip.pdf) | A hypothetical reflected pair and a test exponent | [Diagram](figures/strip.tex) |
| [Model oscillation](figures/oscillation.pdf) | A two-pole function with an exactly known threshold crossing | [Plot](figures/oscillation.tex) |
| [Localization kernel](figures/kernel.pdf) | The derivative weight at two window sizes | [Plot](figures/kernel.tex) · [Data](figures/kernel.dat) |
| [Finite-field path](figures/path.pdf) | All eight supported triples in the example over the field of five elements | [Diagram and table](figures/path.tex) |
| [Theta-lift chain](figures/lift.pdf) | The groups, forms and direction of integration | [Diagram](figures/lift.tex) |
| [Chain length](figures/balance.pdf) | The exponents of the two competing quantities as the length varies | [Plot](figures/balance.tex) |

## Rebuild

With a full TeX Live installation, Make and Python 3, run these commands from this directory. They regenerate both data tables, all thirteen figure PDFs and the companion, including internal page references.

```sh
make data
make -B all
```

To typeset just the text against the checked-in figures, run `latexmk -pdf -interaction=nonstopmode -halt-on-error companion.tex` here. The original build used pdfLaTeX from TeX Live 2026. The [Makefile](Makefile) fixes the PDF metadata date. The [numerical generator](figures/figure_data.py) computes the ramps directly and evaluates the kernel relative to its peak using logarithms.

## Source edition

The companion uses the announcement and accompanying Lean archive released on 20 November 2026. Its Lean links point to the extracted-source mirror at revision `a6ac91a412dcbaab31801355ec5707024a71bf65`. The archive pins Lean `v4.33.1` and mathlib `0df444a360eaa60ab8c11dca51a86af692955474`. [Alpöge’s announcement](https://alpo.ge/remark.pdf) · [Pinned Lean source](https://github.com/TomasOrtega/RH/tree/a6ac91a412dcbaab31801355ec5707024a71bf65/extracted/lean)

| Local source read | SHA-256 |
| --- | --- |
| Announcement PDF | `3fc97784b71ddd44ff8aa0a177e99622a1c61b13cfa843a0989ee4a7a0cfeb8d` |
| Reassembled Lean archive | `9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc` |
