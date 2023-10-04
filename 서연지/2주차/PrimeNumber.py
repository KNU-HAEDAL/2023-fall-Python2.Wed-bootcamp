n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))
cnt = 0

for i in range (n,m+1):
    for j in range (2,i+1):
        if j==i:
            cnt += 1
        elif (i % j) == 0:
            break

print("소수개수:", cnt)