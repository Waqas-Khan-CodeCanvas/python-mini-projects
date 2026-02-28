# Python Control Flow
    # Comparison Operators
    # Boolean Operators
    # Mixing Operators
    # if Statements
name = 'Antony'

if name == 'Debora':
   print('Hi Debora!')
elif name == 'George':
    print('Hi George!')
else:
    print('Who are you?')
# Who are you?    
    
    
# Ternary Conditional Operator
# <expression1> if <condition> else <expression2>
# Example:
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult

fnd = "zari"
result = "yah it's zari" if fnd == "zari" else "no i don't know who is he"
print(result)

age = 9
print("kid" if age < 18 else "adult" if age > 13 else "teen")


# Switch-Case Statement
# Matching single values
response_code = 201
match response_code:
     case 200:
         print("OK")
     case 201:
         print("Created")
     case 300:
         print("Multiple Choices")
     case 307:
         print("Temporary Redirect")
     case 404:
         print("404 Not Found")
     case 500:
         print("Internal Server Error")
     case 502:
         print("502 Bad Gateway")
# Created


# Matching with the or Pattern
response_code = 502
match response_code:
     case 200 | 201:
         print("OK")
     case 300 | 307:
         print("Redirect")
     case 400 | 401:
         print("Bad Request")
     case 500 | 502:
         print("Internal Server Error")

# Internal Server Error


# Matching by the length of an Iterable
# Default value
# Matching Builtin Classes
# Guarding Match-Case Statements



# while Loop Statements
spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1

# Hello, world.
# Hello, world.
# Hello, world.
# Hello, world.
# Hello, world.


# break Statements
while True:
     name = input('Please type your name: ')
     if name == 'your name':
         break

print('Thank you!')
# Please type your name: your name
# Thank you!

# continue Statements
while True:
    name = input('Who are you? ')
    if name != 'Joe':
        continue
    password = input('Password? (It is a fish.): ')
    if password == 'swordfish':
        break

print('Access granted.')
# Who are you? Charles
# Who are you? Debora
# Who are you? Joe
# Password? (It is a fish.): swordfish
# Access granted.




# For loop
# The for loop iterates over a list, tuple, dictionary, set or string:

pets = ['Bella', 'Milo', 'Loki']
for pet in pets:
    print(pet)

# Bella
# Milo
# Loki


# The range() function
# The range() function returns a sequence of numbers. It starts from 0, increments by 1, and stops before a specified number:

for i in range(5):
    print(f'Will stop at 5! or 4? ({i})')

# Will stop at 5! or 4? (0)
# Will stop at 5! or 4? (1)
# Will stop at 5! or 4? (2)
# Will stop at 5! or 4? (3)
# Will stop at 5! or 4? (4)


# range(start, stop, step)
for i in range(0, 10, 2):
   print(i)

# 0
# 2
# 4
# 6
# 8


for i in range(5, -1, -1):
    print(i)

# 5
# 4
# 3
# 2
# 1
# 0