import random
a = random.randint(1,3)
a = input("Welcome to the game : ")
u_i = input("Enter any of the following : \nRock\nPaper\nScissirs")
u_i = u_i.upper()

if u_i == 'ROCK' and a==1 or a==2:
    print("You win ")
elif u_i=='PAPER' and a==2:
    print("you win")
elif u_i == 'SCISSORS' and a == 3:
    print("you win")
else:
    print("you fail")

