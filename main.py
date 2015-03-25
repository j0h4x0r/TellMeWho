import urllib, json

api_key = 'AIzaSyDMaf8g5AnI_OI7jR3ck5VVR2tf8LWmhQg'
accepted_type_list = ['Person', 'Author', 'Actor']

def main():
    topic(search('tolkien'))


#Infobox Creation

def search(query):
    service_url = 'https://www.googleapis.com/freebase/v1/search'
    params = {
        'query': query,
        'key': api_key}

    url = service_url + '?' + urllib.urlencode(params)

    response = json.loads(urllib.urlopen(url).read())

    result_mid = []

    for result in response['result']:
        result_mid.append(result['mid'])
    return result_mid


def topic(result_mid):
    service_url = 'https://www.googleapis.com/freebase/v1/topic'
    topic_id = result_mid[0]

    params = {
        'key': api_key
    }
    url = service_url + topic_id + '?' + urllib.urlencode(params)
    topic = json.loads(urllib.urlopen(url).read())
    type_list=[]
    for property_list in topic['property']['/type/object/type']['values']:
        type_list.append(property_list['text'])

    return type_list

def valid_topic(type_list, accepted_type_list):
	valid_type_list=[]
	for types in type_list:
		if(types in accepted_type_list):
			valid_type_list.append(types)
	return valid_type_list		
    




#Question Answering







if __name__ == '__main__': main()

