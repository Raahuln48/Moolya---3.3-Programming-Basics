# using range function
for num in range(0,11):
    print(num)

# using slicing
my_list  = ['a','b','c','d','e','f','g']
for char in my_list[0::2]:
    print(char)

my_list  = ['a','b','c','d','e','f','g']
index_count = 0
for char in my_list[0::2]:
    print(f'At index {index_count} is {char}')
    index_count = index_count+2

# list comprehension
my_msg = 'bye'
my_list = []

for char in my_msg:
    my_list.append(char)
print(my_list)

my_list1 = []
my_list = [char for char in my_msg]
print(my_list)

my_name = 'raahul'
my_nameaslist = [char for char in my_name]
print(my_nameaslist)

for num in range(0,11):
    print(num**2)

my_squares = [num**2 for num in range(0,11)]
print(my_squares)

my_squares = [num**5 for num in range(20,50)]
print(my_squares)

for num in range(0,11):
    if num % 2 == 0:
        print(num)

my_evenlist = [num for num in range(0,11) if num % 2 == 0]
print(my_evenlist)

for x in [1,2,3]:
    for y in [10,100,1000]:
        print(x*y)

my_nestedlist = [x*y for x in [1,2,3] for y in [10,100,1000]]
print(my_nestedlist)

my_nestedlist.append(9000)
print(my_nestedlist)

my_nestedlist.insert(3,40)
print(my_nestedlist)

my_nestedlist.remove(200)
print(my_nestedlist)

any_num = [5,2,9]
my_nestedlist.extend(any_num)
print(my_nestedlist)

my_nestedlist.clear()
print(my_nestedlist)

# functions
def name_of_function():
    print("hello world")
    print('hi')
    print('how')
    print('are')
    print('you')
name_of_function()

def print_name(name):
    print(f'Hello {name}')
print_name("Ram")

def sum_numbers(a,b):
    print(a+b)

def difference_numbers(x,y):
    print(x-y)

sum_numbers(2,5)
difference_numbers(10,2)

def sum_numbers(a,b):
    return (a+b)
num_1 = sum_numbers(50,10)
print(num_1)

def difference_numbers(x,y=10):
    print(x-y)
difference_numbers(50)
difference_numbers(50,30)

def is_even(num):
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')

is_even(10)
is_even(19)

def is_even_1(num):
    if num % 2 == 0:
        return True
    else:
        return False
    print("after return statement")

print(is_even_1(10))
print(is_even_1(19))


def check_even(num_list):
    for num in num_list:
        if num%2 == 0:
            return True
        else:
            pass
    return False

num_list = [1,3,5]
print(check_even(num_list))


num = [1,3,5,7,8,9,10]
for n in num:
    if n > 1:
        for i in range(2,n):
            if(n%i==0):
                print(f'{n} is not Prime number')
                break
            else:
                print(f'{n} is a Prime number')
                break
    else:
        print(f'{n} is not Prime number')
