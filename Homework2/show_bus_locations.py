__author__ = 'jgrundy'

import sys
import urllib2
import json

url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel' \
      '=calls&LineRef=%s' % (sys.argv[1],sys.argv[2])
webUrl = urllib2.urlopen(url)
data = json.loads(webUrl.read())
parsedData = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]["VehicleActivity"]

print "Bus line:", sys.argv[2]
print "Number of active vehicles:", len(parsedData)

busNumber = 0

for x in parsedData:
    busNumber = busNumber + 1
    latitude = x['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude = x['MonitoredVehicleJourney']['VehicleLocation']['Longitude']

    print "Bus %s is at latitude %s and longitude %s" %(busNumber, latitude, longitude)