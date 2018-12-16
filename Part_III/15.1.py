from sys import argv
import re

filename, regex = argv[1:]

def regex_func(filename, reg_ex):
    with open(filename, 'r') as text:
        for line in text:
            match = re.search(reg_ex, line)
            if match:
                print(line.strip())

regex_func(filename, regex)
