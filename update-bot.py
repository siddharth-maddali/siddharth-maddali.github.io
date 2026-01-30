#!/home/siddharth/venv/bin/python
#
#
#
import twitter
import subprocess
import re
from bs4 import BeautifulSoup
def getPermalinkSubstring( mystr ): 
    link_substrings = mystr.split( '/' )[-1].replace( '.md', '' ).split( '-' )
    search_string = '/'.join( 
        [ 
            '/'.join( link_substrings[:3] ),
            '-'.join( link_substrings[3:] )
        ]
    )
    return search_string
def getTweetContent( xmlobj, pl_substr ):
    entry = [ 
        [ this[ 'title' ], this[ 'description' ], this[ 'link' ] ] 
        for this in xmlobj[ 'rss' ][ 'channel' ][ 'item' ] 
        if pl_substr in this[ 'link' ] 
    ][0]
    entry[1] = cleanUpDescription( entry[1] )
    return tuple( entry )
def cleanUpDescription( entry ):
    excerpt = entry.split( '\n' )[-1].strip( '<p>' ).strip( '</p>' )
    soup = BeautifulSoup( excerpt )
    for this in soup.body.find_all( name='a' ):
        excerpt = excerpt.replace( 
            '<a name="%s">%s</a>'%( this.attrs[ 'name' ], this.text ), 
            this.attrs[ 'name' ].replace( '#', '@' )
        )
    return excerpt
def extractTags( mdfile ):
    with open( mdfile ) as mdf:
        for line in mdf:
            if re.match( 'tags: ', line ):
                break
    tags = [ 
        hashtag[1:] if '\\@' in hashtag else '#%s'%( hashtag.replace( ' ', '' ) ) 
        for hashtag in line.split( ': ' )[-1].strip().strip( '[' ).strip( ']' ).split( ', ' )
    ] 
    return tags
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
    tokens = []
    return mybot
if __name__=="__main__":
    import sys
    import xmltodict
    import re
    import datetime
    rss = '/home/smaddali/local/siddharth-maddali.github.io/_site/feed.xml' 
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
