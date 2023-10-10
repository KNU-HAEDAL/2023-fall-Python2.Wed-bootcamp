n = int(input())

if n % 5 == 0:  # n은 설탕
    print(n // 5)
else: #아니면
    b = 0 #b는 봉지
    while n > 0:
        n -= 3 #5로 떨어지지않는다면, 3키로씩 빼서
        b += 1 #봉지 1개 추가
        if n == 1 or n == 2: #그런데도 1키로나 2키로가 남으면 
            print(-1)  # -1을 출력시킨다
            break
        elif n % 5 == 0:  # 3kg과 5kg를 조합해서 담을 수 있을 때
            b += n // 5
            print(b)
            break
        elif n == 0:  # 3으로 나눠떨어질 때
            print(b)
            break
