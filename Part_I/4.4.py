'''4.3 Из строк command1 и command2 получить список VLANов, которые есть и в команде command1 и в команде command2.'''


command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
command1 = command1.split()
command2 = command2.split()
set1 = set(command1[-1].split(','))
set2 = set(command2[-1].split(','))
set3 = list(set1.intersection(set2))
result = int(set3[0]), int(set3[1]), int(set3[2])
res_list = list(result)
res_list.sort()
print (res_list)
