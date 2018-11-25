'''6.1a Сделать копию скрипта задания 6.1.
Дополнить скрипт:
    Добавить проверку введенного IP-адреса.
    Адрес считается корректно заданным, если он:
        состоит из 4 чисел разделенных точкой,
        каждое число в диапазоне от 0 до 255.
Если адрес задан неправильно, выводить сообщение:
    'Incorrect IPv4 address'
'''

IP = input ('Enter IP:')
IP_OCTETS = IP.split('.')  #Split checking for '.'
IP_CHECK = False
if int:
  i = 0
  while i < 4:
    if not len(IP_OCTETS) == 4:               #Checking 4 obj in list
      print ('Incorrect IPv4 address')
      break
    elif not IP_OCTETS[0 + i].isdigit():      #Checking if obj is numbers
      print ('Incorrect IPv4 address')
      break
    elif len (IP_OCTETS[0 + i]) > 3:          #Checking if number not contain more than 3 digits
      print ('Incorrect IPv4 address')
      break
    elif  int(0) < int (IP_OCTETS[0 + i]) > int(255):   #Checking if number in range 0-255
      print ('Incorrect IPv4 address')
      break
    elif len(IP_OCTETS[0 + i]) == 2 or len(IP_OCTETS[0 + i]) == 3:
      A = IP_OCTETS[0 + i]                    #Checking format "000 or 001"
      if int(A[0]) == 0:
        print ('Incorrect IPv4 address')
        break
    i += 1  
  else:
    IP_CHECK = True

if IP_CHECK == True:
  if 1 <= int(IP_OCTETS[0]) <= 126 or 128 <= int(IP_OCTETS[0]) <= 191 or 192 <= int(IP_OCTETS[0]) <= 223:
    print (IP + ' - ' + 'unicast')
  elif int(IP_OCTETS[0]) == 127:
      print (IP + ' - ' + 'localhost')
  elif 234 <= int(IP_OCTETS[0]) <= 239:
      print (IP + ' - ' + 'multicast')
  elif int (IP_OCTETS[0]) == 255 and int(IP_OCTETS[1]) == 255 and int(IP_OCTETS[2]) == 255 and int(IP_OCTETS[3]) == 255:
     print (IP + ' - ' + 'local broadcast')
  elif int (IP_OCTETS[0]) == 0 and int (IP_OCTETS[1]) == 0 and int (IP_OCTETS[2]) == 0 and int (IP_OCTETS[3]) == 0:
    print (IP + ' - ' + 'unassigned')
