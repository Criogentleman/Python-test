def trunk_intf_gen(intf_vlan_dict):
#First param - dict of intf:vlans
  trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk native vlan 999',
                      'switchport trunk allowed vlan']
  config = []
  for intf, vlans in intf_vlan_dict.items():
    config.append('Interface {}'.format(intf))
    for line_template in trunk_template:
      if 'allowed vlan' in line_template:
        vlans_str = ', '.join([str(x) for x in vlans])
        config.append(line_template + ' ' + vlans_str)
      else:
        config.append(line_template)
  return(config)


trunk_dict = { 'FastEthernet0/1':[10,20,30],
               'FastEthernet0/2':[11,30],
               'FastEthernet0/4':[17] }

print(trunk_intf_gen(trunk_dict))
