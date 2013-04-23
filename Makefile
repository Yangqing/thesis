name=thesis

all: thesis.pdf

thesis.pdf: *.tex *.bib Makefile
	pdflatex $(name)
	bibtex $(name)
	pdflatex $(name)
	pdflatex $(name)

cleanall: clean
	-@rm -f $(name).pdf

clean:
	-@rm -f *.aux *.bbl *.blg *.lof *.log *.lot *.xml *.toc $(name)-blx.bib
