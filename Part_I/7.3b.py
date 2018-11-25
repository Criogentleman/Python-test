MAC_TXT = open('sh_mac.txt', 'r')
VLAN = input('Enter vlan: ')
while not 1 <= int(VLAN) <= 4096:
  VLAN = input('Wrong vlan number(1-4096): ')
for LINES in MAC_TXT:
  LINES = LINES.strip().split('\n')
  if LINES[0].strip(): 
    LINE_STR = LINES[0]
    LINES = LINE_STR.split()
    if LINES[0].isdigit() and LINES[0] == VLAN:
      LINES.pop(2)
      LINES = '   '.join(LINES)
      print(LINES)
