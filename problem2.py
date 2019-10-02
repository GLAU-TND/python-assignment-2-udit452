x=list(map(int,input().split(',')))
k=int(input())
for i in range(len(x)):
    for j in range(len(x)):
        if sum(x[j:i+1])==k:
            print(x[j:i+1])
