import csv
import json
import sys

if __name__=='__main__':
    jsonFile = open(sys.argv[1], 'r')
    data = json.load(jsonFile)
    stations = data['stationBeanList']

    with open(sys.argv[2], 'wb') as csvFile:
        writer = csv.writer(csvFile)
        headers = ['Station Name', 'Latitude', 'Longitude']
        writer.writerow(headers)
        
        for s in stations:
            if s['statusKey']!=1 and s['stationName'].startswith('Coming soon'):
                stationName = s['stationName'][13:]
                stationLat  = s['latitude']
                stationLon  = s['longitude']

                writer.writerow([stationName, stationLat, stationLon])
                #print '% 30s : %s,%s' % (stationName, stationLat, stationLon)
