---
layout: post
mathjax: true
author: Siddharth Maddali
categories: [Programming]
tags: [twitterbot, twitterdev, twitterapi, makefile, jekyll]
---

{% include mathjax.html %}
How to auto-tweet about Jekyll blog updates using a combination of the <a style="text-decoration:none; color:#333;" name="#TwitterDev">Twitter</a> API and some clever shell programming.

# Because I'm lazy...
## ...but I still want the attention.
For a while I've been trying to increase the exposure of my currently very young blog through Twitter with a well thought-out combination of hashtags and Twitter handles, but without actually being bothered to tweet about it separately.
Because of this, I've been interested in playing with [Twitter's API for developers](https://developer.twitter.com/en) to automate this relatively mundane task (in my view). 
After a couple of weekends of aggressive Googling and playing around without actually committing to learning something new, I've arrived at the reasonable solution that is the content of this post, that I'm proud to count among my "little programming victories". 

For context, my blog is a [static website](https://github.com/siddharth-maddali/siddharth-maddali.github.io) hosted on Github Pages, which I generate using [Jekyll](https://jekyllrb.com/).
I maintain the source code on my personal Linux laptop running Ubuntu.
To do what I want to do, I basically (i) scan my website directory tree for new/updated blog posts (Markdown files) using a [makefile](https://www.gnu.org/software/make/), (ii) extract the tags and excerpts from these posts, and (iii) tweet the text of the excerpts, modifed to include a link to the post itself, hashtags generated from the post tags, and the handles of the Twitterati whose attention I want to get.
This post is basically an overview of how I do this, with links to the source code for anyone who's interested in going deeper.

# Setting up Twitter scripting
To automate tasks on Twitter, you first have to apply for a developer account.
It will be at least a few days before they approve your application, in which you have to provide justification. 
Mine seemed to be delayed a little longer than usual due to COVID-19 -related understaffing.

Once you have your developer account, you will have to create an app for your purposes (I called mine `update-bot`). 
You will be assigned 4 tokens: an access token, an access secret, an API key and an API secret.
These will be displayed only once on your online Twitter developer dashboard when you first create the app, so note them down in a safe place.
I chose to store these tokens in [pass](https://www.passwordstore.org/), which is a popular password manager with Unix/Linux users.
My tokens are arranged in the following tree, under `siddarthious` since I plan to auto-tweet through my [@SidDarthious](https://twitter.com/SidDarthious/) account: 
<br/>
<img src="{{ site.url }}/images/blog/pass-branch.png" width="100%" style="display:block; margin-left:auto; margin-right:auto">
<br/>

In my update script (which I describe later), I log in as @SidDarthious by copying these tokens directly into the clipboard and supplying them to the Twitter interface to login each time. 
I use the [Python Twitter module](https://github.com/sixohsix/twitter) for this task.

# The makefile and the update script

The makefile I use can be found [here](https://github.com/siddharth-maddali/siddharth-maddali.github.io/blob/master/Makefile). 
After I `git push` the new website changes to Github Pages, the makefile checks for new blog posts based on the status of the corresponding `.tweet` files (one per `.md` file), searches [the blog's RSS feed](https://siddharth-maddali.github.io/feed.xml) for the [permalinks](https://jekyllrb.com/docs/permalinks/) of the new posts, and then calls my [`update-bot.py`](https://github.com/siddharth-maddali/siddharth-maddali.github.io/blob/master/update-bot.py) script to work on each of the new posts (which ends in a new tweet on my timeline for each new post).
It is in `update-bot.py` that I extract my login tokens and programmatically manipulate my Twitter timeline.

There is a potentially disastrous gotcha here, which comes from the fact that Jekyll on Github Pages takes around 20 seconds (sometimes longer) to rebuild my website each time I push changes.
In this time, I would have to hold off the makefile from running, in case it ends up parsing the remote RSS feed that hasn't been updated yet (in which case it wouldn't find the required permalinks, and it would definitely complain). 
To avoid this, I get the makefile to instead parse the _locally generated_ RSS feed in my local `_site` directory, into which Jekyll dumps my entire static website.
By doing this, I can obtain the updated permalinks I need, except that I need to manually tweak them with a simple search-and-replace string operation.
By this I mean, if a new blog post has the following permalink on my _local_ Jekyll server:

	localhost:4000/mathematics/2020/03/15/Breaking-down-the-Fourier-transform.html

then it's a simple matter to change it to:

	https://siddharth-maddali.github.io/mathematics/2020/03/15/Breaking-down-the-Fourier-transform.html

which would be the correct weblink for the online version.
This would prevent my makefile from getting confused by making the auto-tweeting and site-building tasks independent of each other. 

# An example
As an example of the combined Python-makefile combo, shown below is the raw Markdown header of [an earlier blog post of mine](https://siddharth-maddali.github.io/mathematics/2020/05/18/an-operator-based-justification-of-the-heisenberg-uncertainty-principle.html):
<br/>
<img src="{{ site.url }}/images/blog/example-post.png" width="100%" style="display:block; margin-left:auto; margin-right:auto">
<br/>

...which when found and parsed by my Makefile, resulted in this tweet appearing a short while later on my Twitter timeline: 
<blockquote class="twitter-tweet" data-theme="dark"><p lang="ro" dir="ltr">Blog update: An operator-based proof of Heisenberg’s uncertainty principle: σₓ² σₖ² ≥ 1/4 <a href="https://t.co/J2fQQYjo9Z">https://t.co/J2fQQYjo9Z</a> <a href="https://twitter.com/hashtag/linearalgebra?src=hash&amp;ref_src=twsrc%5Etfw">#linearalgebra</a> <a href="https://twitter.com/hashtag/quantummechanics?src=hash&amp;ref_src=twsrc%5Etfw">#quantummechanics</a> <a href="https://twitter.com/hashtag/signalprocessing?src=hash&amp;ref_src=twsrc%5Etfw">#signalprocessing</a> <a href="https://twitter.com/hashtag/Heisenberg?src=hash&amp;ref_src=twsrc%5Etfw">#Heisenberg</a> <a href="https://twitter.com/hashtag/uncertainty?src=hash&amp;ref_src=twsrc%5Etfw">#uncertainty</a> <a href="https://twitter.com/hashtag/Fouriertransform?src=hash&amp;ref_src=twsrc%5Etfw">#Fouriertransform</a></p>&mdash; Siddharth Maddali (@SidDarthious) <a href="https://twitter.com/SidDarthious/status/1262650770417205248?ref_src=twsrc%5Etfw">May 19, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Notice how the tags in the Markdown header have been automatically parsed by `update-bot.py` to generate the hashtags you see in the tweet. 
Of course, by arranging things this way, the only real worry is when somebody tries to open the link in the tweet in the few seconds before Github Pages regenerates my website, and ends up with a [404 page](https://en.wikipedia.org/wiki/HTTP_404).
Since I'm far from popular enough for this kind of traffic on my Twitter timeline, I have decided to defer worrying about this for later!

## Auto-tagging 
Another feature I want was for my `update-bot` to be be smart enough to replace the names of any people mentioned in the post excerpt (for example, scientific collaborators, or anyone else I would want to tag) with their Twitter handles (prefixed with a `@`) in the final tweet. 
This took a little thought, because I would want the Twitter handle to appear in its right place in the tweet, but not the original blog post excerpt.
For example, if you look back at the excerpt at the beginning of this post, it is rendered online in exactly the way I would like: 

<br/>
<img src="{{ site.url }}/images/blog/excerpt-example.png" width="80%" style="border: 2px solid black; display:block; margin-left:auto; margin-right:auto">
<br/>

But in the subsequent _tweet_, I would like the word "Twitter" to be replaced with `@TwitterDev`.
So the "@TwitterDev" handle must be somehow introduced into the excerpt as metadata, and must substitute the word "Twitter" when generating the text of the tweet.
The way I chose to implement this was with HTML anchors in the Markdown file which Markdown knows to ignore, but nevertheless can be extracted programatically.
And so here is the Markdown source of the excerpt of this post:
<br/>
<img src="{{ site.url }}/images/blog/excerpt-source.png" width="100%" style="display:block; margin-left:auto; margin-right:auto">
<br/>
Notice how the substring that I want replaced in the tweet ("Twitter"), is stored as the text of an HTML anchor (`<a ...>Twitter</a>`), and the anchor name itself is the eventual Twitter handle (after substituting `#` with `@`). 
The extra style formatting for the anchor is to camouflage it to look like the surrounding text and not a hyperlink (the default behavior as defined in my `main.css` file).
A string like this is easily parsed using Python's [`BeautifulSoup`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) module, and the Twitter handle can be extracted with relatively little effort.
Take a look at the `cleanUpDescription` function in the [`update-bot.py`](https://github.com/siddharth-maddali/siddharth-maddali.github.io/blob/master/update-bot.py) script to see how I did it.

Surely enough, the tweet announcing this blog post is nearly identical to the post excerpt, but has the `@TwitterDev` handle exactly where I want it: 
<blockquote class="twitter-tweet" data-theme="dark"><p lang="en" dir="ltr">Blog update: How to auto-tweet about Jekyll blog updates using a combination of the <a href="https://twitter.com/TwitterDev?ref_src=twsrc%5Etfw">@TwitterDev</a> API and some clever shell programming. <a href="https://t.co/y8xEzZbwFo">https://t.co/y8xEzZbwFo</a> <a href="https://twitter.com/hashtag/twitterbot?src=hash&amp;ref_src=twsrc%5Etfw">#twitterbot</a> <a href="https://twitter.com/hashtag/twitterdev?src=hash&amp;ref_src=twsrc%5Etfw">#twitterdev</a> <a href="https://twitter.com/hashtag/twitterapi?src=hash&amp;ref_src=twsrc%5Etfw">#twitterapi</a> <a href="https://twitter.com/hashtag/makefile?src=hash&amp;ref_src=twsrc%5Etfw">#makefile</a> <a href="https://twitter.com/hashtag/jekyll?src=hash&amp;ref_src=twsrc%5Etfw">#jekyll</a></p>&mdash; Siddharth Maddali (@SidDarthious) <a href="https://twitter.com/SidDarthious/status/1264828558255497216?ref_src=twsrc%5Etfw">May 25, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

# Conclusion
An interesting thing I noticed is that my Twitter developer app, `update-bot`, gets an honorable mention whenever the tweets are viewed on a phone and a desktop browser (but not in the embedded tweet above):
<br/>
<img src="{{ site.url }}/images/blog/example-post-phone.png" width="300" style="display:block; margin-left:auto; margin-right:auto">
<br/>
This, of course, different from my local `update-bot.py` described above (which is a single Python script).

The last thing left to truly automate the tweeting of new posts is to invoke the makefile in a cron job. 
This would leave me to focus exclusively on generating new content, while the bot I created faithfully and instantaneously notifies all of Twitter!
I wrote the Bash script [`update-site.sh`](https://github.com/siddharth-maddali/siddharth-maddali.github.io/blob/master/update-site.sh) for this purpose, which is invoked once a week. 
I can now sit back while my home server dutifully does my social networking for me!

I have been thinking about increasing my content exposure even more by also auto-posting on LinkedIN. 
For this I would have to teach myself the essentials of the [REST API](https://developer.linkedin.com/docs/rest-api). 
This is a project for another time, so stay tuned!

## EDIT
I had first implemented the auto-tagging idea not with HTML anchors but comments. 
My reasoning back then was that comments are also ignored in Markdown rendering and can be parsed programatically. 
Unfortunately, I discovered that the Jekyll engine that generates my static web pages misbehaves with this particular trick, and the pages end up being garbled in a way that I don't know how to debug.
So as of now, the solution with anchors works, and that is how I'll do it from now on!

