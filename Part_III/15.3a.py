from sys import argv
import re

filename = argv[-1]

def regex_func(filename):
    with open(filename, 'r') as text:
        ip_dict = {}
        regex_ip_mask = '(\d+.\d+.\d+.\d+)\s(\d+.\d+.\d+.\d+)'
        for line in text:
            if line.startswith('interface'):
                iface = line.split()
            if 'ip address' in line:
                match = re.search(regex_ip_mask, line)
                if match:
                    ip_dict[iface[1]] = (match.group(1), match.group(2))
    return ip_dict

print(regex_func(filename))
