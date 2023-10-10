n = int(input())
g = 1 # n이 0이면 1이 되게 설정
if n > 0: #0보다 큰 경우의 조건문
    for z in range(1, n+1):# 범위 설정, 1부터 n+1까지 반복  
     g *= z #g에 z을 곱함
print(g)