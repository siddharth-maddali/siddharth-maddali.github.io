#!/home/smaddali/anaconda3//envs/sims/bin/python

# Script to extract citation stats from Google scholar
# 
#  Siddharth Maddali
#  Dec 2023
#

from scholarly import scholarly
import argparse
from pybtex.database import parse_file as parsebibfile

author_name = 'Siddharth Maddali' 
email_domain = '@alumni.cmu.edu'

query = scholarly.search_author( author_name )
try: 
    result = next( query )
    author = scholarly.fill( result )
    while author[ 'email_domain' ] != email_domain: 
        result = next( query )
        author = scholarly.fill( result )
    print( 'Metrics: %d citations, h-index = %d, i10-index = %d'%tuple( 
            author[st] for st in [ 'citedby', 'hindex', 'i10index' ]
        )
    )
except:
    raise StopIteration( 'Author not found on Google Scholar. ' )
