print("Hello")

print(2+2)
print(2/2)
print(2*2)
print(2%2)

print(2**10)
print(2+2*40)
print((2+2)*5)
print((2+2)+(50*60))

a = 50
b = 120
sum = a + b
print(sum)

first_name = "Raahul"
last_name = "N"
print(first_name+" "+last_name)

# type(a)
# type(first_name)

my_salary = 10000
tax_percentage = 0.2
taxes = my_salary * tax_percentage
print(taxes)

name = "Nicky"
update = name[1:5]
updated_name = "M" + update
print(updated_name)

update1 = name[0:5]
updated_name1 = "Mr. " + update1
print(updated_name1)

str1 = "Hello"
str2 = "Hi"
str3 = str1[0] + str2[1]
print(str3)

str4 = "Hi, What is your name"
str5 = str4[:3] +" My "+ str4[17:21] +" "+ str4[9:11] +" "+ "Raahul N "
print(str5)
print(str5[0:21:2])
print(str5*5)

print(updated_name1.upper())
print(updated_name1.lower())

print(str4.split())
print(str4.split('a'))

place = 'Bangalore'
college = 'BMSIT&M'
print(str5+f'I am from {place}, Graduated from {college}')
