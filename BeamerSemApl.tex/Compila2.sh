/usr/local/texlive/2012/bin/i386-linux/pdflatex BeamerSemApl.tex
/usr/local/texlive/2012/bin/i386-linux/pdflatex BeamerSemApl.tex
for f in bu*.aux; do 
  /usr/local/texlive/2012/bin/i386-linux/bibtex $f
done
/usr/local/texlive/2012/bin/i386-linux/pdflatex BeamerSemApl.tex
/usr/local/texlive/2012/bin/i386-linux/pdflatex BeamerSemApl.tex
/usr/local/texlive/2012/bin/i386-linux/pdflatex BeamerSemApl.tex
okular BeamerSemApl.pdf &