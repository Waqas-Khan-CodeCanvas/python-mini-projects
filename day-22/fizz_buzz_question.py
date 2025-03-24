'''
if number is divisible  by 3 it would print fizz
if number is divisible  by 5 it would print buzz
if number is divisible  by 3 and 5 both it would print fizzbuzz
'''

for number in range(1,101):
    if number%3==0 and number%5==0:
        print("FizzBuzz")
    elif number%5==0:
        print("Buzz")
    elif number%3==0:
        print("Fizz")
    else:
        print(number)