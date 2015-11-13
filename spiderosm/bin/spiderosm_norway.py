#!/usr/bin/env python

from spiderosm import osm

import sys                   # fixme usage
import os

root = 'test_data/input/norway/'
elveg_filename = os.path.join(root, 'highway-finstad-elveg-small.osm') #sys.argv[1]
osm_filename = os.path.join(root, 'highway-finstad-osm-small.osm') #sys.argv[2]
elveg = osm.OSMData(file_name=elveg_filename, xml_format=True)
osm   = osm.OSMData(file_name=osm_filename, xml_format=True)
#osm   = osm.OSMData()           # overpass

elveg_nwk = elveg.create_path_network('elveg')
osm_nwk = osm.create_path_network('osm')

# try to decrease max_d: 
# for nwk in (elveg_nwk, osm_nwk):
#     nwk.street_scale = 0.1

#osm_nwk.match(elveg_nwk)
elveg_nwk.match(osm_nwk)#, d=0.1)

elveg_nwk.match_stats()
osm_nwk.match_stats()

elveg_nwk.write_geojson(os.path.join('data', 'elveg'))
osm_nwk.write_geojson(os.path.join('data', 'osm'))
