'''Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000
'''

A = input('Enter IP/mask:').split('/')
IP = A[0].split('.')
IP = [int(i) for i in IP]
PREFIX = int(A[1])
MASK_BIN = list('1' * PREFIX + (32 - PREFIX) * '0')
MASK_BIN.insert(8, '.'); MASK_BIN.insert(17, '.'); MASK_BIN.insert(26, '.')
MASK_BIN = ''.join(MASK_BIN).split('.')
MASK_DEC = int(MASK_BIN[0], 2), int(MASK_BIN[1], 2), int(MASK_BIN[2], 2), int(MASK_BIN[3], 2)

RESULT = '''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:>08b} {1:>08b} {2:>08b} {3:>08b}
Mask:
/{4}
{5:<8} {6:<8} {7:<8} {8:<8}
{5:>08b} {6:>08b} {7:>08b} {8:>08b}
'''
print (RESULT.format(IP[0], IP[1], IP[2], IP[3], PREFIX, MASK_DEC[0], MASK_DEC[1], MASK_DEC[2], MASK_DEC[3],  ))
