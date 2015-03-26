__author__ = 'CC'
from collections import defaultdict

total = defaultdict(list)

# Column width
whole=80
one_half=30
one_fourth=12
left_header = 20
colwidth0="{0:<"+str(left_header)+"}"
colwidth1="{0:<"+str(whole)+"}"
colwidth2="{0:<"+str(one_half)+"}"
colwidth3="{0:<"+str(one_fourth)+"}"
# Fake data
attribute=['Front End','Web','Storage']
res_ids=['100','12','200']
nEName=['BALDR','THOR','VALI']
ipList=['192.168.0.5','192.168.0.20','192.168.0.10']

# data = {
#     'Name': [u'Tom Jones'],
#     'Birthday': [u'1940-06-07'],
#     'Description': [   u'Sir Thomas Jones Woodward, OBE, known by his stage name Tom Jones, is a Welsh singer. He became...'],

#     'Place of Birth': [u'Treforest'],
#     'Siblings': [u'Shelia Woodward'],
#     'Spouse(s)': {   'Ceremony Location': [],
#                      'Marriage From': [u'1957-03-02'],
#                      'Marriage To': [],
#                      'Spouse Name': [u'Melinda Trenchard']},
#     'TV Series': {   'Character': [],
#                      'TV Series': [   u'Marge Gets a Job',
#                                       u'Alan Carr and Tom Jones',
#                                       u'Season 2, Episode 15',
#                                       u'Host: Tom Jones',
#                                       u'Tom Jones, Paul Lynde, Karen Wyman',
#                                       u'Host: Tom Jones',
#                                       u'June 29, 2009',
#                                       u'Tom Jones / The Seekers / Dee Dee Sharp / Sid Caesar',
#                                       u'Series 1, Show 40',
#                                       u'Tom Jones, Totie Fields, Jackie DeShannon']}}



data = {
    'Name': [u'Tom Jones', 'JD', 'SB'],
    'Birthday': [u'1940-06-07'],
    'Films': {   'Character': [], 'Film': []},
    'Description': [ u'Sir Thomas Jones Woodward, OBE, known by his stage name Tom Jones, is a Welsh singer. He became...'],
    'Place of Birth': [u'Treforest'],
    'Siblings': [u'Shelia Woodward'],
    }
# Printer
def print_table(data):
    # for key, values in data.iteritems():
        # print key, ':', values, ':', len(values)
    for key, values in data.iteritems():
        #if value is list, just print list
        if (type(values) is list):
            print "|" + left_header*"-" + ((whole+3))*"-" + "-|"
            print  "| " + colwidth0.format(str(key)+' :') + "| ",
            # if list only contains one element, no newline needed
            if(len(values)==1):
                for one in xrange(len(values)):
                    #auto break-line
                    if(len(values[one]) > whole):
                        a = str(values[one])
                        list_s = [a[i:i+whole] for i in range(0, len(a), whole)]
                        for i in xrange(len(list_s)):
                            if(i==0):
                                print colwidth1.format(list_s[i])+"|",
                            else:
                                print "\n|" + (1+left_header) * " " + "|  " + colwidth1.format(list_s[i])+"|",
                    else:
                        print colwidth1.format(values[one])+"|",
                print ""
            else:
                #if multiple elements in list, print them in new lines
                for i in xrange(len(values)):
                    if(i==0):
                        print colwidth1.format(values[i])+"|",
                    else:
                        print "\n|" + (1+left_header) * " " + "|  " + colwidth1.format(values[i])+"|",
                print ""
        # if value is a dict, break column based on number on dicts


        elif(type(values) is dict):
            #print multi-header
            print "|" + left_header*"-" + ((whole+3))*"-" + "-|"
            print  "| " + colwidth0.format(str(key)+' :') + "| ",
            n = len (values)
            tmp_colwidth = "{0:<"+str((whole-n+1)/n)+"}"
            for keys in values:
                print tmp_colwidth.format(str(keys)+ ' :') + "|",
            print ""
            # print contents
            for inner_key, inner_value in values:
                print "\n|" + (1+left_header) * " " + "|  " + tmp_colwidth.format(list_s[i])+"|",












    print "|" + left_header*"-" + ((whole+3))*"-" + "-|"

    # elif(type(values) is dict):





# Populating the dictionary
for iter1 in attribute:
    total["Attribute"].append(iter1)
for iter2 in res_ids:
    total["RES_ID"].append(iter2)
for iter3 in nEName:
    total["networkElementName"].append(iter3)
for iter4 in ipList:
    total["IPv4"].append(iter4)

# Let's print the dictionary
print_table(data)