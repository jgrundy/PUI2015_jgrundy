import sys
import json
import datetime
import urllib2

if __name__=='__main__':
    for dataID in sys.argv[1:]:
        url = 'https://nycopendata.socrata.com/views/%s/' % (dataID)#sets up so that can grab a specific file with a python terminal command
        request = urllib2.urlopen(url) #query for the url from the website using urllib2 package
        metadata = json.loads(request.read()) #load the information
        #print metadata.keys()
        print dataID, datetime.datetime.fromtimestamp(metadata['createdAt'])
    
