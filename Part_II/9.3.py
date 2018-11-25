def get_intf_vlans (sw_config):
  intf_access = {}
  intf_trunk = {}
  with open (sw_config, 'r') as sw_conf_txt:
    for line in sw_conf_txt:
      if 'interface' in line:
        interface = line.strip().split()[-1]
      elif 'access vlan' in line:
        access_vl = int(line.strip().split()[-1])
        intf_access[interface] = access_vl
      elif 'allowed vlan' in line:
        trunk_vl = line.strip().split()[4:]
        trunk_vl = [int(x) for x in trunk_vl[0].split(',')]
        intf_trunk[interface] = trunk_vl
  return(intf_access, intf_trunk)

get_intf_vlans('sw1_config.txt')
