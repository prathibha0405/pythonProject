#RightAngle Triangle
def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end=" ")
        print("\r")
pattern(int(input()))

#Left Angle Triangle
def pattern(n):
    k=2*n-2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-2
        for j in range(0,i+1):
            print("*",end=" ")
        print("\r")
pattern(int(input()))

#downward Half pattern pyramid
def pattern(n):
    for i in range(n,-1,-1):
        for j in range(0,i):
            print("*",end=" ")
        print("\r")
pattern(int(input()))

#downward left angle pyramid
def pattern(n):
    k=2*n-2
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(end=" ")
        k=k+2
        for j in range(0,i):
            print("*",end=" ")
        print("\r")
pattern(int(input()))