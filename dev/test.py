import sys
import os
import logging

import lxml.etree

_APP_PATH = \
    os.path.join(os.path.dirname(__file__), '..')

sys.path.insert(0, os.path.abspath(_APP_PATH))

import geonames.config.log
import geonames.compat
import geonames.adapters.search

def _main():
    sa = geonames.adapters.search.Search('dsoprea')
    result = sa.query('detroit').country('us').max_rows(5).execute()
    flat_results = result.get_flat_results()
 
    for (id_, name) in flat_results:
        print(geonames.compat.make_unicode("[{0}]: [{1}]").format(id_, name))

if __name__ == '__main__':
    _main()
