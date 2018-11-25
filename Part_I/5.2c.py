#5.2c Переделать скрипт из задания 5.2b таким образом, чтобы, при запросе параметра, которого нет в словаре устройства, отображалось сообщение 'Такого параметра нет'.

london_co = {
    'r1' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.1'
    },
    'r2' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.2'
    },
    'sw1' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '3850',
    'ios': '3.6.XE',
    'ip': '10.255.0.101',
    'vlans': '10,20,30',
    'routing': True
    }
}

DEVICE = input('Choose device:')
KEYS = london_co[DEVICE].keys()
KEYS_LIST = list(KEYS)
KEYS_STR = ','.join(KEYS_LIST)
PARAM = input('Choose param (' + KEYS_STR + ') :')
print (london_co.get(DEVICE).get(PARAM, 'There is no parameter ' '"'+ PARAM + '"'))
