#!/usr/bin/bash

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
	echo "Pausing for 5 sec before requesting Google crawl..."
	sleep 5
	curl $CRAWL?sitemap=https://$SITE/sitemap.xml
	echo
}

updatePosts
pushChanges "$1"
autoTweet
requestCrawl

