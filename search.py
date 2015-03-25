__author__ = 'CC'

import urllib, json

api_key = 'AIzaSyDMaf8g5AnI_OI7jR3ck5VVR2tf8LWmhQg'
query = 'blue bottle'
service_url = 'https://www.googleapis.com/freebase/v1/search'
params = {
        'query': query,
        'key': api_key
}
url = service_url + '?' + urllib.urlencode(params)
response = json.loads(urllib.urlopen(url).read())
for result in response['result']:
    print result['name'] + ' (' + str(result['score']) + ')'