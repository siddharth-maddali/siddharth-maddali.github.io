#!/bin/bash

#######################################################
#
# A simple script to scrub metadata from image files 
# on the website. Also inserts a copyright notice.
#
#######################################################

if [ $# -ne 2 ]; then
	echo "Usage: ./scrubMetadata.sh <image_filename> <current year>"
	exit 1
fi

SCRUBBER=$( which exiftool ) # Install through: sudo apt install libimage-exiftool-perl

$SCRUBBER -overwrite_original_in_place\
	-Make=""\
	-Model=""\
	-DateTimeOriginal=""\
	-DateCreated=""\
	-TimeCreated=""\
	-Orientation=""\
	-Software=""\
	-ModifyDate=""\
	-Comment=""\
	-rights="©$2 Siddharth Maddali, all rights reserved"\
	-CopyrightNotice="©$2 Siddharth Maddali, all rights reserved"\
	 $1	# first argument



