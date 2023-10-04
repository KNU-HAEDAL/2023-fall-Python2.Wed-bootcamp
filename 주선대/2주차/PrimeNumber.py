n = int(input("첫 번째 수 입력: "))
m = int(input("두 번째 수 입력: "))
count = 0

for num in range(n, m + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1

print("소수 개수: " + str(count))