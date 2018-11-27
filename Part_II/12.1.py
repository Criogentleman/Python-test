import subprocess

def ping_script(ip_list):
  reachable = []
  unreachable = []
  for ip in ip_list:
    ping = subprocess.run(['ping', ip, '-c 3'], stdout=subprocess.DEVNULL)    #DEVNULL to hide process
    if ping.returncode == 0:
      reachable.append(ip)
    else:
      unreachable.append(ip)
  return reachable, unreachable

ping_script(input('Enter IP\'s: ').split())
