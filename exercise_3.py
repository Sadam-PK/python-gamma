a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []
new_list2 = []

for i in a:
    if i < 5:
        print(i)

# #--- add to new list and print ------

for i in a:
    if i < 5:
        new_list.append(i)

print(new_list)

# #--- single line ------

print([i for i in a if i < 5])

# #--- ask for number ------

num = int(input('Enter a number: '))

for i in a:
    if i < num:
        print(i)
