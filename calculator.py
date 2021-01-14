import math
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def mod(x,y):
    return x%y
def pow(x,y):
    return x**y
def floordiv(x,y):
    return x//y
def sqrt(x):
    return math.sqrt(x)
def sin(x):
    return math.sin(x)
def cos(x):
    return math.cos(x)
def tan(x):
    return math.tan(x)
print("Select Operation")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.ModuloDivision")
print("6.Power")
print("7.Floordivision")
print("8.Squareroot")
print("9.sine function")
print("10Cosine function")
print("11.Tangent function")
while True:
    choice=input("Enter (1/2/3/4/5/6/7/8/9/10/11):")
    if choice in ("1","2","3","4","5","6","7","8","9","10","11"):
        a=float(input("enter 1st number:"))
        b=float(input("enter 2nd number:"))
        if choice=="1":
            print("sum of a and b is",add(a,b))
        elif choice=="2":
            print("subtraction of a and b is",sub(a,b))
        elif choice=="3":
            print("Multiplication of a and b is",mul(a,b))
        elif choice=="4":
            print("Division of a and b is",div(a,b))
        elif choice=="5":
            print("Modulodivision of a and b is",mod(a,b))
        elif choice=="6":
            print("power of a and b is ",pow(a,b))
        elif choice=="7":
            print("Floordivision of a and b is",floordiv(a,b))
        elif choice=="8":
            print("Squareroot of a  is",sqrt(a))
            print("Squareroot of b is ",sqrt(b))
        elif choice=="9":
            print("Sine of a is ",sin(a))
            print("sine of b is",sin(b))
        elif choice=="10":
            print("cosine of a is ",cos(a))
        elif choice=="11":
            print("Tangent of a is ",tan(a))
            print("Tangent of b is",tan(b))


            break
    else:
        print("Invalid option")