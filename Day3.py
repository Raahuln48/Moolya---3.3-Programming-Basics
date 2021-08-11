list_num = [1,2,3,4,5]
for item in list_num:
    print(item)
    # print('the items are listed')
print('the items are listed')

list_num = [1,2,3]
for _ in list_num:
    print('hello')

my_num = [1,2,3,4,5,6,7,8]
for num in my_num:
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')

my_num = [1,2,3,4,5,6]
sum_num = 0

for num in my_num:
    sum_num = sum_num + 4

print(sum_num)

my_num = [1,2,3,4,5,6]
sum_num = 0

for num in my_num:
    sum_num = sum_num + num

print(sum_num)

my_msg = 'hello world'
for i in my_msg:
    print('hi')
print(len(my_msg))

# Tuple unpacking
tup_num = (1,2,3)

for item in tup_num:
    print(item)

list_tup = [(1,2),(3,4),(5,6)]
for item in list_tup:
    print(item)

list_tup = [('a','b'),('c','d'),('e','f')]
for item in list_tup:
    print(item)

for a,b in list_tup:
    print(a)
    print(b)

list_tup = [(1,2,3),(4,5,6)]
for item in list_tup:
    print(item)

for a,b,c in list_tup:
    # print(a)
    print(b)
    # print(c)

dict_val = {'key1':1, 'key2':2}
for item in dict_val.items():
    print(item)

for key,value in dict_val.items():
    print(key)
    print(value)

for x in dict_val.values():
    print(x)

for x in dict_val.keys():
    print(x)

# break continue pass

x=[1,2,3]

for num in x:
    print(num)

for num in x:
    # print(num)
    pass
#
x=[1,2,3,4,5,6,7,8]

for num in x:
    if num == 4:
        continue
    print(num)
#
list_emp = ['sam','dam','fan']
for i in list_emp:
    if i == 'sam':
        print("salary not credited")
        continue
    print("credit salary")

x=[1,2,3,4,5,6,7,8]

for num in x:
    if num == 4:
        break
    print(num)
print('Outside the for loop')

# break in while loop
n=0
while(n<5):
    print(n)
    n=n+1
#
my_list_num = [0,1,2,3,4,5,6]
for num in my_list_num:
    print(num)

# Range
for num in range(1,21):
    print(num)

for num in range(0,200,20):
    print(num)

print(list(range(0,11,3)))

# Enumerate

string_msg = 'hello'
for char in string_msg:
    print(char)
#
string_msg = 'hello'
index_count=0
for char in string_msg:
    print(f'at index {index_count} is {char}')
    index_count = index_count + 1

string_msg = 'hello'
for char in enumerate(string_msg):
    print(char)
# tuple unpacking
string_msg = 'hello'
for index,char in enumerate(string_msg):
    print(index)
    print(char)

for a,b in enumerate(string_msg):
    if(a==0):
        print("the letter in first index is h")
    else:
        print(a)

mylist = [1,2,3,4]
for a,b in enumerate(mylist):
    if(a==1):
        mylist.pop(a)
print(mylist)

mylist_1 = ['sam','dam','fan','tom']
mylist_2 = [10,20,30]
mylist_3 = [80,100,50]

for item in zip(mylist_1,mylist_2,mylist_3):
    print(item)

for a,b,c in zip(mylist_1,mylist_2,mylist_3):
    print(b)

# in operator
print(1 in [1,2,3])
print('x' in ['x','y','z'])
print('key1' in {'key1':1,'key2':2})

# min function
list_num = [50,60,90,10,20]
print(min(list_num))

# random library

from random import shuffle
mylist = [1,2,3,4,5,6,7,8,9]
shuffle(mylist)
print(mylist)

# generate a random number using random module
from random import randint
print(randint(1,100))

from random import randint
randomname = randint(1,100)
print(randomname)

# input function
weather = input("what is the weather")

if weather == 'sunny':
    print('weather is sunny')
elif weather == 'rainy':
    print("weather is rainy")