MAC = 'AAAA:BBBB:CCCC'.split(':')
MAC = ''.join([bin(int(mac, 16))[2:] for mac in MAC])
print(MAC)
#or
MAC = 'AAAA:BBBB:CCCC'.replace(':', '')
MAC = bin(int(MAC, 16))[2:]
