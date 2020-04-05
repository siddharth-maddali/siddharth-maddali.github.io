#!/bin/bash

cp CV-original.ipynb CV.ipynb
sed -i "s/# References/# Publications/g" CV.ipynb
sed -i "/cite{/d" CV.ipynb # removes explicit citations
jupyter nbconvert --to markdown CV.ipynb
cat header.txt CV.md > cv.md
sed -i "s/Maddali, S\./**Maddali, S\.**/g" cv.md
sed -i "s/Maddali S\./**Maddali S\.**/g" cv.md
sed -i "s/Maddali Siddharth/**Maddali Siddharth**/g" cv.md
sed -i "s/S\. Maddali/**S\. Maddali**/g" cv.md

