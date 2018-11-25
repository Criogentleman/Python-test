"""6 Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:

Protocol:               OSPF
Prefix:                 10.0.24.0/24
AD/Metric:              110/41
Next-Hop:               10.0.13.3
Last update:            3d18h
Outbound Interface:     FastEthernet0/0  
"""

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route = ospf_route.replace('O', 'OSPF').replace(',', '').split()
print (ospf_route)

SH_IP_RO_OSPF = '''
Protocol:               {}
Prefix:                 {}
AD/Metric:              {}
Next-Hop:               {}
Last update:            {}
Outbound Interface:     {}
'''
print (SH_IP_RO_OSPF.format(ospf_route[0], ospf_route[1], ospf_route[2], ospf_route[4], ospf_route[-1], ospf_route[-2]   ))
