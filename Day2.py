# Lists
list_num = [1,2,3,4,5,6]
print(list_num)

list_mixed = [1,2.2,'Hi']
print(list_mixed)
print(list_mixed[1])
print(list_num[1:4])
print(list_num[1:6:2])
print(list_num[1::2])

list_1 = [1,2,3]
list_2 = [4,5,6]
list_3 = list_1+list_2
print(list_3)

list_4 = ["Hi","My","name","is","Raahul N"]
list_4[4] = "Ram"
print(list_4)

list_1.append(4)
print(list_1)
list_1.pop()
print(list_1)
list_1.pop(2)
print(list_1)

list_sort = [4,9,1,6,3,8,2,1]
print(list_sort)
list_sort.sort()
print(list_sort)
# list_new = list_sort.sort()
list_new = list_sort
print(list_new)

print(len(list_sort))
print(len(list_4))
list_sort.reverse()
print(list_sort)

# Dictionaries
my_dict = {'name':'Raahul N','age':'22','designation':'intern'}
print(my_dict)

scores = {'raj':'20','priya':'30','ram':'40'}
print(scores['ram'])
scores['kumar'] = 50
print(scores)
scores['raj']=60
print(scores)
print(scores.keys())
print(scores.values())
print(scores.items())

dict_new = {'name':'raj','score':[20,40,60,80]}
print(dict_new['score'])
print(dict_new['score'][3])

# Tuple - immutable
tuple_1 = (1,2,3)
print(tuple_1)
# tuple_1 = (1,2,3)
# tuple_1[0]=0
# print(tuple_1)
print(tuple_1[0])
print(tuple_1[0:])
print(tuple_1[0:2])

tuple_2 = (1,1,1,2,3,6,7,4,0,1,2)
print(tuple_2.count(1))
print(tuple_2.index(2))

tuple_3 = ('sam','dam','fan')
print(tuple_3.index('dam'))

tuple_mixed = (1,'Hi',3.2)
print(tuple_mixed)

# Sets
set_new = {'hello','how','are','you'}
print(set_new)

set_new1 = {'hello','how','how','how'}
print(set_new1)

list_1 = [1,1,1,2,3,3,4,4,8,8,9]
print(set(list_1))

set_num = {1,2,3,4,5}
set_num.add(6)
print(set_num)
set_num.add(1)
print(set_num)

#Boolean
print(1>2)
print(5>1)

a = 50
b = 20
print(a<b)
print(a>=b)
print(a<=b)

c = 'hello'
d = 'hello'
print(c==d)
print(c!=d)

print(9>5>2)
print(5>1 and 1<0)
print(5>1 or 1<0)
print(not 1<0)

# Control Flow
if 1 < 0:
    print('the codition is true')
else:
    print('the condition is false')

name = 'ram'
if name == 'pam':
    print('login as ram')
elif name == 'sam':
    print("login as sam")
else:
    print("check the user")

x = 0
while x<10:
    print(x)
    x = x + 1
else:
    print("the condition is false")