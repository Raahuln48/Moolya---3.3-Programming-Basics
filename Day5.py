# Tuple unpacking with functions
stock_prices = [('Tata',500),('HDFC',1000),('Maruti',200)]
for stock_name,price in stock_prices:
    print(price)

working_hours = [('Sam',10000),('Tom',4000),('Pam',300)]
def employee_max(working_hours):
    current_max_hours = 0
    employee_name = ''

    for employee,hours in working_hours:
        if hours > current_max_hours:
            current_max_hours = hours
            employee_name = employee

    return (employee_name,current_max_hours)

print(employee_max(working_hours))

employee,hours = employee_max(working_hours)
print(employee)

# *args and *kwargs

def sum_num(a,b,c=0,d=0):
    return sum((a,b,c,d))

print(sum_num(10,20,30,40))
print(sum_num(10,20))

def sum_num(*args):
    print(args)
    return sum(args)

print(sum_num(10,20,30,40))
print(sum_num(10,20))

def kw_example(**kwargs):
    if 'food' in kwargs:
        print(kwargs['food'])
    else:
        print('No food in the list')

kw_example(fruit = 'orange', food = 'potato')
kw_example(fruit = 'orange', vegetable = 'potato')
kw_example(fruit = 'orange', vegetable = 'potato',snack = 'chips')

print('food' in {'fruit':'orange', 'food':'potato'})
print('food' in {'fruit':'orange', 'vegetable':'potato'})

# Three cup monte game

# list of cups
list_cups = ['','0','']

from random import shuffle
result = shuffle(list_cups)

print(result)
# shuffle the cup
def shuffle_list(list_cups):
    shuffle(list_cups)
    return list_cups

result = shuffle(list_cups)
print(result)

# ask the guess
def get_guess():
    guess = ''
    guess = input("Pick the cup 0,1 or 2")
    return int(guess)

guess = get_guess()

def check_guess(list_cups,guess):
    if list_cups[guess] == '0':
        print("Correct guess")
        print(list_cups)
    else:
        print("Wrong guess")
        print(list_cups)

check_guess(list_cups,guess)
print(list_cups)
result = shuffle_list(list_cups)
guess = get_guess()
check_guess(result,guess)
print(result)

# Lambda expression
# map(function,iterables)
mylist = [1,2,3,4,5]
def square(num):
    return num**2
result = square(2)
print(result)

for item in map(square,mylist):
    print(item)

print(list(map(square,mylist)))

list_string = ['Potato','Orange','Chips']
def even_odd_check(string):
    if len(string)%2 == 0:
        return 'even'
    else:
        return 'odd'
# even_check('carrot')

print(list(map(even_odd_check,list_string)))

# Filter
mylist = [1,2,3,4,5,6]
def even_odd_check(num):
    return num%2==0

print(list(filter(even_odd_check,mylist)))

square = lambda num: num**2
print(square(10))

print(list(map(lambda num:num**2,mylist)))
print((lambda num:num**2)(10))

print(list(filter(lambda num: num%2 == 0,mylist)))