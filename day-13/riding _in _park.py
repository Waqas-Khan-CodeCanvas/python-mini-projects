height=int(input("Enter your height here: "))
bill=0
if height>=4:
    print("you can ride ")
    print(f"this height {height} good is fit for riding ")
    age=int(input("Enter your age here: "))
    if age <=12:
        bill=200
        print(f'your ticket price is {bill} ')
    elif age <=18:
        bill = 300
        print(f'your ticket price is {bill} ')
    else:
        bill = 500
        print(f'your ticket price is {bill} ')
    photo=input("You wont to take photo during ride (yes / no):")
    if photo == 'yes':
        bill+=50
        print(f"phot price is 50 Rs")
    print(f"your total bill is {bill}")
    print("thanks Enjoy... your ride")
else:
    print("you can't ride")
    print(f" sorry this height {height} feet is not good for riding ")
print("bye")