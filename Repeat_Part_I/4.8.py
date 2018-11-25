IP = '192.168.3.1'.split('.')
IP = [int(num) for num in IP]
IP_res = ''.join(('{:<10} '.format(i)) for i in IP)
IP_bin = ''.join(('{:>010b} '.format(i)) for i in IP)
print(IP_res) 
print(IP_bin)
