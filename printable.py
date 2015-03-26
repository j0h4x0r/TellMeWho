from collections import OrderedDict
from itertools import izip_longest

# Column width
whole=100
one_half=30
one_fourth=12
left_header = 30
colwidth0="{0:<"+str(left_header)+"}"
colwidth1="{0:<"+str(whole)+"}"
colwidth2="{0:<"+str(one_half)+"}"
colwidth3="{0:<"+str(one_fourth)+"}"
colwidth4="{0:<"+str(whole+left_header+3)+"}"



# Printer
def print_table(data, *arglist):
    #print header
    if len(arglist) is not 0:
        type_list_name = arglist[0]
        if len(type_list_name) is not 0:
            name = str(data["Name"][0].encode('ascii', 'ignore')) + "("
            for i in xrange(len(type_list_name)):
                if len(type_list_name) >=1 and type_list_name[i] == 'Person':
                    continue
                if i is not len(type_list_name)-1:
                    name = name + ' '+type_list_name[i] + ','
                else:
                    name = name + ' ' + type_list_name[i] + ')'
            print "|" + left_header*"-" + ((whole+3))*"-" + "-|"
            print "| "  + colwidth4.format(name) + " |"

    #print the rest
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
                lines_str = []
                for inner_key, inner_value in values[ii].iteritems():
                    #last column auto-scaling
                    if(values[ii].keys().index(inner_key) == len(values[ii]) - 1):
                        #auto break-line
                        if(len(inner_value) > whole - (2+(whole - 2*n + 2) / n) * (n-1)):
                            a = str(inner_value)
                            list_s = [last_colwidth.format(a[i:i+(whole - (2+(whole - 2*n + 2) / n) * (n-1))]) for i in range(0, len(a), (whole - (2+(whole - 2*n + 2) / n) * (n-1)))]
                            lines_str.append(list_s)
                            # for i in xrange(len(list_s)):
                            #     indexes = values[ii].keys().index(inner_key)
                            #     print "\n|" + (1+left_header) * " " + "|  " + ((indexes) * ((whole - 2*n + 2) / n) + indexes) * " " + "|" + last_colwidth.format(list_s[i])+"|",
                        else:
 
                            lines_str.append([last_colwidth.format(str(inner_value.encode('ascii','ignore')))])
                            #print last_colwidth.format(str(inner_value)) + "|",

                    #previous columns
                    else:
                        #auto break-line
                        if(len(inner_value) > (whole - 2*n + 2) / n):
                            a = (inner_value)
                            list_s = [tmp_colwidth.format(a[i:i+((whole - 2*n + 2)/n)]) for i in range(0, len(a), ((whole - 2*n + 2)/n))]
                            lines_str.append(list_s)
                            # for i in xrange(len(list_s)):
                            #     indexes = values[ii].keys().index(inner_key)
                            #     print "\n|" + (1+left_header) * " " + "|  " + ((indexes) * ((whole - 2*n + 2) / n) + indexes) * " " + "|" + tmp_colwidth.format(str(list_s[i]))+"|",
                            # # print "\n|" + left_header*"-" + ((whole+3))*"-" + "-|"
                        else:
                            lines_str.append([tmp_colwidth.format(str(inner_value.encode('ascii','ignore')))])
                            #print tmp_colwidth.format(str(inner_value)) + "|",

                for tup in izip_longest(*lines_str):
                    print "|" + (1+left_header) * " " + "| ",
                    linestr = ''
                    for i in range(len(tup)):
                        if tup[i]:
                            linestr += tup[i] + '| '
                        else:
                            if i == len(tup) - 1:
                                linestr += ((whole - (2+(whole - 2*n + 2) / n) * (n-1)) * ' ') + '| '
                            else:
                                linestr += ((whole - 2*n + 2) / n) * ' ' + '| '
                    print linestr
                if(ii is not len(values)-1):
                    print "|" + (left_header+2)*" " + ((whole+1))*"-" + "-|"
        # if value isn't dicts
        else:
            print "|" + left_header*"-" + ((whole+3))*"-" + "-|"
            print  "| " + colwidth0.format(str(key)+' :') + "| ",
            # if list only contains one element, no newline needed
            if(len(values)==1):
                for one in xrange(len(values)):
                    #auto break-line
                    if(len(values[one]) > whole):
                        a = (values[one])
                        list_s = [a[i:i+whole] for i in range(0, len(a), whole)]
                        for i in xrange(len(list_s)):
                            if(i==0):
                                print colwidth1.format(list_s[i])+"|",
                            else:
                               
                                print "\n|" + (1+left_header) * " " + "|  " + colwidth1.format(list_s[i].encode('ascii', 'replace')) + "|",
                    else:
                        print colwidth1.format(values[one])+"|",
                print ""
            else:
                #if multiple elements in list, print them in new lines
                for i in xrange(len(values)):
                    if(i==0):
                        print colwidth1.format(values[i])+"|",
                    else:
                        print "\n|" + (1+left_header) * " " + "|  " + colwidth1.format(values[i].encode('ascii', 'replace'))+"|",
                print ""

    print "|" + left_header*"-" + ((whole+3))*"-" + "-|"

 