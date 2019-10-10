#/home/siddharth/venv/bin/python3

import bibtexparser as bibparse

yearPrefix='20'
fakeName='AAAAAAA' # this should appear first in any sorted list of bibtex keys
realName='Maddali'


def writeMarkdownContent():
    with open( '../_includes/cv/pubs.md', 'w' ) as pubspage:
        with open( 'publication.bib' ) as bibfile:
            data = bibparse.load( bibfile ).entries_dict
            yearD = getYear( data )

            for year in sorted( yearD.keys() )[::-1]: # latest publications first
                pubspage.write( '## **%d**\n'%year )
                
                for bibkey in yearD[ year ]:
                    pubspage.write( '1.\t***%s***\n<br/>'%data[ bibkey ][ 'title' ] )
                    pubspage.write( '\t%s\n<br/>'%getAuthorString( data[ bibkey ][ 'author' ] ) )
                    pubspage.write( '\t%s\n'%getSourceWithLink( data[ bibkey ] ) )
                pubspage.write( '\n\n' )
    return

##########################################################################################

def getSourceWithLink( bibentry ):
    if 'eprint' in bibentry.keys():
        srcstr = '%s: <a href="%s">%s</a>'%( 
            bibentry[ 'eprinttype' ], 
            bibentry[ 'file' ].replace(
                'online:', '' ).replace( 
                ':PDF', '' ).replace( 
                '\\', '' ),
            bibentry[ 'eprint' ]
        )
    elif 'journal' in bibentry.keys():
        try:    # look for url
            srcstr = '<a href="%s">%s</a>'%( bibentry[ 'url' ], bibentry[ 'journal' ] )
        except: # no url, look for DOI
            doistr = bibentry[ 'doi' ].split( 'doi.org/' )[-1]
            srcstr = '<a href="https://doi.org/%s">%s</a>'%( doistr, bibentry[ 'journal' ] )
    else:
        srcstr = '%s'%bibentry[ 'comment' ]
    return srcstr

##########################################################################################

def getAuthorString( authString ):
    rightWay = ', '.join( 
        [ ' '.join( auth.strip().split( ', ' )[::-1] ) for auth in authString.split( ' and ' ) ]
    ).replace( 
        'S. Maddali', '**S. Maddali**' 
    ).replace( 
        'Siddharth Maddali', '**Siddharth Maddali**'
    )
    return rightWay



##########################################################################################

def getYear( data ):
    D = {}
    for key in data.keys():
        if 'year' in data[ key ].keys():
            try:
                D[ int( data[ key ][ 'year' ] ) ].append( key )
            except KeyError:
                D[ int( data[ key ][ 'year' ] ) ] = [ key ]
        else:
            try:
                D[ int( data[ key ][ 'date' ].split( '-' )[0] ) ].append( key )
            except KeyError:
                D[ int( data[ key ][ 'date' ].split( '-' )[0] ) ] = [ key ]

        for year in D.keys():
            D[ year ] = [ # ensures that publications with desired first author are displayed first
                bibcitekey.replace( fakeName, realName ) for bibcitekey in
                sorted( [ 
                    oldkey.replace( realName, fakeName ) for oldkey in D[ year ]
                ] )
            ]

    return D

##########################################################################################

if __name__=="__main__":
    print( 'Generating publications page...' )
    writeMarkdownContent()
    print( 'Success!' )





        
