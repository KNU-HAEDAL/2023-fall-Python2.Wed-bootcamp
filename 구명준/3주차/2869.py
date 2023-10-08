A,B,V = map(int, input().split())
cnt = (V-B) / (A-B)
if cnt == int(cnt):
    print(int(cnt))
else:
    print(int(cnt) + 1)