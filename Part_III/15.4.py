import re
from pprint import pprint

def regex_func(filename):
  with open(filename, 'r') as text:
    regex = '(\S+)\s+(\d+.\d+.\d+.\d+|unassigned)\s+\w+\s+\w+\s+(up|administratively down|down)\s+(\w+)'
    ip_int_br = []
    for line in text:
      match = re.search(regex, line)
      if match:
        ip_int_br.append(match.groups())
  return(ip_int_br)

pprint(regex_func('sh_ip_int_br_2.txt'))
