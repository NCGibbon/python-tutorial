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
# if within 0.5 miles, show on google map
def find_northbound():
    from xml.etree.ElementTree import parse
    doc = parse('rt22.xml')
    check_time = doc.findtext('time')
    for bus in doc.findall('bus'):
        d = bus.findtext('d')
        id = bus.findtext('id')
        lat = float(bus.findtext('lat'))
        lon = bus.findtext('lon')
        if d == 'North Bound':
            dist = distance(lat, office_lat)
            print ('time = ', check_time)
            print ('id = ', id)
            # print ('lat = ', lat)
            # print ('lon = ', lon)
            print ('dist = ', dist)
            if dist <= 0.5:  
                open_map(str(lat), lon, id)

# calculate distance from office to bus
def distance(lat1, lat2):
    return 69 * abs(lat1-lat2)

# open google map in web browser and show bus and office on map
def open_map(lat, lon, id):
    import webbrowser
    key = 'AIzaSyDe1fq7oib8shkDokkXzJ8H1txRTLjR8k8'
    office_location = '&markers=color:blue%7Clabel:O%7C' + str(office_lat) + ',' + str(office_lon)
    bus_location = '&markers=color:red%7Clabel:B%7C' + lat + ',' + lon
    url = 'http://maps.googleapis.com/maps/api/staticmap?size=400x400&maptype=roadmap' \
            + office_location + bus_location + '&key=' + key
    webbrowser.open(url)

# check the buses every minute
def keep_checking(minutes):
    import time
    for bus_checks in range(minutes):
        get_bus_data()
        find_northbound()
        time.sleep(60)

if __name__ == '__main__':
    keep_checking(60) 