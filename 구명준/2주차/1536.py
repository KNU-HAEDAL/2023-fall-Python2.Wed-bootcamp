key = 666
N = int(input())
cnt = 0
while True:
    if '666' in str(key):
        cnt +=1
    if cnt == N:
        print(key)
        break
    key +=1