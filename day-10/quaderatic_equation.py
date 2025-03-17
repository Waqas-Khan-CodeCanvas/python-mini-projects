import cmath

print("General form of quarderatic  equation is ax**2 + bx + c = 0 ")


a=int(input("Enter the value of a ( a!=0 ): "))
b=int(input("Enter the value of b : "))
c=int(input("Enter the value of c : "))

print(f"result for the equation is {a}x**2 + {b}x + {c} = 0")
d=(b**2)-(4*a*c)
# print(d)
# 1

sol1=(-b+cmath.sqrt(d)/(2*a))
# print(sol1)
sol2=(-b-cmath.sqrt(d)/(2*a))
# print(sol2)

print(f"the solution are {sol1} and {sol2}")



