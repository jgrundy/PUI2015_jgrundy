import sys
import json

if __name__=='__main__':
    jsonFile = open(sys.argv[1], 'r') #open the file from system (terminal command)
    data = json.load(jsonFile) #load the information
    stations = data['stationBeanList']
    #print len(stations), stations[0]

for s in stations: #for loop running through the various stations
        if s['statusKey']!=1 and s['stationName'].startswith('Coming soon'):
            stationName =  s['stationName'][13:]
            stationLat = s['latitude']
            stationLon = s['longitude']

            print '% 30s : %s,%s' % (stationName, stationLat, stationLon)
    
