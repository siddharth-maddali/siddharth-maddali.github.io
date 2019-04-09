#/home/siddharth/venv/bin/python3

import bibtexparser as bibparse


with open( 'pubs.md', 'w' ) as pubspage:
    # header
    pubspage.write( '---\n' )
    pubspage.write( 'layout: cv\n' )
    pubspage.write( 'title: My curriculum vitae\n' )
    pubspage.write( '---\n\n# Publications\n\n' )

    with open( 'publication.bib' ) as bibfile:
        data = bibparse.load( bibfile ).entries_dict

        for key in data.keys():
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
                    pubspage.write( '[%s, %s](%s)\n'%( 
                            data[ key ][ 'journal' ], 
                            data[ key ][ 'year' ], 
                            data[ key ][ 'url' ]
                        )
                    )
                elif 'arxiv.org' in data[ key ][ 'url' ]:   # an arxiv preprint
                    pubspage.write( 'ArXiv: [%s](%s) %s\n'%( 
                            data[ key ][ 'eprint' ], 
                            data[ key ][ 'url' ], 
                            data[ key ][ 'note' ]
                        )
                    )
            else: # no URL information available
                pubspage.write( '%s\n'%data[ key ][ 'note' ] )

            pubspage.write( '\n' )
