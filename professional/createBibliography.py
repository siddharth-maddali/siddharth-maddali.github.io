#!/home/smaddali/anaconda3/bin/python

def getSortedKeys( bib ):
    keys = list( dict( bib.entries ).keys() )
    years = [ key.split( '_' )[-1] for key in keys ]
    sortidx = argsort( years )
    return [ keys[idx] for idx in sortidx ][::-1]

def argsort( seq ):
    return sorted( range( len( seq ) ), key=seq.__getitem__ )

def getAuthorString( pub ):
    authlist = [ str( auth ) for auth in dict( pub.persons )[ 'author' ] ]
    authlist = [ ' '.join( auth.split( ', ' )[::-1] ) for auth in authlist ]
    authlist = [ '<b>'+auth+'</b>' if 'Maddali' in auth else auth for auth in authlist ]
    authlist[-2] = ' and '.join( authlist[-2:] )
    return ', '.join( authlist[:-1] ) 

def getCitation( thispub ):
    authorstring = getAuthorString( thispub )
    title = '<em>'+thispub.fields[ 'title' ]+'</em>'
    if thispub.type in [ 'inpreparation', 'submitted' ]:
        if thispub.type=='inpreparation':
            status_string = '(In preparation)'
        else: 
            status_string = '(Submitted)'
        return ', '.join( [ authorstring, title+' <b><em>'+status_string+'</em></b></div>&nbsp;&nbsp;&nbsp;' ] )
    try: 
        journal = '<b><em>'+thispub.fields[ 'journal' ]+'</em></b>'
    except: 
        try: 
            journal = '<b><em>'+thispub.fields[ 'archiveprefix' ]+'</em></b>'
        except: 
            raise NameError( 'Either journal or archive prefix should be specified. ' )
    try: 
        when = ' '.join( [ thispub.fields[ st ] for st in [ 'month', 'year' ] ] )
    except: 
        when = '' # month and/or year information missing, e.g., for Inpreparation
    when += '</div>&nbsp;&nbsp;&nbsp;'
    citation = ', '.join( [ st for st in [ authorstring, title, journal, when ] if len( st ) > 0 ] )
    return citation

def getPreprintBadge( thispub ):
    if 'preprinturl' not in thispub.fields.keys(): 
        return '' 
    else: 
        preprinturl = thispub.fields[ 'preprinturl' ]
        parts = preprinturl.split( '/' )
        number = parts[-1]
        server = parts[-3].replace( '.org', '' ) # it's usually arxiv
        ppstr = '%s:%s'%( server, number )
        outstr = '<div style="display: inline-block">'
        outstr += '<a href="%s" rel="noopener noreferrer" target="_blank">'%preprinturl
        outstr += '<img src="https://img.shields.io/badge/preprint-%s-green.svg"></a>'%ppstr
        outstr += '</div>&nbsp;&nbsp;&nbsp;'
        return outstr

def getDOIAltmetricBadge( thispub ):
    if 'doi' not in thispub.fields.keys(): 
        return '', '' 
    else: 
        doiurl = thispub.fields[ 'doi' ]
        if 'doi.org' not in doiurl: 
            doiurl = 'https://doi.org/' + doiurl
        parts = doiurl.split( '/' )
        doi = '/'.join( parts[-2:] )
        
        doistr = '<div style="display: inline-block">'
        doistr += '<a href="%s" rel="noopener noreferrer" target="_blank">'%doiurl
        doistr += '<img src="https://img.shields.io/badge/DOI-%s-1292FC.svg"></a>'%( doi.replace( '-', '_' ) )
        doistr += '</div>&nbsp;&nbsp;&nbsp;'

        altstr =  '<div style="display: inline-block" data-badge-popover="right" '
        altstr += 'class="altmetric-embed" data-badge-type="1" data-doi="'
        altstr += doi
        altstr += '" data-condensed="true"></div><br/>'

        return doistr, altstr

if __name__=='__main__':

    import argparse
    from pybtex.database import parse_file as parsebibfile
    
    parser = argparse.ArgumentParser()
    parser.add_argument( '-b', '--bibtexfile', help='Input .bib file', type=str )
    parser.add_argument( '-s', '--fontsize', type=float, default=1.2, help='Font size' )
    args = parser.parse_args()
    
    startstr = '<div style="white-space: wrap">'
    startstr += '<div style="font-size: %.1fem; display: inline-block">'%args.fontsize
    stopstr = '</div></div>'

    #print( args.bibtexfile )
    bibdata = parsebibfile( args.bibtexfile )
    keys_sorted = getSortedKeys( bibdata )
    npub = len( keys_sorted )
    for n, key in enumerate( keys_sorted ):
        thispub = bibdata.entries[ key ]
        citation = getCitation( thispub )
        preprintbadge = getPreprintBadge( thispub )
        doibadge, altmetricbadge = getDOIAltmetricBadge( thispub )
        prestr = startstr + '[<a id="cit-%s" href="#call-%s">%d</a>] '%( key, key, npub-n )
        fullstr = prestr + citation + doibadge + preprintbadge + altmetricbadge #+ stopstr
        print( fullstr, '\n' )

