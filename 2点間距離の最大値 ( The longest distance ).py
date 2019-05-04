import math

N = int(input())
x, y = [0]*N, [0]*N
for i in range(N):
    x[i], y[i] = map(int, input().split())

ls = []

for i in range(N-1):
    for j in range(i+1, N):
        ls.append(math.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2))
print(max(ls))
