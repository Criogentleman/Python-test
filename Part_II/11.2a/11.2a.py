from file_as_str import file_as_str
from parse_cdp_neighbors import parse_cdp_neighbors
from draw_network_graph import draw_topology

SW1 = parse_cdp_neighbors(file_as_str('sh_cdp_n_sw1.txt'))
R1 = parse_cdp_neighbors(file_as_str('sh_cdp_n_r1.txt'))
R2 = parse_cdp_neighbors(file_as_str('sh_cdp_n_r2.txt'))
R3 = parse_cdp_neighbors(file_as_str('sh_cdp_n_r3.txt'))
SW1.update(R1)
SW1.update(R2)
SW1.update(R3)

result = {}
for key, value in SW1.items():
    if value not in result.values():
        result[value] = key

draw_topology(result)
