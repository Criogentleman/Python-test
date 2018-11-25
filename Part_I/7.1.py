OSPF_FILE = open ('ospf.txt', 'r')
INFO = 'Protocol:,Prefix:,AD/Metric:,Next-Hop:,Last update:,Outbound Interface:, '
INFO = INFO.split(',')

for LINES in OSPF_FILE:
  OSPF = LINES.replace('O', 'OSPF').replace("'", '').replace(',', '').split()
  OSPF.append('')
  OSPF.pop(3)
  a=0
  while a <= 6:
    print ('{:22}'.format(INFO[0+a]) + '{}'.format(OSPF[0+a]))
    a+=1
