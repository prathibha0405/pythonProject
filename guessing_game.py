import random as r
#imported the random module
num=r.randrange(200)
guess=int(input())
while guess>=0:
    your_guess=int(input("enter your guess:"))
    def check(x):
        if your_guess==x:
            print("You won")

        elif your_guess>x:
            print("You are close,keep trying lower")
        else:
            print("your are close,keep trying higher")
    if guess>1:
        check(num)
    elif guess==1:
        check(num)
        print("this is your last chance,make the most of it,good luck!")
    else:
        print("you lost")
    guess=guess-1
