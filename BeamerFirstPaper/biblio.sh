for f in bu*.aux; do
  bibtex $f
done
bibtex BeamerFirstPaper.aux