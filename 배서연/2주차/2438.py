N = int(input())

for i in range(N):
    for j in range(i+1):
        print('*', end='')
    if i is not N-1:
        print()