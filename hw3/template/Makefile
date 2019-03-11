TEX_SOURCES = $(shell find . -name "*.tex")
BIB_SOURCES = $(shell find . -name "*.bib")

default: leong_lambert_final.pdf

leong_lambert_final.pdf: $(TEX_SOURCES) $(BIB_SOURCES)
	pdflatex final
	bibtex final
	pdflatex final
	pdflatex final
	@echo "leong_lambert_final.pdf file generated"

clean:
	/bin/rm -f *.aux *.log *.toc  *.blg *.bbl *.lof *.lot
	touch final.tex

