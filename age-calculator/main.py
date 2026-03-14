age=int(input("Enter your age :"))

new_age=age

years=new_age
months=new_age*12
weeks=new_age*52
days=new_age*365

print(f"you have spent {years} years")
print(f"you have spent {months} months")
print(f"you have spent {weeks} weeks")
print(f"you have spent {days} days")

if new_age<=12:
    print("you are child ")
    print("Enjoy you are a childhood")
elif new_age<=20:
    print("you are adult ")
    print("foucs on study and be careful you are in a teen age :    ")
elif new_age<=30:
    print("you are young  ")
    print("be careful about your job and earing  ")
elif new_age<=40:
    print("you are a man ")
    print("be responsible and be careful  about your family ")
elif new_age<=60:
    print("you are old ")
    print("you are old so be careful about your hereafter life \n "
          "Allah says in Quran , 'The hereafter is better for you than the present life of this world'  ")
else:
    print("you are about to die")



