#!/home/siddharth/venv/bin/python

#########################################################################
#
# Script to automate tweeting of blog update notifications to
# the timeline of @SidDarthious. Uses GNU Make to create 
# formatted tweets of new blog/updated posts, which include title, 
# URL, excerpt and hashtags.
#
#   Siddharth Maddali
#   May 2020
#
#########################################################################

import twitter      # for auto-tweeting
import subprocess   # to access pass through python

# Get a searchable string for the blog post permalink
def getPermalinkSubstring( mystr ): 
    link_substrings = mystr.split( '/' )[-1].replace( '.md', '' ).split( '-' )
    search_string = '/'.join( 
        [ 
            '/'.join( link_substrings[:3] ),
            '-'.join( link_substrings[3:] )

        ]
    )
    return search_string

# Given a searchable string, mine the xml object for the 
# post title, excerpt and permalink that will go into the 
# final tweet.
def getTweetContent( xmlobj, pl_substr ):
    entry = [ 
        [ this[ 'title' ], this[ 'description' ], this[ 'link' ] ] 
        for this in xmlobj[ 'rss' ][ 'channel' ][ 'item' ] 
        if pl_substr in this[ 'link' ] 
    ][0]
    entry[1] = cleanUpDescription( entry[1] )
    return tuple( entry )

# Extracts blog excerpt from description, which contains 
# other HTML tags like <script>
def cleanUpDescription( entry ):
    excerpt = entry.split( '\n' )[-1].strip( '<p>' ).strip( '</p>' )
    return excerpt

# Extracts tags from the input markdown file, and perses 
# them as hashtags to be tweeted.
def extractTags( mdfile ):
    with open( mdfile ) as mdf:
        for line in mdf:
            if re.match( 'tags: ', line ):
                break
    tags = [ 
        hashtag[1:] if '\\@' in hashtag else '#%s'%( hashtag.replace( ' ', '' ) ) 
        for hashtag in line.split( ': ' )[-1].strip().strip( '[' ).strip( ']' ).split( ', ' )
    ] 
        # Jekyll doesn't like blog tags beginning with @, which I want to use to tag 
        # people on Twitter, so I need to prefix each with \@ and then teach this script 
        # to ignore the leading \
        # TODO: create new HTML element to use in future .md files, that reads something like this: 
        # ... in collaboration with <twitter-person id="ComixLab">the COMIX lab</twitter-person> in Marseille...
        # This script should be able to extract "ComixLab" and replace the above instance with:
        # ... in collaboration with @ComixLab in Marseille...
        # in the final tweet. This is a much better way of tagging people.
    return tags

# Creates the update bot and authenticates.
def getAuthenticatedBot(
        root='social/twitter/siddarthious/update-bot', 
        labels=[ 'access-token', 'access-token-secret', 'api-key', 'api-secret-key' ]
    ):
    tokens = [ 
        subprocess.Popen( 
            [ 'pass', '%s/%s'%( root, thislabel ) ], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT
        ).communicate()[0].strip().decode( 'utf-8' )
        for thislabel in labels
    ]
    mybot = twitter.Twitter( 
        auth=twitter.OAuth( 
            token=tokens[0],
            token_secret=tokens[1],
            consumer_key=tokens[2], 
            consumer_secret=tokens[3]
        ) 
    )
    tokens = [] # flushing all tokens
    return mybot



if __name__=="__main__":
    import sys          # command line args
    import xmltodict    # to parse rss feed
    import re           # searching for tags
    import datetime     # for logging and makefile tracking purposes

    rss = '/extra/siddharth-maddali.github.io/_site/feed.xml' 
    root = 'https://siddharth-maddali.github.io'
    fakeroot = 'http://localhost:4000/'

    mdfile  = sys.argv[1]
    logfile = sys.argv[2]

    tags = extractTags( mdfile )

    with open( rss ) as fid:
        feed = xmltodict.parse( fid.read() )
   
    pl_substr = getPermalinkSubstring( mdfile )

    title, desc, link = getTweetContent( feed, pl_substr )
    link = link.replace( fakeroot, root )

    tweet = 'Blog update: %s \n%s \n%s '%( 
        desc, 
        link, 
        ' '.join( tags )
    )

    timestamp = datetime.datetime.now().strftime( '%Y-%m-%d, %H:%M:%S' )
    with open( logfile, 'a' ) as lf:
        lf.write( 'Tweeted on: %s\n'%timestamp )
        lf.write( tweet )
        lf.write( '\n' )

    bot = getAuthenticatedBot()
    bot.statuses.update( status=tweet )
