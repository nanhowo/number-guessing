import random

print("******************************Da game***************************************")
print("Welcome to da shitty ass number guessing game, wth you decided to play this? \nNvm, you have 7 chances to guess, enter the range yourself, oge?\nLet's play")

chances = 7
guesscounter = 0

range = int(input("Enter range: "))
computer = random.randrange(range)

if range == 10:
    print("Why you so noob?")
elif range > 10:
    print("Aint no way! This nigga is fire tho!!!")
else:
    print("Gay ass nigga!")
while guesscounter < chances:
    guesscounter = guesscounter + 1
    player = int(input("Nvm! Enter your guess: "))

    if guesscounter > 1:
        a = "chances"
    else:
        a = "chance"
    if player == computer:
        print(f"You're correct nigga! The number is {computer}, you wasted {guesscounter} {a}! Enjoy your free Vbuck, loser!")
        break
    elif guesscounter >= chances:
        print(f"The number is {computer}!\nHahaha! You're so bad! That's why you pull no bitches!")
    elif player < computer:
        print("Your guessed is too small")
    elif player > computer:
        print("Your guessed is too big")