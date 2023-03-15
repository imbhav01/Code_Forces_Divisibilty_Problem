x=int(input())

for i in range(0,x):
    y = str(input()).split()
    a,b,count = int(y[0]),int(y[1]),0
    while (a%b!=0):
        a = a+1
        count = count+1
    print(count)

