import datetime
name = input('Enter Name: ')
age = int(input('Enter Age: '))
rem = 100 - age
year = datetime.date.today().year
toBe100 = year + rem
print(f'Hello {name}, you will turn 100 years old in {toBe100}')
