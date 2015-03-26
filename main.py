import urllib, json
import matching

api_key = 'AIzaSyDMaf8g5AnI_OI7jR3ck5VVR2tf8LWmhQg'
accepted_type_list = ['Person', 'Author', 'Actor']

def main():
    data, type_list = topic(search('tolkien'))
    infobox(data, type_list)

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
    params = {
        'key': api_key
    }
    for topic_id in result_mid:
        url = service_url + topic_id + '?' + urllib.urlencode(params)
        topic = json.loads(urllib.urlopen(url).read())
        type_list=[]
        for property_list in topic['property']['/type/object/type']['values']:
            type_list.append(property_list['id'].encode("ascii"))
        valid_type_list = valid_topic(type_list, matching.accepted_type_list)
        if len(valid_type_list) is not 0:
            return topic, valid_type_list
    return {}, []

def valid_topic(type_list, accepted_type_list):
    valid_type_list=[]
    for types in type_list:
        if(types in accepted_type_list):
            valid_type_list.append(types)

    return valid_type_list
    
def assemble_infobox(data, typeid_list, information_map):
    result = {}
    for one_type in typeid_list:
        info_dict = information_map[one_type]
        for info_keys, info_values in info_dict:
            # non-nested dict
            if(type(info_values) is str):
                tmp_text=[]
                for text_list in data['property'][info_keys]['values']:
                    tmp_text.append(text_list['text'].encode("ascii"))
                result[info_values] = tmp_text
             # nested dict
            if(type(info_values) is dict):
                # if nested property only has one key, treat it as outer property
            	if(len(info_values['children']) == 1):
                    for nested_key, nested_value in info_values:
                        tmp_text=[]
                        for text_list in data['property'][info_keys]['property'][nested_key]['values']:
                            tmp_text.append(text_list['text'].encode("ascii"))
                        result[nested_value] = tmp_text
                # if nested property only has more than one key, add name as key
                else:
                    result[info_values['name']] = {}
                    for nested_key, nested_value in info_values['children']:
                        tmp_text=[]
                        for text_list in data['property'][nested_key]['values']:
                            tmp_text.append(text_list['text'].encode("ascii"))
                        result['name'][nested_value] = tmp_text


                



def print_infobox(data):
	print data


#Question Answering







if __name__ == '__main__': main()

