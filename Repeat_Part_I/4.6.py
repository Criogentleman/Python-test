ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'.replace('O', 'OSPF').replace('via', '').replace(',', '').replace('[', '').replace(']', '').split()

Ospf_param_list = ['Protocol:', 'Prefix:', 'AD/Metric:', 'Next-Hop:', 'Last update:', 'Outbound Interface:']

for param, ospf in zip(Ospf_param_list, ospf_route):
  print('{:22} {:15}'.format(param, ospf))
