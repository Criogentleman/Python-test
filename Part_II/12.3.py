import subprocess
from tabulate import tabulate

def ping_script(ip_list):
    reachable = []
    unreachable = []
    ip1_list = []
    for ip in ip_list:
        if '-' in ip:
            ip = ip.split('-')
            first = [int(x) for x in ip[0].split('.')]
            if not '.' in ip[-1]:
                for first[-1] in range(first[-1], int(ip[-1]) + 1):
                    ip1_list.append('.'.join([str(x) for x in first]))
            else:
                last = [int(x) for x in ip[-1].split('.')]
                for first[-1] in range(first[-1], last[-1] + 1):
                    ip1_list.append('.'.join([str(x) for x in first]))
        else:
            ip1_list.append(ip)

    for ip in ip1_list:
        ping = subprocess.run(['ping', ip, '-n', '3'], stdout=subprocess.DEVNULL)  # DEVNULL to hide process
        if ping.returncode == 0:
            reachable.append(ip)
        else:
            unreachable.append(ip)
    dict_head = {'reachable':reachable, 'unreachable':unreachable}
    return dict_head

ip_list = ['8.8.4.4-8', '76.122.94.1-2', '76.122.95.1-76.122.95.2']

print(tabulate(ping_script(ip_list), headers='keys'))
