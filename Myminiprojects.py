#Finding Random Number in DICE
import random
while True:
    choice=input("1.enter your choice 2.exit")
    if choice in ("1","2"):
        if choice=="1":
            print(random.randint(1,6))
        else:
            print("incorrect choice")
