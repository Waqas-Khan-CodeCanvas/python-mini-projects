import random

name=input("Enter everybody's name:")
list=name.split(" ")
print(list)
lenght=len(list)
index=random.randint(0,lenght-1)
print(f"{list[index]} will pay the bill")