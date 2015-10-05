import sys
import json
import datetime

if __name__=='__main__':
    jsonFile = open(sys.argv[1], 'r') #sets up so that can grab a specific file with a python terminal command
    metadata = json.load(jsonFile)
    print metadata.keys()
    print datetime.datetime.fromtimestamp(metdata['createdAt'])
