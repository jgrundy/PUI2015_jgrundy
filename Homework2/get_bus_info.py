__author__ = 'jgrundy'

import sys
import urllib2
import json
import csv

url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel' \
      '=calls&LineRef=%s' % (sys.argv[1],sys.argv[2])
webUrl = urllib2.urlopen(url)
data = json.loads(webUrl.read())
parsedData = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]["VehicleActivity"]


with open(sys.argv[3], 'wb') as outputCSV:
    writer = csv.writer(outputCSV)
    headers = ['Latitude', 'Longitude', 'Stop Name', 'Stop Status']
    writer.writerow(headers)

    for x in parsedData:
        latitude = x['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        longitude = x['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        stopName = x['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
        stopStatus = x['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']

        writer.writerow([latitude, longitude, stopName, stopStatus])