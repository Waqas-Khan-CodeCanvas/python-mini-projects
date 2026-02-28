# Python Functions
# Function Arguments
# A function can take arguments and return values:
def say_hello(name):
   print(f'Hello {name}')

say_hello('Carlos')
# llo Carlos
say_hello('Wanda')
# llo Wanda
say_hello('Rose')
# Hello Rose


# Keyword Arguments
def say_hi(name, greeting):
   print(f"{greeting} {name}")

# without keyword arguments
say_hi('John', 'Hello')
# llo John
# with keyword arguments
say_hi(name='Anna', greeting='Hi')
# Hi Anna


# Return Values
def sum_two_numbers(number_1, number_2):
   return number_1 + number_2

result = sum_two_numbers(7, 8)
print(result)
# 15



# Local and Global Scope
# Lambda Functions