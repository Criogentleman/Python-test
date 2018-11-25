from file_as_str import file_as_str

def parse_cdp_neighbors(sh_cdp_string):
    cdp_dict = {}
    for i in (sh_cdp_string.split('\n')[6:]):
        iface_list = i.split()
        cdp_dict['SW1', iface_list[2]] = (iface_list[0], iface_list[-1])
    return(cdp_dict)

(parse_cdp_neighbors(file_as_str('sw1_sh_cdp_neighbors.txt'))) #file_as_str - return file text as single string
