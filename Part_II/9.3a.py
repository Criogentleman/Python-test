def get_intf_vlans (sw_config):
  intf_access = {}
  intf_trunk = {}
  intf_access_list = []
  with open (sw_config, 'r') as sw_conf_txt:
    for line in sw_conf_txt:
      if 'interface' in line:   #Line checking to create interface variable
        interface = line.strip().split()[-1]
      elif 'access vlan' in line:   #Checking next lines for 'access vlan', if true vlan variable created
        access_vl = int(line.strip().split()[-1])
        intf_access[interface] = access_vl
      elif 'allowed vlan' in line:    #Checking next lines for 'allowed vlan', if true vlan variable for trunk port created
        trunk_vl = line.strip().split()[4:]
        trunk_vl = [int(x) for x in trunk_vl[0].split(',')]
        print(trunk_vl)
        intf_trunk[interface] = trunk_vl
      elif 'mode access' in line:
        intf_access_list.append(interface)
  for x in intf_access_list:
    if not x in (y for y in [*intf_access]):
      intf_access[x] = 1

  return(intf_access, intf_trunk)

get_intf_vlans('sw2_config.txt')
