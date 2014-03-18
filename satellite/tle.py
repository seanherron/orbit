import datetime
import math

from lxml import html
import requests
import requests_cache
import ephem

from . import utilities

requests_cache.install_cache(expire_after=86400)

def get_tle(catnr):
    page = html.fromstring(requests.get('http://www.celestrak.com/cgi-bin/TLE.pl?CATNR=%s' % catnr).text)
    tle = page.xpath('//pre/text()')[0].split('\n')
    return tle[1].strip(), tle[2].strip(), tle[3].strip()
    
def parse_tle(name, line1, line2):
    tle_rec = ephem.readtle(name, line1, line2)
    tle_rec.compute()
    results = {}
    results["name"] = name.strip()
    results["catalog_number"] = line1[2:7]
    results["elsat_classification"] = line1[7]
    results["launch_year"] = utilities.calc_year(line1[9:11])
    results["tle"] = [name, line1, line2]
    results["lat"] = math.degrees(tle_rec.sublat)
    results["long"] = math.degrees(tle_rec.sublong)
    results["elevation"] = tle_rec.elevation
    results["eclipsed"] = tle_rec.eclipsed
    print results
    

def sat_lat(catnr):
    tle = get_tle(catnr)
    parse_tle(tle[0], tle[1], tle[2])
    
sat_lat(25544)