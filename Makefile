#########################################################
# 
# Makefile to tweet blog updates based on new entries in  
# the _posts directory.
# Account: @SidDarthious
# Archive: tweet-record/tweet-archive.zip
# 
# 	Siddharth Maddali
# 	siddharth.mv@protonmail.com
# 	May 2020
# 
#########################################################

ROOT=${HOME}/local/siddharth-maddali.github.io
BOT=${ROOT}/update-bot.py
ZIP=/usr/bin/zip
H2P=/usr/bin/wkhtmltopdf

# auto-tweeting variables
POSTS=$(wildcard ${ROOT}/tweet-record/*.md)
TWEETS=$(POSTS:.md=.tweet)
ARCHIVE=${ROOT}/tweet-record/tweet-archive.zip

# html to pdf
WEB=$(wildcard ${ROOT}/docs/*.html)
PDF=$(WEB:.html=.pdf)
DOCLIST=${ROOT}/docs/docs.list
H2PFLAGS=--page-size tabloid

#########################################################
# Make directives
#########################################################

#--------------------------------------------------------------

# creates a new <filename>.tweet for every <filename>.md
%.tweet: %.md
	$(BOT) $< $@

# archives all <filename>.tweet into existing archive.
$(ARCHIVE):$(TWEETS)
	$(ZIP) -rv $(ARCHIVE) $(TWEETS)

#--------------------------------------------------------------

# builds pdfs from html pages in docs directory
%.pdf: %.html
	$(H2P) $(H2PFLAGS) $< $@

# generates list of pdfs as text file.
$(DOCLIST):$(PDF)
	@echo $(PDF) > $(DOCLIST)

#--------------------------------------------------------------

.PHONY: updatelinks tweet touch clean docs

# updatelinks: 
#	creates symlinks of all new blog posts 
#	within the staging directory.
updatelinks:
	diff $(ROOT)/_posts/ $(ROOT)/tweet-record/ |\
		grep "^Only in $(ROOT)/_posts" |\
		awk '{ print $$(4); }' |\
		xargs -I '{}' ln -s $(ROOT)/_posts/{} -t $(ROOT)/tweet-record/

# tweet: 
# 	build the target i.e., local copy of tweets, and eventually the archive.
tweet: $(ARCHIVE)

# touch: 
# 	Fast-forwards status of all blog posts as tweeted, regardless 
# 	of whether post has been updated or not. Used to avoid tweeting 
# 	same blog post multiple times after an edit.
touch: 
	@echo WARNING: Resetting timestamps of all existing posts...
	ls $(ROOT)/tweet-record/*.tweet |\
		sed "s/\.tweet//g" |\
		xargs -I '{}' basename {} |\
		xargs -I '{}' bash -c "\
			unlink $(ROOT)/tweet-record/{}.md && \
			ln -s $(ROOT)/_posts/{}.md -t $(ROOT)/tweet-record && \
			touch $(ROOT)/tweet-record/{}.tweet"
	touch $(ARCHIVE)

# clean: 
# 	Flushes everything away removes record of auto-tweeted posts.
# 	WARNING: Doing this and then running 'make updatelinks' followed 
# 	by 'make tweet' will auto-tweet EVERY POST since the beginning!
clean: 
	rm -f $(ROOT)/tweet-record/*.tweet $(ARCHIVE)
	ls $(ROOT)/tweet-record/*.md | xargs -I '{}' unlink {}

# docs: 
# 	Rebuilds pdf documents
docs: $(DOCLIST) 

