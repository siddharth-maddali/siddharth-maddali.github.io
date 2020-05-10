#########################################################
# 
# Makefile to tweet blog updates based on new entries in  
# the _posts directory.
# Account: @SidDarthious
# Archive: tweet-record/tweet-archive.zip
# 
# 	Siddharth Maddali
# 	smaddali@alumni.cmu.edu
# 	May 2020
# 
#########################################################

ROOT=/extra/siddharth-maddali.github.io
BOT=${ROOT}/scripts/update-bot.py
ZIP=/usr/bin/zip

POSTS=$(wildcard ${ROOT}/tweet-record/*.md)
TWEETS=$(POSTS:.md=.tweet)

ARCHIVE=${ROOT}/tweet-record/tweet-archive.zip

#########################################################
# Make directives
#########################################################


# creates a new <filename>.tweet for every <filename>.md
%.tweet: %.md
	$(BOT) $< $@

# archives all <filename>.tweet into existing archive.
$(ARCHIVE):$(TWEETS)
	$(ZIP) -rv $(ARCHIVE) $(TWEETS)

.PHONY: updatelinks tweet clean
updatelinks:
	diff $(ROOT)/_posts/ $(ROOT)/tweet-record/ |\
		grep "^Only in [[:alnum:][:punct:]]\{,\}/_posts" |\
		awk '{ print $$(4); }' |\
		xargs -I '{}' ln -s $(ROOT)/_posts/{} -t $(ROOT)/tweet-record/

# build the target i.e., local copy of tweets
tweet: $(ARCHIVE)

# awk inputs need to be escaped with an extra $
clean: 
	rm -f $(TWEETS) $(ARCHIVE)
	ls $(POSTS) | xargs -I '{}' unlink {}
