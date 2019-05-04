N, K = map(int, input().split())
a = []
for i in range(N):
    a.append(list(map(int, input().split())))
a.sort()
sum = 0
for i, x in enumerate(a):
    sum += x[1]
    if sum >= K:
        print(a[i][0])
        break
