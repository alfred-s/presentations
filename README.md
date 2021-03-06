# presentations
Repo containing presentations I've given + a template.

All presentations can be compiled with the latest texlive-full 
distribution, and the font "cmbright", which can be downloaded
at http://www.ctan.org/pkg/cmbright. Compile using pdflatex.

**presentation_template:**
 * This is a vary basic template for latex presentations, including figures, formulas and tables. 
 * Based on yet another template. 

**fluctuation_dissipation_theorem:**
 * Presentation for termpaper on the *Fluctutation-Dissipation Theorem*.

**functional_microcircuits:**
 * Talk concerning feature specific networks and the changing 
 structure after the onset of visual stimuli, given for
 the seminar *Language and Brain*, January 2016.
 * Contains an algorithm to shrink pdf figures (see `convert.py`).
In order to run `.shrinkpdf.sh`, you have to give it permission:
```
chmod +x shrinkpdf.sh
```
 * The uncompressed figures and final presentations are not
uploaded (way too much data). 

**microcircuit:**
 * Final presentation of the work I've done during my bachelor thesis.

**poster_microcircuit:**
 * Poster about the work I've done during my bachelor thesis.


### General comments:
 * A nice tool for presentations:
pdfpc -- includes infos for the presentation on a second screen:
https://github.com/pdfpc/pdfpc

 * Useful alias for removing latex overhead (which is not 
uploaded anyways): 
```
alias rmlat="rm *.aux *.bbl *.bcf *.blg *.fdb_latexmk *.fls *.log *.nav *.out *.run.xml *.snm *.toc"
```
