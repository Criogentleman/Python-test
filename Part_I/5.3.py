'''5.3 Скрипт должен запрашивать у пользователя:

    информацию о режиме интерфейса (access/trunk),
        пример текста запроса: 'Enter interface mode (access/trunk): '
    номере интерфейса (тип и номер, вида Gi0/3)
        пример текста запроса: 'Enter interface type and number: '
    номер VLANа (для режима trunk будет вводиться список VLANов)
        пример текста запроса: 'Enter vlan(s): '

В зависимости от выбранного режима, на стандартный поток вывода, должна возвращаться соответствующая конфигурация access или trunk (шаблоны команд находятся в списках access_template и trunk_template).

При этом, сначала должна идти строка interface и подставлен номер интерфейса, а затем соответствующий шаблон, в который подставлен номер VLANа (или список VLANов).'''

access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan {}']
INPUT = input ('Select switchport mode:')
IFACE = input ('Select interface:')
VLANS = input ('Select vlans:')
access_template[1] = access_template[1].format(VLANS)
trunk_template[2] = trunk_template[2].format(VLANS)


DICT = {'access' : access_template, 'trunk' : trunk_template}
A_DICT = DICT[INPUT]

RESULT = 'Interface ' + IFACE + '\n' + '\n'.join(A_DICT)
print (RESULT)
