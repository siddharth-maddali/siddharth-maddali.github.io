#!/bin/bash

#---------------- Notebook modifications for CV --------------------------------------
cp CV-original.ipynb CV.ipynb
sed -i "s/# References/# Publications \<a href=\\\\\"https:\/\/scholar\.google\.com\/citations?user=hsYqvQIAAAAJ\&hl=en\&oi=ao\\\\\"\>\<i class=\\\\\"ai ai-google-scholar-square ai\\\\\"\>\<\/i\>\<\/a\>/g" CV.ipynb
sed -i "s/Reeferences/References/g" CV.ipynb
sed -i "/cite{/d" CV.ipynb # removes explicit citations
jupyter nbconvert --to markdown CV.ipynb
cat header.txt CV.md > cv.md
sed -i "s/Maddali, S\./**Maddali, S\.**/g" cv.md
sed -i "s/Maddali S\./**Maddali S\.**/g" cv.md
sed -i "s/Maddali Siddharth/**Maddali Siddharth**/g" cv.md
sed -i "s/S\. Maddali/**S\. Maddali**/g" cv.md
#sed -i "s/\`\`_/ _/g" cv.md		# cleaning up Jupyter latex_env's
#sed -i "s/_'',/_ ,/g" cv.md		# horrible citation formatting

# create corresponding page used for PDF dump
cp cv.md cv_download.md
sed -i "s/layout: portfolio/layout: portfolio_plain/g" cv_download.md
sed -i "s/resume-nav-body\.html/resume-nav-body-plain.html/g" cv_download.md

#---------------- Notebook modifications for resume ----------------------------------
cp Resume-original.ipynb Resume.ipynb
jupyter nbconvert --to markdown Resume.ipynb
cat header-resume.txt Resume.md > resume.md
cp resume.md resume_download.md
sed -i "s/layout: portfolio/layout: portfolio_plain/g" resume_download.md
sed -i "s/resume-nav-body\.html/resume-nav-body-plain.html/g" resume_download.md
