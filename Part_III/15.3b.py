import re
from pprint import pprint

def regex_func(filename):
  with open(filename, 'r') as text:
    ip_dict = {}
    regex_ip_mask = '(\d+.\d+.\d+.\d+)\s(\d+.\d+.\d+.\d+)'
    for line in text:
      if line.startswith('interface'):
        ip_list = []
        iface = line.split()
      if 'ip address' in line:
        match = re.search(regex_ip_mask, line)
        if match:
          ip_list.append((match.group(1), match.group(2)))
          ip_dict[iface[1]] = ip_list
    return(ip_dict)

pprint(regex_func('r1_config.txt'))
