import nginx

file_path = 'D:/nginx.conf'
c = nginx.loadf(file_path)
content = open(file_path).read()
data = nginx.loads(content)
print(data)


def lst2string(lst):
    tmp = ""
    for line in lst:
        for k, v in line.iteritems():
            if len(tmp) == 0:
                tmp = ("  " + k+" "+v + ";")
            else:
                tmp += ("\n  " + k+"; "+v)
    return tmp

# print(lst2string([{'safafas': ''}, {'aafsaf': ''}]))


def generate_if_area(if_dict):
    # 'if ("")': [{'safafas': ''}, {'aafsaf': '']}
    tmp = ""
    for key, value in if_dict.iteritems():
        if key.strip().startswith("if"):
           tmp = key +" {\n" + lst2string(value) + "\n}"
    return tmp


print(generate_if_area(dict({'if ("")': [{'safafas': ''}, {'aafsaf': ''}]})))


# return
# conf = c.as_dict["conf"]
# for line in conf:
#     for key, value in line.iteritems():
#         if key.strip() == "http":
#             for http_area in value:
#                 # print type(http_area),http_area
#                 server_info_list = http_area.get("server","")
#                 if len(server_info_list) > 0:
#                     # print(type(server_info_list),server_info_list)
#                     lcation_arr = ""
#                     for server_info_msg in server_info_list:
#                         for key,value in server_info_msg.iteritems():
#                             if key.strip().startswith("location"):
#                                 # print(key, value)
#                                 if key.strip() == "location /" and len(value) == 0:
#                                     print(key, "=====empty location=======", value)
#                                 elif key.strip().startswith("location") and len(value) != 0:
#                                     if key.strip().find("="):
#                                         lcation_arr = key.strip().split("=")
#                                     else:
#                                         lcation_arr = key.strip().split("location")
#                                     for field_line in value:
#                                         for k,v in field_line.iteritems():
#                                             if k == "proxy_set_header":
#                                                 print ("proxy_set_header:%s" % v)
#                                         print(field_line)
#                                     # print(key, lcation_arr,"=====not empty location=======", value)
#                                     # location_name = key.split("=")[1]
#
#
#
#                                     pass
#                                 #     print(key,"----",value)
#                                 # print("=====------",key.split("="))
#                         # print(type(server_info_msg),server_info_msg)
#                     print("=========")

        # print(key,value)
    # print(type(line),len(line),line,http)
# print(type(c))
# ll = c.servers
# print(ll,type(ll))
# print(type(c.as_dict),c.as_dict)
# for key,val in c.as_dict.iteritems():
#     print(key,type(val),val)
#     for line in val:
#         # print "-->",type(line),line
#         #
#         for k,v in line.iteritems():
#             print("value:",k,v)
#             if type(v) == dict:
#                 print v["http"]
# print(c.servers)

