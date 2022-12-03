# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# counter = 0
# c = []
# for i in a:
#     for j in b:
#         if i == j:
#             c.append(i)
#
# c = set(c)
# print(c)
#

# #---- random lists --------
# import random
#
# a = random.sample(range(20), 10)
# a = sorted(a)
#
# b = random.sample(range(20), 12)
# b = sorted(b)
#
# c = []
# for i in a:
#     for j in b:
#         if i == j:
#             c.append(i)
#
# print(f'list a = {a}')
# print(f'list b = {b}')
# c = set(c)
# print(f'Common = {c}')
