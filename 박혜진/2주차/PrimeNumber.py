n = int(input("첫 번째 수 입력: "))
m = int(input("두 번째 수 입력: "))
count = 0

for i in range(n, m+1):
    c = 0
    for a in range(1, i+1):
        if i % a == 0:
            c += 1
    if c == 2 :
        count += 1
print('소수개수:', count)