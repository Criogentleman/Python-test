#5 Список VLANS это список VLANов, собранных со всех устройств сети, поэтому в списке есть повторяющиеся номера VLAN. Из списка нужно получить уникальный список VLANов, отсортированный по возрастанию номеров.
VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
vlans_set = set(VLANS)
vlans_list = list(vlans_set)
vlans_list.sort()
print (vlans_list)
