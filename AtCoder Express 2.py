N, M ,Q = [int(i) for i in input().split()]
L, M, p, q = [0]*M,[0]*M,[0]*Q,[0]*Q
for i in range(M):
    L[i], R[i] = map(int, input().split())
for i in range(Q):
    p[i], q[i] = map(int, input().split())

ans = []

for i in range(Q):
