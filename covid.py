print(input("Enter your name:"))
print(input("enter your age:"))
print("Are you suffering from any symptoms:")
a=input()
if a=="YES":
    print("What are the symptoms?")
    b=input()
    if b=="Cough and Cold":
        print("Is there any other symptoms?")
        c=input()
        if c=="ThroatInfection and Fever":
            print("Covid Positive!!\nHence self quarantine and eat proper healthy food!!\nwear the mask which is recommended by WHO!!\nTake proper Medication!!")
    elif b=="Cough" or b=="Cold":
        print("you are suffering from cough or cold!\nIt\'s better consult doctor for your good health.")
    elif b=="fever" or b=="Throat Infection":
        print("Do Covid-19 Test and Take proper precautions.")
    else:
        print("You are covid free\nbut wear your mask for your good sake.")
else:
    print("you are covid free!\nStay Safe and Stay healthy!!")