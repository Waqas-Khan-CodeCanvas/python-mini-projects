greeting = 'Hello'
greeting += ' world!'
print(greeting)
# 'Hello world!'

number = 1
number += 1
print(number)
# 2

my_list = ['item']
my_list *= 3
print(my_list)
# ['item', 'item', 'item']

# Walrus Operator
print(my_var:="Hello World!")
# 'Hello world!'

my_var="Yes"
print(my_var)
# 'Yes'

print(my_var:="Hello")
# 'Hello'


# The end keyword
phrase = ['printed', 'with', 'a', 'dash', 'in', 'between']
for word in phrase:
    print(word, end='-')
print()    

# printed-with-a-dash-in-between-


# The sep keyword
print('cats', 'dogs', 'mice', sep=',')
print('cats', 'dogs', 'mice')
# cats,dogs,mice


# The input() Function
print('What is your name?')   # ask for their name
my_name = input()
print('Hi, {}'.format(my_name))
print(f"Hi, {my_name}")
# What is your name?
# Martha
# Hi, Martha



# The len() Function
my_list = ['asafda', 'badsfs', 'cafds']
print(len(my_list))


# The str(), int(), and float() Functions
print(str("4"))
print(int("4"))
print(float("4.0")) 
# The type() Function
print(type("4"))    