num = int(input('Enter a number: '))
mylist = []

for i in range(1, num + 1):
    if num % i == 0:
        mylist.append(i)

print(mylist)
