from sys import argv
import re

filename, regex = argv[1:]

def regex_func(filename, reg_ex):
    with open(filename, 'r') as text:
        ip_list = []
        for line in text:
            match = re.search(reg_ex, line)
            if match:
                ip_list.append(match.group())
    return ip_list

print(regex_func(filename, regex))
