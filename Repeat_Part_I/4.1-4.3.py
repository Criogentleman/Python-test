NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload".replace('Fast', 'Gigabit')
print(NAT)

MAC = 'AAAA:BBBB:CCCC'.replace(':', '.')
print(MAC

CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'.split()[-1].split(',')
print(CONFIG)
