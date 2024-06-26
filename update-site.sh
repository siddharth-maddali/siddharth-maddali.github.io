#!/bin/bash

###############################################################
#
# 	Script to automatically update website content along with 
# 	auto-tweeting about new/updated blog posts. Ideally, this 
# 	should be a cron job on a server, not manually run on a laptop.
#
#	Siddharth Maddali
#	siddharth.mv@protonmail.com
#	May 2020
#
###############################################################

PSRC=$HOME/local
SITE=siddharth-maddali.github.io
ROOT=$PSRC/$SITE
CRAWL=http://www.google.com/ping
PROF=$PSRC/$SITE/professional
LUALATEX=$ROOT/latexBuild_lua.sh

function updateResumeCV() {
	# cd $PROF
	# bash ./createCV.sh
	cd $ROOT/docs/resume
	$LUALATEX resume
	cd $ROOT/docs/cv
	$LUALATEX cv
}

## DEPRECATED
# function updateDocs() { 
# 	JEKYLL_SERVERS=$( netstat -tupln 2>/dev/null | grep "jekyll serve" | wc -l )
# 	if [[ "$JEKYLL_SERVERS" -lt "1" ]]; then # no Jekyll servers running. 
# 		RED='\033[0;31m'
# 		NC='\033[0m' # No Color
# 		echo -e ${RED}updateDocs ERROR: Jekyll server not running${NC}; Faulty docs build. 
# 		echo -e Serve Jekyll site locally with: ${RED} $ bundle exec jekyll serve${NC} and then build docs. 
# 	else
# 		cd $ROOT
# 		echo "Building docs..."
# 		make docs
# 	fi
# }

function updatePosts() {
	cd $ROOT/_drafts
	#ls *.md | xargs -I '{}' echo $( date +%F )-{}
	ls *.md | xargs -I '{}' mv {} ../_posts/$( date +%F )-{}
}

function pushChanges() {
	cd $ROOT
	git add .
	git commit -m "$1"
	git push
}
function autoTweet() {
	cd $ROOT
	make updatelinks
	make tweet
}

function requestCrawl() {
#	echo "Pausing for 5 sec before requesting Google crawl..."
#	sleep 5
	curl $CRAWL?sitemap=https://$SITE/sitemap.xml
	echo
}

updateResumeCV
#updateDocs
updatePosts
pushChanges "$1"
autoTweet
requestCrawl

