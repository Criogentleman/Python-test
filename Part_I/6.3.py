'''6.3 В скрипте сделан генератор конфигурации для access-портов.
Сделать аналогичный генератор конфигурации для портов trunk.

Задача для портов 0/1, 0/2, 0/4:
    сгенерировать конфигурацию на основе шаблона trunk_template
    с учетом ключевых слов add, del, only
'''

access_template = ['switchport mode access',
                   'switchport access vlan',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan']

fast_int = {'access':{'0/12':'10','0/14':'11','0/16':'17','0/17':'150'}, 
            'trunk':{'0/1':['add','10','20'],
                     '0/2':['only','11','30'],
                     '0/4':['del','17']} }

for intf, vlan in fast_int['access'].items():
    print('interface FastEthernet' + intf)
    for command in access_template:
        if command.endswith('access vlan'):
            print(' {} {}'.format(command, vlan))
        else:
            print(' {}'.format(command))

for interface, vlans in fast_int['trunk'].items():
  print('Interface FastEthernet' + interface)
  for command in trunk_template:
    vlans1 = (','.join(vlans[1:]))
    if command.endswith('allowed vlan') and 'add' in vlans:
      print (' {} {} {}'.format(command, 'add', vlans1))
    elif command.endswith('allowed vlan') and 'only' in vlans:
      print (' {} {}'.format(command, vlans1))
    elif command.endswith('allowed vlan') and 'del' in vlans:
      print (' {} {} {}'.format(command, 'remove', vlans1))
    else:
      print (' {}'.format(command))
