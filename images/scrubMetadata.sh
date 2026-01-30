#!/bin/bash
#
#
if [ $
	echo "Usage: ./scrubMetadata.sh <image_filename> <current_year>"
	exit 1
fi
SCRUBBER=$( which exiftool )
$SCRUBBER -overwrite_original_in_place\
	-Make=""\
	-Model=""\
	-DateTimeOriginal=""\
	-DateCreated=""\
	-GPSAltitudeRef=""\
	-GPSLatitude=""\
	-GPSLatitudeRef=""\
	-GPSLongitude=""\
	-GPSLongitudeRef=""\
	-GPSDateStamp=""\
	-GPSTimeStamp=""\
	-TimeCreated=""\
	-Orientation=""\
	-Software=""\
	-ModifyDate=""\
	-Comment=""\
	-rights="©$2 Siddharth Maddali, all rights reserved"\
	-CopyrightNotice="©$2 Siddharth Maddali, all rights reserved"\
	 $1
