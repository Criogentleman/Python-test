MAC_TXT = open('sh_mac.txt','r')
for LINES in MAC_TXT:
  LINES = LINES.strip().split('\n')
  if LINES[0].strip(): 
    LINE_STR = LINES[0]
    LINES = LINE_STR.split()
    if LINES[0].isdigit():
      LINES.pop(2)
      print(LINES[0] + 4 * ' ' + LINES[1]+ 4 * ' ' + LINES[2])
