from pprint import pprint
from ip_int_br import regex_func

def convert_to_dict(headers, ip_int_br_list):
  dict_list = []
  i = 0
  while i < len(ip_int_br_list):
    dict_list.append(dict(zip(headers, ip_int_br_list[i])))
    i += 1
  return(dict_list)

headers = ['interface', 'address', 'status', 'protocol']

pprint(convert_to_dict(headers, regex_func('sh_ip_int_br_2.txt')))
