command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'.split()[-1].split(',')
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'.split()[-1].split(',')
vlans = set(command1).intersection(set(command2))
vlans = [int(vlan) for vlan in vlans]
vlans.sort()
print(vlans)
