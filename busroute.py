"""Find the suitcase on the bus
from the youtube video tutorial:
https://www.youtube.com/watch?v=RrPZza_vZ3w#t=1643
PDF of talk: http://dabeaz.com/pydata/LearnPyData.pdf"""

# the reference location (an office in Chicago)
office_lat = 41.980262
office_lon = -87.668452

# get bus data from the bus tracker api
def get_bus_data():
    import urllib.request as urllib
    u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
    data = u.read()
    f = open('rt22.xml', 'wb')
    f.write(data)
    f.close()

# parse xml and print buses to console
# if a bus is northbound and north of the office
def find_northbound():
    from xml.etree.ElementTree import parse
    doc = parse('rt22.xml')
    for bus in doc.findall('bus'):
        d = bus.findtext('d')
        id = bus.findtext('id')
        lat = float(bus.findtext('lat'))
        if d == 'North Bound':
            if lat > office_lat:
                print ('id = ', id)
                print ('lat = ', lat)
                print ('dir = ', d)
                print (distance(lat, office_lat))

# calculate distance from office to bus
def distance(lat1, lat2):
    return 69 * abs(lat1-lat2)

# check the buses every minute
def keep_checking(minutes):
    import time
    for bus_checks in range(minutes):
        get_bus_data()
        find_northbound()
        time.sleep(60)

if __name__ == '__main__':
    keep_checking(60) 