#!/usr/bin/bash

cp cv_base.md cv.md
./createBibliography.py -b publication.bib >> cv.md

cp cv.md cv_download.md
sed -i "s/layout: portfolio/layout: portfolio_plain/g" cv_download.md
sed -i "s/resume-nav-body\.html/resume-nav-body-plain.html/g" cv_download.md
echo "Updated CV. "

cp resume.md resume_download.md
sed -i "s/layout: portfolio/layout: portfolio_plain/g" resume_download.md
sed -i "s/resume-nav-body\.html/resume-nav-body-plain.html/g" resume_download.md
echo "Updated resumé. "
