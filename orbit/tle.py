import math

from lxml import html
import requests
import requests_cache
import ephem

from . import utilities

requests_cache.install_cache(expire_after=86400)

def get(catnr):
    page = html.fromstring(requests.get('http://www.celestrak.com/NORAD/elements/gp.php?CATNR=%s' % catnr).text)
    tle = page.xpath('//p/text()')[0].split('\n')
    return tle[0].strip(), tle[1].strip(), tle[2].strip()
    
def parse(name, line1, line2):
    tle_rec = ephem.readtle(name, line1, line2)
    tle_rec.compute()
    return tle_rec
