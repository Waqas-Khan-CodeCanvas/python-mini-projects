string=input("Enter your string here")
list=list(string)
print(list)
alphabets=""
number_alphabets=0
number=""
number_digits=0
symbols=""
number_symbols=0

for i in range(len(string)):
    if string[i].isalpha():
        number_alphabets += 1
        alphabets += list[i]
    elif string[i].isdigit():
        number_digits +=1
        number += list[i]
    else:
        number_symbols +=1
        symbols += list[i]
print("your string has ",number_alphabets,"number of alphabets and that alphabets are ",alphabets)
print("your string has ",number_digits,"number of alphabets and that alphabets are ",number)
print("your string has ",number_symbols,"number of alphabets and that alphabets are ",symbols)