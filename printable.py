from collections import OrderedDict
__author__ = 'CC'
from collections import defaultdict
from itertools import izip_longest

total = defaultdict(list)

# Column width
whole=88
one_half=30
one_fourth=12
left_header = 20
colwidth0="{0:<"+str(left_header)+"}"
colwidth1="{0:<"+str(whole)+"}"
colwidth2="{0:<"+str(one_half)+"}"
colwidth3="{0:<"+str(one_fourth)+"}"



data = OrderedDict([('Description', [u'Elon Reeve Musk is a South Africa-born, Canadian American business magnate, engineer and investor. He is the CEO and CTO of SpaceX, CEO and chief product architect of Tesla Motors, and chairman of SolarCity. He is the founder of SpaceX and a cofounder of PayPal, Tesla Motors, and Zip2. He has also envisioned a conceptual high-speed transportation system known as the Hyperloop.']), ('Name', [u'Elon Musk']), ('Place of Birth', [u'Pretoria']), ('Siblings', [u'Tosca Musk', u'Kimbal Musk']), ('Birthday', [u'1971-06-28']), ('Spouse(s)', [{'Marriage From': u'2000', 'Marriage To': u'2008', 'Ceremony Location': '', 'Spouse Name': u'Justine Musk'}, {'Marriage From': u'2010-09-25', 'Marriage To': u'2012', 'Ceremony Location': u'Dornoch Cathedral', 'Spouse Name': u'Talulah Riley'}]), ('Films', [{'Character': '', 'Film': u'Iron Man 2'}]), ('Founded', [u'PayPal', u'SpaceX', u'Zip2', u'X.com', u'Musk Foundation', u'Tesla Motors']), ('Leadership', [{'To': '', 'Organization': u'Tesla Motors', 'From': u'2008-10', 'Role': u'Chief Executive Officer', 'Title': u'Co-Founder, Chairman CEO and Product Architect'}, {'To': '', 'Organization': u'SpaceX', 'From': '', 'Role': u'Chief Executive Officer', 'Title': ''}]), ('Board Membership', [{'To': '', 'Organization': u'The Planetary Society', 'From': u'2003', 'Role': '', 'Title': ''}, {'To': '', 'Organization': u'Mahalo.com', 'From': '', 'Role': '', 'Title': ''}, {'To': '', 'Organization': u'Tesla Motors', 'From': u'2004-04', 'Role': '', 'Title': u'Chair'}, {'To': '', 'Organization': u'SpaceX', 'From': u'2002-06', 'Role': '', 'Title': u'CEO'}, {'To': '', 'Organization': u'X Prize Foundation', 'From': u'2005-01', 'Role': '', 'Title': ''}])])

# Printer
def print_table(data):
    # for key, values in data.iteritems():
        # print key, ':', values, ':', len(values)
    for key, values in data.iteritems():
        #if value is list, just print list
        if len(values)==0:
            continue
        # if value is dicts, break column based on number on dicts
        elif(type(values[0]) is dict):
            #print multi-header
            print "|" + left_header*"-" + ((whole+3))*"-" + "-|"
            print  "| " + colwidth0.format(str(key)+' :') + "| ",
            n = len (values[0])
            tmp_colwidth = "{0:<"+str((whole - 2*n + 2) / n)+"}"
            last_colwidth = "{0:<"+str(whole - (2+(whole - 2*n + 2) / n) * (n-1))+"}"
            for keys in values[0].keys():
                if(values[0].keys().index(keys) == len(values[0]) - 1):
                    print last_colwidth.format(str(keys)+ ' :') + "|",
                else:
                    print tmp_colwidth.format(str(keys)+ ' :') + "|",
            print "\n|" + left_header*"-" + ((whole+3))*"-" + "-|"
            #print contents
            for ii in xrange(len(values)):
                print "|" + (1+left_header) * " " + "| ",
                for inner_key, inner_value in values[ii].iteritems():
                    #last column auto-scaling
                    if(values[ii].keys().index(inner_key) == len(values[ii]) - 1):
                        #auto break-line
                        if(len(inner_value) > (whole - 2*n + 2) / n):
                            a = str(inner_value)
                            list_s = [a[i:i+(whole - 2*n + 2)] for i in range(0, len(a), (whole - 2*n + 2))]
                            for i in xrange(len(list_s)):
                                indexes = values[ii].keys().index(inner_key)
                                print "\n|" + (1+left_header) * " " + "|  " + ((indexes) * ((whole - 2*n + 2) / n) + indexes) * " " + "|" + last_colwidth.format(list_s[i])+"|",
                        else:
                            print last_colwidth.format(str(inner_value)) + "|",
                    #previous columns
                    else:
                        #auto break-line
                        if(len(inner_value) > (whole - 2*n + 2) / n):
                            a = str(inner_value)
                            list_s = [a[i:i+((whole - 2*n + 2)/n)] for i in range(0, len(a), ((whole - 2*n + 2)/n))]

                            for i in xrange(len(list_s)):
                                indexes = values[ii].keys().index(inner_key)
                                print "\n|" + (1+left_header) * " " + "|  " + ((indexes) * ((whole - 2*n + 2) / n) + indexes) * " " + "|" + tmp_colwidth.format(str(list_s[i]))+"|",
                            # print "\n|" + left_header*"-" + ((whole+3))*"-" + "-|"
                        else:
                            print tmp_colwidth.format(str(inner_value)) + "|",

                print ""
        # if value isn't dicts
        else:
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

    print "|" + left_header*"-" + ((whole+3))*"-" + "-|"



# Let's print the dictionary
print_table(data)