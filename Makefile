ROOT=${HOME}/local/siddharth-maddali.github.io
BOT=${ROOT}/update-bot.py
ZIP=/usr/bin/zip
DOCCREAT=${ROOT}/createDocs.py
POSTS=$(wildcard ${ROOT}/tweet-record/*.md)
TWEETS=$(POSTS:.md=.tweet)
ARCHIVE=${ROOT}/tweet-record/tweet-archive.zip
BLOG_POSTS=$(wildcard ${ROOT}/_posts/*.md)
WORDCLOUD_IMG=${ROOT}/images/blog/wordcloud.png
WORDCLOUD_SCRIPT=${ROOT}/generate_wordcloud.py
WEB=$(wildcard ${ROOT}/docs/{cv,resume}/*.tex)
PDF=$(WEB:.tex=.pdf)
DOCLIST=${ROOT}/docs/docs.list
DOCCREATFLAGS=
%.tweet: %.md
	$(BOT) $< $@
$(ARCHIVE):$(TWEETS)
	$(ZIP) -rv $(ARCHIVE) $(TWEETS)
$(WORDCLOUD_IMG): $(BLOG_POSTS)
	python3 $(WORDCLOUD_SCRIPT)
%.pdf: %.html
	-$(H2P) $(H2PFLAGS) $< $@
	@cp $@ ./professional/
$(DOCLIST):$(PDF)
	@echo $(PDF) > $(DOCLIST)
.PHONY: updatelinks tweet touch clean docs test wordcloud notify
updatelinks:
	diff $(ROOT)/_posts/ $(ROOT)/tweet-record/ \
		| grep "^Only in $(ROOT)/_posts" \
		| awk '{ print $$(4); }' \
		| xargs -I '{}' ln -s $(ROOT)/_posts/{} -t $(ROOT)/tweet-record/
wordcloud: $(WORDCLOUD_IMG)
tweet: wordcloud $(ARCHIVE)
touch: 
	@echo WARNING: Resetting timestamps of all existing posts...
	ls $(ROOT)/tweet-record/*.tweet \
		| sed "s/\.tweet//g" \
		| xargs -I '{}' basename {} \
		| xargs -I '{}' bash -c "\
			unlink $(ROOT)/tweet-record/{}.md && \
			ln -s $(ROOT)/_posts/{}.md -t $(ROOT)/tweet-record && \
			touch $(ROOT)/tweet-record/{}.tweet"
	touch $(ARCHIVE)
clean: 
	rm -f $(ROOT)/tweet-record/*.tweet $(ARCHIVE)
	ls $(ROOT)/tweet-record/*.md | xargs -I '{}' unlink {}
docs: $(DOCLIST) 
notify:
	python3 $(ROOT)/notify_crawlers.py