def dec(x, n):
    c=0
    if(x[n-1]>=x[n-2]):
        x[n-1] = x[n-2]-1
        c += 1
    if (x[0] <= x[1]):
        x[0]=x[0]+1
        c=c+1
    for i in range(n - 2, 0, -1):
        if(x[i-1]<=x[i] and x[i+1]<=x[i])or(x[i-1]>=x[i] and x[i+1]>=x[i]):
            x[i] = (x[i - 1] + x[i + 1]) // 2
            c=c+1
            if (x[i]==x[i-1] or x[i]==x[i+1]):
                return False
    if (c > 1):
        return False
    return True
arr=list(map(int,input().split(',')))
n = len(arr)
if (dec(arr, n)):
    print("Yes")
else:
    print("No")
