'''6.1 
    Запросить у пользователя ввод IP-адреса в формате 10.0.1.1.
    Определить какому классу принадлежит IP-адрес.
    В зависимости от класса адреса, вывести на стандартный поток вывода:
        'unicast' - если IP-адрес принадлежит классу A, B или C
        'multicast' - если IP-адрес принадлежит классу D
        'local broadcast' - если IP-адрес равен 255.255.255.255
        'unassigned' - если IP-адрес равен 0.0.0.0
        'unused' - во всех остальных случаях
'''

IP = input ('Enter IP:')
IP_OCTETS = IP.split('.')
OCTETS_CHECK = int (IP_OCTETS[0])

if  OCTETS_CHECK >= 1 and OCTETS_CHECK <= 126 or OCTETS_CHECK >= 128 and OCTETS_CHECK <= 191 or OCTETS_CHECK >= 192 and OCTETS_CHECK <= 223:
  print (IP + ' - ' + 'unicast')
elif OCTETS_CHECK == 127:
  print (IP + ' - ' + 'localhost')
elif OCTETS_CHECK >= 234 and OCTETS_CHECK <= 239:
  print (IP + ' - ' + 'multicast')
elif int (IP_OCTETS[0]) == 255 and int (IP_OCTETS[1]) == 255 and int (IP_OCTETS[2]) == 255 and int (IP_OCTETS[3]) == 255:
  print (IP + ' - ' + 'local broadcast')
elif int (IP_OCTETS[0]) == 0 and int (IP_OCTETS[1]) == 0 and int (IP_OCTETS[2]) == 0 and int (IP_OCTETS[3]) == 0:
  print (IP + ' - ' + 'unassigned')
else:
  print ('unused')
