def ignore_command(command, ignore):
  #First param - checking config line, second ignore list
    return any(word in command for word in ignore)

def config_to_dict(config):
  conf_dict = {}
  with open(config, 'r') as config_txt:
    for line in config_txt:
      if (ignore_command(line, ignore)) != True and not '!' in line:   #Function call ignore_command (line 3)
        if not line.startswith(' '):
          glob_comm = line.strip('\n')
          subcom_list = []
          subcom_in_subcom = []
          conf_dict[glob_comm] = subcom_list
        elif not line.startswith('  '):
          subcom = line.strip('\n')
          subcom_list.append(line.strip('\n'))
        else:
          conf_dict[glob_comm] = {}
          subcom_in_subcom.append(line.strip('\n'))
          conf_dict[glob_comm][subcom] = subcom_in_subcom
  return(conf_dict)

ignore = ['duplex' 'alias', 'Current configuration']

print(config_to_dict('r1_config.txt'))
