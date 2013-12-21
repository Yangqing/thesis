name=thesis

SOURCES = $(wildcard **/*.tex)

all: thesis.pdf

thesis.pdf: $(SOURCES) *.bib Makefile
	pdflatex $(name)
	bibtex $(name)
	pdflatex $(name)
	pdflatex $(name)

cleanall: clean
	-@rm -f $(name).pdf

clean:
	-@rm -f *.pdf *.aux *.bbl *.blg *.lof *.log *.lot *.xml *.toc $(name)-blx.bib
