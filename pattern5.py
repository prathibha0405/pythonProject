for i in range(5):
    for j in range(5):
        if i+j==2 or i-j==2 or i+j==6 or j-i==2:
            print("*",end=" ")
        else:
            print(end=" ")
    print()
#Number pattern programs
def pattern(n):
    x=0
    for i in range(0,n):
        for j in range(0,i+1):
            print(x,end=" ")
            x=x+1
        print("\r")
pattern(int(input()))
#2
def pattern(n):
    k=2*n-2
    x=0
    for i in range(0,n):
        x=x+1
        for j in range(0,k):
            print(end=" ")
        k=k-2
        for j in range(0,i+1):
            print(x,end=" ")
        print("\r")
pattern(int(input()))
#3
def pattern(n):
    k=2*n-2
    x=0
    for i in range(n,-1,-1):
        x=x+1
        for j in range(k,0,-1):
            print(end=" ")
        k=k+2
        for j in range(0,i):
            print(x,end=" ")
        print("\r")
pattern(int(input()))