import random

dice1 = 0
dice2 = 0

faces = [ 1, 2, 3, 4, 5, 6,
          1, 2, 3, 4, 5, 6 ]

print("welcome to dice simulator! ")
alegere = input("do you want to roll the dices?  y/n ")

def reset():
    faces = [ 1, 2, 3, 4, 5, 6,
          1, 2, 3, 4, 5, 6 ]
    return faces

def popit():
    dice1 = 0
    dice2 = 0
    faces = reset()
    random.shuffle(faces)
    face = faces.pop()
    dice1 = dice1 + face
    random.shuffle(faces)
    face2 = faces.pop()
    dice2 = dice2 + face2
    print(dice1, dice2)

while alegere != "q":
    popit()
    alegere = input("do you want to roll again?  y/n ")
    if alegere == "y":
        reset()
    if alegere == "n":
        print("ok, bye!")
        exit()


