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

ROOT=/extra/siddharth-maddali.github.io

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

updatePosts
pushChanges "$1"
autoTweet

