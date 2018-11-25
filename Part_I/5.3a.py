'''5.3a Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима, задавались разные вопросы в запросе о номере VLANа или списка VLANов:

    для access: 'Enter VLAN number:'
    для trunk: 'Enter allowed VLANs:'
    '''

access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan {}']

CHOOSE_VLAN_DICT = {'access' : 'Enter VLAN number', 'trunk' : 'Enter allowed VLANs:'}
INPUT = input ('Select switchport mode:')
IFACE = input ('Select interface:')
VLANS = input (CHOOSE_VLAN_DICT[INPUT])
access_template[1] = access_template[1].format(VLANS)
trunk_template[2] = trunk_template[2].format(VLANS)


DICT = {'access' : access_template, 'trunk' : trunk_template}
A_DICT = DICT[INPUT]

RESULT = 'Interface ' + IFACE + '\n' + '\n'.join(A_DICT)
print (RESULT)
