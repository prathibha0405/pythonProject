def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print(function(i,j)," ",end=" ")
        print()
def function(n,k):
    res=1
    if(k>n-k):
        k=n-k
    for i in range(0,k):
        res=res*(n-i)
        res=res//(i+1)
    return res
pattern(int(input()))


#Descending order pattern
def pattern(n):
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(j,end=" ")
        print("\r")
pattern(int(input()))

#Ascending order pattern
def pattern(n):
    for i in range(0,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print("\r")
pattern(int(input()))

#3
def pattern(n):
    k=2*n-2
    x=0
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
            print(x,end=" ")
            x=x+1
        print("\r")
pattern(int(input()))
