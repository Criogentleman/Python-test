'''5.4 Найти индекс последнего вхождения элемента.
Например, для списка num_list, число 10 последний раз встречается с индексом 4; в списке word_list, слово 'ruby' последний раз встречается с индексом 6.

Сделать решение общим (то есть, не привязываться к конкретному элементу в конкретном списке) и проверить на двух списках, которые указаны и на разных элементах.

Для этого надо запросить у пользователя сначала ввод числа из списка num_list и затем вывести индекс его последнего появления в списке. А затем аналогично для списка word_list.
'''

num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
num_list.reverse()
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']
word_list.reverse()

INPUT_NUM = input('Enter num:')
num_list = num_list.index(int(INPUT_NUM)) + 1
NUM_INDEX = 10 - num_list #10 - число элементов в списке, посчитаное вручную, можно использовать 'len', но о нем еще не было никакой информации
print (NUM_INDEX)

INPUT_WORD = input ('Enter word now:')
word_list = word_list.index((INPUT_WORD)) + 1
NUM_WORD = 8 - word_list
print (NUM_WORD)
