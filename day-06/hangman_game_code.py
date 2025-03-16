import random

stages=['''

   +------+
   |      |
   0      |
  /|\     |
  / \     |
          |
===========  ''','''
   +------+
   |      |
   0      |
  /|\     |
  /       |
          |
=========== ''','''
   +------+
   |      |
   0      |
  /|\     |
          |
          |
=========== ''','''
   +------+
   |      |
   0      |
  /|      |
          |
          |
=========== ''','''
   +------+
   |      |
   0      |
   |      |
          |
          |
=========== ''','''
   +------+
   |      |
   0      |
          |
          |
          |
=========== ''','''
   +------+
   |      |
          |
          |
          |
          |
=========== '''
]
list=["hello","how","now","are",'soon']

chosen_word=random.choice(list)
print(chosen_word)

blanks=[]
for blank in chosen_word:
    blanks += "_"
print(blanks)


lives=6
game_over=True

while game_over:
    guessed_letter=input("Gues a letter  for the above blanks :")
    for location in range(len(chosen_word)):
        letter=chosen_word[location]
        if guessed_letter == letter:
            blanks[location]=letter
    print(blanks)
    if guessed_letter not in chosen_word:
        lives-=1
        if lives == 0:
            print("you lose the game sham on you")
            game_over=False
    if "_" not in blanks:
        print("you won the game good luck")
        game_over=False

    print(stages[lives])
print('game over')