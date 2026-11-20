FIGURES = character-line critical-plane theta-plane windows units-modulo-four principal-extension prime-ramp strip oscillation kernel path lift balance
VECTOR_PDFS = $(addprefix figures/,$(addsuffix .pdf,$(FIGURES)))
LATEX_FLAGS = -interaction=nonstopmode -halt-on-error -file-line-error

# Freeze PDF metadata across repeated builds with the same TeX distribution.
export SOURCE_DATE_EPOCH = 1795190400
export FORCE_SOURCE_DATE = 1

.PHONY: all figures data
all: companion.pdf
figures: $(VECTOR_PDFS) figures/residue-classes.pdf
data:
	python3 figures/figure_data.py

companion.pdf: companion.tex $(VECTOR_PDFS)
	latexmk -g -pdf $(LATEX_FLAGS) companion.tex

figures/%.pdf: figures/%.tex figures/style.tex
	cd figures && pdflatex $(LATEX_FLAGS) $*.tex

figures/prime-ramp.pdf: figures/prime-ramp.dat
figures/kernel.pdf: figures/kernel.dat
