S = list(input())
ls = ['a', 'b', 'c']
for x in S:
    if x in ls:
        ls.remove(x)
if len(ls) == 0:
    print('Yes')
else:
    print('No')
