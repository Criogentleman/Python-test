#1 Обработать строку NAT таким образом, чтобы в имени интерфейса вместо FastEthernet было GigabitEthernet.
NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
NAT = NAT.replace ('Fast', 'Gigabit') #Method 1
NAT2 = "ip nat inside source list ACL interface FastEthernet0/1 overload".replace ('Fast', 'Gigabit') #Method 2
print (NAT, '\n', NAT2,"\n" * 2, sep='') #sep='' убрать пробелы после разделения

#sep='' пример
print (22,22,2,3,'\n','test',400,500, "\n")
print (22,22,2,3,'\n','test',400,500,'\n'*2, sep='')

#2 Преобразовать строку MAC из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX
MAC = 'AAAA:BBBB:CCCC'.replace(':','.')
print (MAC, '\n' * 4)

#3 Получить из строки CONFIG список VLANов вида: ['1', '3', '10', '20', '30', '100']
CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'.split()
VLANS = CONFIG[-1].split(',')
print (CONFIG, '\n',CONFIG[-1], '\n', VLANS, sep='')
