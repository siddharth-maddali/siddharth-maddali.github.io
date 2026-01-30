#!/bin/bash

PSRC=$HOME/local
SITE=siddharth-maddali.github.io
ROOT=$PSRC/$SITE
PROF=$PSRC/$SITE/professional
LUALATEX=$ROOT/latexBuild_lua.sh

function updateResumeCV() {
	cd $ROOT/docs/resume
	$LUALATEX resume
	cp resume.pdf $ROOT/professional/
	cd $ROOT/docs/cv
	$LUALATEX cv
	cp cv.pdf $ROOT/professional/
}

function updatePosts() {
	cd $ROOT/_drafts
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
	cd $ROOT
	make notify
}

updateResumeCV
updatePosts
pushChanges "$1"
autoTweet
requestCrawl