a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []
for i in a:
    if i % 2 == 0:
        b.append(i)

# print(b)

# #------ one line ---------

# print([i for i in a if i % 2 == 0])

b = [i for i in a if i % 2 == 0]
print(b)
