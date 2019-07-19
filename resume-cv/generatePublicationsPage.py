#/home/siddharth/venv/bin/python3

import bibtexparser as bibparse
import re   # for regular expression parsing


with open( '../_includes/cv/pubs.md', 'w' ) as pubspage:
#    # header
#    pubspage.write( '---\n' )
#    pubspage.write( 'layout: cv\n' )
#    pubspage.write( 'title: Curriculum vitae\n' )
#    pubspage.write( 'mathjax: true\n' )
#    pubspage.write( '---\n{% include mathjax.html %}\n\n' )
#    pubspage.write( '# Publications\n\n' )



    with open( 'publication.bib' ) as bibfile:
        data = bibparse.load( bibfile ).entries_dict
        
        sortKey = []
        for key in data.keys():
            yearkey = 'year' if 'year' in data[ key ].keys() else 'Year'
            sortKey.extend( [ [ int( data[ key ][ yearkey ] ), key ] ] )

        sortKey = list( np.array( sorted( sortKey, key=lambda x:x[0] ) )[::-1] )
            # print publications in reverse chronological order
        thisYear = 'dummy'

        for n in list( range( len( sortKey ) ) ):
            if sortKey[n][0]!= thisYear:
                thisYear = sortKey[n][0]
                pubspage.write( '## **%s**\n\n'%thisYear )

            key = sortKey[n][1]
            print( key )
            pubspage.write( '1.\t_%s_<br/>'%( data[ key ][ 'title' ] ) )
            pubspage.write( '\t%s\n<br/>'%( 
                data[ key ][ 'author' ].replace( ' and', ',' ).\
                        replace( '\\\\textbf{S. Maddali}', '**S. Maddali**' ).\
                        replace( '\\textbf{S. Maddali}', '**S. Maddali**' )
                ) 
            )
                        
            if 'url' in data[ key ].keys(): # published article
                if 'journal' in data[ key ].keys():
                    if data[ key ][ 'journal' ].lower() != 'arxiv e-prints':
                        pubspage.write( '[%s, %s](%s)\n'%( 
                                data[ key ][ 'journal' ], 
                                data[ key ][ yearkey ], 
                                data[ key ][ 'url' ]
                            )
                        )
                    #elif 'arxiv.org' in data[ key ][ 'url' ]:   # an arxiv preprint
                    else:
                        pubspage.write( 'ArXiv: [%s](%s) '%( 
                                data[ key ][ 'eprint' ], 
                                data[ key ][ 'url' ] 
                            )
                        )
            if 'comment' in data[ key ].keys():
                mynote = re.sub( r'\\emph\{(.*)\}', r'_\1_', data[ key ][ 'comment' ].rstrip() )
                    # converts the latex '\emph{<string>}' to markdown '_<string>_'
                pubspage.write( ' %s\n'%mynote )
            else:
                pubspage.write( '\n' )

            pubspage.write( '\n' )
