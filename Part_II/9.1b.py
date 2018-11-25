def access_interface_gen(interface_dict, port_sec = False):
  #First apply dict with key pair intf:vlan. Second if port_sec = True - add port security on intf.
  access_template = ['switchport mode access',
                    'switchport access vlan',
                    'switchport nonegotiate',
                    'spanning-tree portfast',
                    'spanning-tree bpduguard enable']

  port_security = ['switchport port-security maximum 2',
                     'switchport port-security violation restrict',
                     'switchport port-security']
  
  config_dict = {}
  for intf, vlan in interface_dict.items():
    config_list = []      #For each iteration it holding config for one intf. 
    for line in access_template:
      if 'access vlan' in line:
        config_list.append(line + ' {}'.format(vlan))
      elif not 'access vlan' in line:
        config_list.append(line)
    if port_sec == True:
      for line in port_security:
        config_list.append(line)
    config_dict.update({'Interface {}'.format(intf):config_list})   #For each iteration add dict entry intf:config.
  return(config_dict)

access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }

print(access_interface_gen(access_dict, True))
