#5.2d Переделать скрипт из задания 5.2c таким образом, чтобы, при запросе параметра, пользователь мог вводить название параметра в любом регистре.

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
A = input('Choose param (' + KEYS_STR + ') :')
B = london_co[DEVICE].get(A)
A_SWAP = A.swapcase()
A_CHECK = london_co[DEVICE].setdefault(A_SWAP, B)
print (A_CHECK)
