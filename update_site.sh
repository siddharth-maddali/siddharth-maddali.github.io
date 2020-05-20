#!/bin/bash

# Script to automatically update website content along with auto-tweeting about new/updated blog posts
# Ideally, this should be a cron job on a server, not manually run on a laptop.

ROOT=/extra/siddharth-maddali.github.io
TWEETS=$ROOT/scripts
SLEEP=2m	

function pushChanges() {
	cd $ROOT
	git add .
	git commit -m "$1"
	git push
}
function autoTweet() {
	cd $TWEETS
	make updatelinks
	make tweet
}

pushChanges "$1"
sleep $SLEEP
autoTweet

