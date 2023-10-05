a, b = input().split()  # a와 b를 입력받아 split를 사용해 배열하고

a = int(a)
b = int(b) # a와 b를 int로 인식하게 한다

if a > b:   #a > b이면 참으로 나오겠금 조건을 설정
    print('>')
elif a < b:     # if문의 조건식이 참이 아닐 때 수행되는 문장인 elif를 사용해서 문장완성
    print('<')
elif a == b:
    print('==')