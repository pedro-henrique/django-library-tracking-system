import random
rand_list = [random.randint(1, 20) for _ in range(10)]
print('rand_list: ', rand_list)

list_comprehension_below_10 = [n for n in rand_list if n < 10]
print('list_comprehension_below_10: ', list_comprehension_below_10)

list_comprehension_below_10_filter = list(filter(lambda x: x < 10, rand_list))
print('list_comprehension_below_10_filter: ', list_comprehension_below_10_filter)