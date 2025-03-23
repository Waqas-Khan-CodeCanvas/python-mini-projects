import random

secissor = '''
    _____
----` ____)___
        _______)
      __________)
      (_____)
----__(____)
'''
rock='''
     ______  
----`   ____)
         ____)
        ____)  
----______)
'''

paper='''
      _____
----- _____)___
       _________)_
       ___________)
       _________)
-----_______)                
'''

images=[rock,paper,secissor]
user_choice=int(input("Enter your choice "))
if user_choice >=3 or user_choice <0:
    print("you entered worng number you lose")
else:
    print(f"user choice is {user_choice}")
    print(images[user_choice])
    computer_choice=random.randint(0,2)
    print(f"computer choice is {computer_choice}")
    print(images[computer_choice])
    score=0
    # print(score)
    if user_choice == computer_choice:
        print("Both are equall")
        print("its drow ")
        # print("its drow")

    elif user_choice ==1 and computer_choice == 0:
        score +=1
        print("paper wins against rock")
        print("you win")

    elif user_choice ==2 and computer_choice == 0:
        print("Secissor lose against rock")
        print("you lose")

    elif user_choice == 0 and computer_choice == 1:
        print("paper wins against rock")
        print("you lose")

    elif user_choice ==2  and computer_choice ==1 :
        score += 1
        print("Secissor wins against paper")
        print("you win")

    elif user_choice == 0 and computer_choice == 2:
        score += 1
        print(" rock wins against Secissor")
        print("you win")

    elif user_choice ==1 and computer_choice == 2:
        print(" paper lose against Secissor")
        print("you lose")
    print(f"your score is {score}")
