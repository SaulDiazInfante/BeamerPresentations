/usr/local/texlive/2012/bin/x86_64-linux/pdflatex BeamerSemApl.tex
/usr/local/texlive/2012/bin/x86_64-linux/pdflatex BeamerSemApl.tex
for f in bu*.aux; do 
  /usr/local/texlive/2012/bin/x86_64-linux/bibtex $f
done
/usr/local/texlive/2012/bin/x86_64-linux/bibtex BeamerSemApl.aux
/usr/local/texlive/2012/bin/x86_64-linux/pdflatex BeamerSemApl.tex
/usr/local/texlive/2012/bin/x86_64-linux/pdflatex BeamerSemApl.tex
/usr/local/texlive/2012/bin/x86_64-linux/pdflatex BeamerSemApl.tex