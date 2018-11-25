def access_interface_gen(interface_dict):
  access_template = ['switchport mode access',
                    'switchport access vlan',
                    'switchport nonegotiate',
                    'spanning-tree portfast',
                    'spanning-tree bpduguard enable']
  config = []
  for intf, vlan in interface_dict.items():
      config.append('Interface {}'.format(intf))
      for line in access_template:
          if 'access vlan' in line:
            config.append(line + ' {}'.format(vlan))
          elif not 'access vlan' in line:
            config.append(line)
  return(config)

access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }

print(access_interface_gen(access_dict))
