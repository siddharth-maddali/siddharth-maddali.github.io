---
layout: post
mathjax: true
author: Siddharth Maddali
categories: [Programming]
tags: [twitterbot, twitterdev, twitterapi, makefile, jekyll]
---

{% include mathjax.html %}
<a name="exex"></a>
How to auto-tweet about Jekyll blog updates using a combination of the <!--id="TwitterDev"-->Twitter<!--/id--> API and some clever shell programming.

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
I chose to store these tokens in [pass](https://www.passwordstore.org/), which is a popular password manager for Unix/Linux users.
My tokens are arranged in the following tree, under `siddarthious` since I plan to auto-tweet through my [@SidDarthious](https://twitter.com/SidDarthious/) account: 
<br/>
<img src="{{ site.url }}/images/blog/pass-branch.png" style="display:block; margin-left:auto; margin-right:auto">
<br/>

In my update script (which I describe later), I log in as @SidDarthious by copying these tokens directly into the clipboard and supplying them to the Twitter interface to login each time. 
I use the [Python Twitter module](https://github.com/sixohsix/twitter) by the Twitter devs in my update script.

# The makefile and the update script

The makefile I use can be found [here](https://github.com/siddharth-maddali/siddharth-maddali.github.io/blob/master/Makefile). 
After I `git push` the new website changes to Github Pages, the makefile checks for new blog posts based on the status of the corresponding `.tweet` files (one per `.md` file), searches [the blog's RSS feed](https://siddharth-maddali.github.io/feed.xml) for the [permalinks](https://jekyllrb.com/docs/permalinks/) of the new posts, and then calls my [`update-bot.py`](https://github.com/siddharth-maddali/siddharth-maddali.github.io/blob/master/update-bot.py) script to work on each of the new posts.
It is in `update-bot.py` that I extract my login tokens and programmatically manipulate my Twitter timeline.

There is a potentially disastrous gotcha here, which comes from the fact that Jekyll on Github Pages takes around 20 seconds (sometimes longer) to rebuild my website each time I push changes.
In this time, I would have to hold off the makefile from running, in case it ends up parsing the remote RSS feed that hasn't been updated yet (in which case it wouldn't find the required permalinks, and it would definitely complain). 
To avoid this, I get the makefile to instead parse the _locally generated_ RSS feed in my local `_site` directory, into which Jekyll dumps my entire static website.
By doing this, I can obtain the updated permalinks I need, except that I only need to manually tweak the link with a simple search-and-replace string operation.
For example, if a new blog post has the following permalink on my _local_ Jekyll server:

	localhost:4000/mathematics/2020/03/15/Breaking-down-the-Fourier-transform.html

then it's a simple matter to change it to:

	https://siddharth-maddali.github.io/mathematics/2020/03/15/Breaking-down-the-Fourier-transform.html

which would be the correct weblink for the online version.
This would prevent my makefile from getting confused by making the auto-tweeting and site-building tasks independent of each other. 

# An example
As an example of the combined Python-makefile combo, shown below is the raw Markdown header of [an earlier blog post of mine](https://siddharth-maddali.github.io/mathematics/2020/05/18/an-operator-based-justification-of-the-heisenberg-uncertainty-principle.html):
<br/>
<img src="{{ site.url }}/images/blog/example-post.png" style="display:block; margin-left:auto; margin-right:auto">
<br/>

...which when found and parsed by my Makefile, resulted in this tweet appearing a short while later on my Twitter timeline: 
<blockquote class="twitter-tweet" data-theme="dark"><p lang="ro" dir="ltr">Blog update: An operator-based proof of Heisenberg’s uncertainty principle: σₓ² σₖ² ≥ 1/4 <a href="https://t.co/J2fQQYjo9Z">https://t.co/J2fQQYjo9Z</a> <a href="https://twitter.com/hashtag/linearalgebra?src=hash&amp;ref_src=twsrc%5Etfw">#linearalgebra</a> <a href="https://twitter.com/hashtag/quantummechanics?src=hash&amp;ref_src=twsrc%5Etfw">#quantummechanics</a> <a href="https://twitter.com/hashtag/signalprocessing?src=hash&amp;ref_src=twsrc%5Etfw">#signalprocessing</a> <a href="https://twitter.com/hashtag/Heisenberg?src=hash&amp;ref_src=twsrc%5Etfw">#Heisenberg</a> <a href="https://twitter.com/hashtag/uncertainty?src=hash&amp;ref_src=twsrc%5Etfw">#uncertainty</a> <a href="https://twitter.com/hashtag/Fouriertransform?src=hash&amp;ref_src=twsrc%5Etfw">#Fouriertransform</a></p>&mdash; Siddharth Maddali (@SidDarthious) <a href="https://twitter.com/SidDarthious/status/1262650770417205248?ref_src=twsrc%5Etfw">May 19, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Notice how the tags in the Markdown header have been automatically parsed by `update-bot.py` to generate the hashtags you see in the tweet. 
Of course, by arranging things this way, the only thing I _would_ need to worry about is somebody trying to open the link in the tweet in the few seconds before Github Pages regenerates my website.
Since I'm far from getting this kind of traffic on my timeline, I'll defer worrying about this for later!

## Auto-tagging 
Another feature I wanted was for my `update-bot` to be be smart enough to replace the names of any people mentioned in the post excerpt (for example, scientific collaborators, or anyone else I would want to tag) with their Twitter handles (prefixed with a `@`) in the final tweet. 
This took a little thought, because I would want the Twitter handle to appear in its right place in the tweet, but not the original blog post excerpt.
For example, if you look back at [the excerpt for this post](#exex), it is rendered online in exactly the way I would like: 

<br/>
<img src="{{ site.url }}/images/blog/excerpt-example.png" width="800" style="display:block; margin-left:auto; margin-right:auto">
<br/>

But in the subsequent _tweet_, I would like the word "Twitter" to be replaced with `@TwitterDev`.
So the "TwitterDev" handle must be somehow introduced into the excerpt as metadata, and must substitute the word "Twitter" in the final tweet.
The way I chose to implement this was with HTML comments in the Markdown file which Markdown knows to ignore, but nevertheless can be extracted programatically.
The best example of this is seen in the Markdown source of this post itself: 
<br/>
<img src="{{ site.url }}/images/blog/excerpt-source.png" width="800" style="display:block; margin-left:auto; margin-right:auto">
<br/>
Notice how the substring that I want replaced in the tweet, is sandwiched between the HTML comments `<!--id="TwitterDev"-->` and `<!--/id-->`. 
The first of these contains the Twitter handle I want to put in eventually (`@TwitterDev`). 
If you're interested in getting into the details of how I did this in a generalized manner (multiple tags), you can take a look at the `cleanUpDescription` function in the [`update-bot.py`](https://github.com/siddharth-maddali/siddharth-maddali.github.io/blob/master/update-bot.py) script.
Sure enough, the tweet announcing this blog post had the `@TwitterDev` handle in the right place: 
<blockquote class="twitter-tweet" data-theme="dark"><p lang="en" dir="ltr">Blog update: How to auto-tweet about Jekyll blog updates using a combination of the <a href="https://twitter.com/TwitterDev?ref_src=twsrc%5Etfw">@TwitterDev</a> API and some clever shell programming. <a href="https://t.co/y8xEzZbwFo">https://t.co/y8xEzZbwFo</a> <a href="https://twitter.com/hashtag/twitterbot?src=hash&amp;ref_src=twsrc%5Etfw">#twitterbot</a> <a href="https://twitter.com/hashtag/twitterdev?src=hash&amp;ref_src=twsrc%5Etfw">#twitterdev</a> <a href="https://twitter.com/hashtag/twitterapi?src=hash&amp;ref_src=twsrc%5Etfw">#twitterapi</a> <a href="https://twitter.com/hashtag/makefile?src=hash&amp;ref_src=twsrc%5Etfw">#makefile</a> <a href="https://twitter.com/hashtag/jekyll?src=hash&amp;ref_src=twsrc%5Etfw">#jekyll</a></p>&mdash; Siddharth Maddali (@SidDarthious) <a href="https://twitter.com/SidDarthious/status/1264828558255497216?ref_src=twsrc%5Etfw">May 25, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Finally, I also noticed is that the Twitter developer app I created, `update-bot`, gets an honorable mention whenever the tweets is viewed in the phone app:
<br/>
<img src="{{ site.url }}/images/blog/example-post-phone.png" width="300" style="display:block; margin-left:auto; margin-right:auto">
<br/>
This, of course, refers to the `update-bot` app I created that's visible on the Twitter dev dashboard, and not the same as my local `update-bot.py` described above (which is a single Python script).

# Conclusion
The last thing left to be done to truly automate the tweeting of new posts is to put the makefile in a cron job and run it periodically. 
This would leave me to focus exclusively on generating new content, while the bot I created faithfully notifies all my friends on Twitter!
I wrote the Bash script [`update-site.sh`](https://github.com/siddharth-maddali/siddharth-maddali.github.io/blob/master/update-site.sh) for this purpose, simply add this script (with the correct pah modifications) to your crontab, and you can stop worrying about tweeting manually about your blog posts!
