s = input()
limit = eval(input())
ls = s.split()
l1= []
st = ''
ln = len(ls)
if ln == 1:
    print(s)
i = 0
for l in ls:
    st += l
    i += 1
    if i < ln:
        lk = len(ls[i])
        if len(st) + 1 + lk <= limit:
            st += ' '
            continue
    l1.append(st)
    st = ''
print(l1)
