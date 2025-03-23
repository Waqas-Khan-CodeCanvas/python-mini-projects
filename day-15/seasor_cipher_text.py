#
#
#
# count=1
# while count <= 5:
#     print(count)
#     count +=1
#
# count=6
# while count > 0:
#     print(count)
#     count -= 1
#
#
# list=[1,2,3,4,5,6,7,8,9]
# while list:
#     print("hello how are you")
#     list.pop()
#     print(list)
#
# name="zaryab"
# count=0
# while count <10:
#     print(name)
#     count+=1
#     print(count)
#
# stope=input("Enter 1 for exit:")
# while stope != "1":
#     stope=input("Enter 1 for exit:")
#
#
# number=1
# while number < 50:
#     print(number)
#     number +=1
#     if number == 30:
#        print("Thirty")
#
# else:
#     print(" now in else block")
# print("out of loop")
#
#

# number=int(input("Enter a number that you want to add (-1 for quit): "))
# print(number)
# sum=0
# while number != -1:
#     sum+=number
#
#     number = int(input("Enter a number that you want to add (-1 for quit): "))
#     print(number)
#
# print(sum)

# number=0
# while number < 10:
#     print(number)
#     number += 1
#     if number == 5:
#         break
#
#
# print("out side of loop")

# number = 0
# while number < 20:
#     print(number)
#     number += 1
#     if number == 17:
#         break

# list=["hello","hi","welcome"]
# names=["alikhan","ahsan","zaryab"]
# for greet in list:
#     for name in names:
#         print(greet,name)

# name={
#     "ahsan":345673456,
#     "hello":387654234,
#     "hi":346789212,
# }
# name["hello"]={"hello_phone":34567,"hello_home":7654}
# print(name["hello"])
#
# data={
#     "ahsan":56789,
#     "zaryab":876557,
#     "hasham":86546,
# }
# # del data["zaryab"]
# # print(data)
# # data.pop("zaryab")
# # print(data.pop.items())
# # data.clear()
# print(data.keys())
# print(data.values())
# print(data.items())
# print(data)
# for i in data:
#     print(i)
#     # print(data[i])
# data2=data.copy()
# print(data2)
# print(len(data))

#
# stutends_marks={
#     "waqas":90,
#     "zaryab":60,
#     "ahsan":70,
#     "hasham":80,
#     "sajid":78,
#     "alam":56,
#     "hasnian":40,
#     "hafeez":98,
#
#
# }
# students_grade={}
# for students in stutends_marks:
#     marks=stutends_marks[students]
#     if marks>90:
#         students_grade[students]="A+"
#     elif marks>80:
#         students_grade[students]="A"
#     elif marks>70:
#         students_grade[students]="B+"
#     elif marks>60:
#         students_grade[students]="B"
#     elif marks>50:
#         print(students_grade)
#         students_grade[students]="C"
#     elif marks>40:
#         students_grade[students]="D"
#     else:
#         students_grade[students]="F"

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption(plain_text,shift_key):
    cipher_text=""
    for char in plain_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position+shift_key)%26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"here is the text after encryption : {cipher_text}")
def decryption(cipher_text,shift_key):
    plain_text=""
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position=(position-shift_key)%26
            plain_text += alphabet[new_position]
        else:
            plain_text += char
    print(f"here is the text after decryption : {plain_text}")

wanna_end=True
while wanna_end:
    what_to_do=input("type 'encrypt' for encryption or 'decrypt' for decryption :")
    if what_to_do == 'encrypt':
        text=input("type your message here: ")
        shift=int(input("enter your shift ket here :"))
        encryption(plain_text=text,shift_key=shift)
    elif what_to_do == "decrypt":
        text = input("type your message here: ")
        shift = int(input("enter your shift ket here :"))
        decryption(cipher_text=text, shift_key=shift)
    want_continue=input("do you want to continue ('yes' or 'no' ) ")
    if want_continue == "no":
        print("good luck have a nice a day....")
        wanna_end=False
