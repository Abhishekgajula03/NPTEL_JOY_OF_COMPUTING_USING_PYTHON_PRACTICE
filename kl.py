
def Msquare(n):
    square=[]
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        square.append(l)
    for i in range(n):
        for j in range(n):
            print(square[i][j],end=" ")
        print(end='\n')
        
    i=n//2
    j=n-1
    count=1
    num=n*n
    print(end='\n')
    while(count<=num):
        if i==-1 and j==n:
            i=0
            j=n-2
        else:
            if j==n:
                j=0
            if i<0:
                i=n-1
        if square[i][j]!=0:
            i=i+1
            j=j-2
            continue
        else:
            square[i][j]=count
            count+=1
        i=i-1
        j=j+1
    for i in range(n):
        for j in range(n):
            print(square[i][j],end=" ")
        print(end='\n')
Msquare(3)