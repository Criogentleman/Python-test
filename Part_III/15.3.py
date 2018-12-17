from sys import argv
import re

filename = argv[-1]

def regex_func(filename):
    with open(filename, 'r') as text:
        ip_list = []
        regex_ip_mask = '(\d+.\d+.\d+.\d+)\s(\d+.\d+.\d+.\d+)'
        for line in text:
            if 'ip address' in line:
                match = re.search(regex_ip_mask, line)
                if match:
                    ip_list.append((match.group(1), match.group(2)))
    return ip_list

print(regex_func(filename))
