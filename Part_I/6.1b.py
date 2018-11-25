'''6.1b Сделать копию скрипта задания 6.1a.
Дополнить скрипт:
    Если адрес был введен неправильно, запросить адрес снова.
'''

IP = input ('Enter IP:')
IP_CHECK = False

while not IP_CHECK:
  i = 0
  IP_OCTETS = IP.split('.')
  while i < 4:
      if not len(IP_OCTETS) == 4:
        break
      elif not IP_OCTETS[0 + i].isdigit():
        break
      elif len (IP_OCTETS[0 + i]) > 3:
        break
      elif  int(0) < int (IP_OCTETS[0 + i]) > int(255):
        break
      elif len(IP_OCTETS[0 + i]) == 2 or len(IP_OCTETS[0 + i]) == 3:
        A = IP_OCTETS[0 + i]
        if int(A[0]) == 0:
          break
      i += 1  
  else:
      IP_CHECK = True
      break
  IP = input("Incorrect IPv4 address, try")

if IP_CHECK == True:
  if 1 <= int(IP_OCTETS[0]) <= 126 or 128 <= int(IP_OCTETS[0]) <= 191 or 192 <= int(IP_OCTETS[0]) <= 223:
    print (IP + ' - ' + 'unicast')
  elif int(IP_OCTETS[0]) == 127:
    print (IP + ' - ' + 'localhost')
  elif 234 <= int(IP_OCTETS[0]) <= 239:
    print (IP + ' - ' + 'multicast')
  for i in range(4):
    if int(IP_OCTETS[0 + i]) == 255:
      print (IP + ' - ' + 'local broadcast')
      break
    elif int (IP_OCTETS[0 + i]) == 0:
      print (IP + ' - ' + 'unassigned')
      break
