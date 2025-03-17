pizza=input("What type of pizza you wont (small/medium/large):")

bill=0
if pizza == 'small':
    bill = 300
    print(f"small pizza price is {bill} Rs")
elif pizza == 'medium':
    bill = 500
    print(f'medium pizza price is {bill} Rs')
elif pizza == 'large':
    bill = 700
    print(f'large pizza price is {bill} Rs')
add_peperoni=input("Do you wont peperoni (yes / on ):")
if add_peperoni == 'yes':
    if pizza == 'small':
        bill += 50
        print("peperoni price for small pizza is 50 Rs ")
    else:
        bill += 100
        print("peperoni price for medium and large  pizza is 100 Rs ")
extra_chees=input("Do you wont extra chees (yes / on ):")
if extra_chees == 'yes':
    bill+=50
    print("extra_chees price for all pizzas is 50 Rs ")
print(f"your total bill is {bill}")
