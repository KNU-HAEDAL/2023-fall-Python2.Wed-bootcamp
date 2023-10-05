while True: # 조건식 설정
    a, b = input().split()   # a와 b를 입력받아 split를 사용해 배열하고

    a = int(a)
    b = int(b) 
    # a와 b를 int로 인식하게 한다.

    if a == 0 and b == 0:
        break; #if a == 0 and b == 0:에서 while문을 중지 시키기 위해 설정
    else: # 이외의 경우
        print(a+b)