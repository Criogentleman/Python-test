#7 Преобразовать MAC-адрес в двоичную строку (без двоеточий).
MAC = 'AAAA:BBBB:CCCC'
MAC = MAC.replace(':', '')
print (MAC)
MAC_INT = int(MAC, 16)
print (MAC_INT)
MAC_BIN = '{:b}'.format(MAC_INT)
print (MAC_BIN)
