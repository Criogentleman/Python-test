ignore = ['duplex', 'alias', 'Current configuration']

def ignore_command(command, ignore):
  #First param - checking config line, second ignore list
    return any(word in command for word in ignore)

def config_to_dict(config):
  conf_dict = {}
  with open(config, 'r') as config_txt:
    for line in config_txt:
      if (ignore_command(line, ignore)) != True and not line.startswith('!'):   #Function call ignore_command (line 3)
        if not line.startswith(' '):
          glob_comm = line.strip('\n')
          subcomm = []
          conf_dict[glob_comm] = subcomm
        else:
          subcomm.append(line.strip('\n'))
  return(conf_dict)

config_to_dict('sw1_config.txt')
