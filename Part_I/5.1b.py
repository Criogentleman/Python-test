#!/usr/bin/env python3
#5.1b. Преобразовать скрипт из задания 5.1a таким образом, чтобы сеть/маска не запрашивались у пользователя, а передавались как аргумент скрипту.

#
from sys import argv
IPARG = argv[-1]
print (IPARG)
A = IPARG.split('/')
#
IP = A[0].split('.')
IP = [int(i) for i in IP]
PREFIX = int(A[1])
MASK_BIN = list('1' * PREFIX + (32 - PREFIX) * '0')
MASK_BIN.insert(8, '.'); MASK_BIN.insert(17, '.'); MASK_BIN.insert(26, '.')
MASK_BIN = ''.join(MASK_BIN).split('.')
MASK_DEC = int(MASK_BIN[0], 2), int(MASK_BIN[1], 2), int(MASK_BIN[2], 2), int(MASK_BIN[3], 2)
##
IP_BIN = ['{0:>08b} {1:>08b} {2:>08b} {3:>08b}'.format(IP[0], IP[1], IP[2], IP[3])]
IP_BIN = IP_BIN[0].split()

NETWORK = [int (IP_BIN[0], 2) & int (MASK_BIN[0], 2), int (IP_BIN[1], 2) & int (MASK_BIN[1], 2), int (IP_BIN[2], 2) & int (MASK_BIN[2], 2), int (IP_BIN[3], 2) & int (MASK_BIN[3], 2)]
##
RESULT = '''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:>08b} {1:>08b} {2:>08b} {3:>08b}
Mask:
/{4}
{5:<8} {6:<8} {7:<8} {8:<8}
{5:>08b} {6:>08b} {7:>08b} {8:>08b}
'''
print (RESULT.format(NETWORK[0], NETWORK[1], NETWORK[2], NETWORK[3], PREFIX, MASK_DEC[0], MASK_DEC[1], MASK_DEC[2], MASK_DEC[3], ))

