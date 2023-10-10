def snail_fast(a,b,v):
    h = (v-b)/(a-b)
    if (h%1==0):
        answer = int(h)
    else:
        answer = int(h) + 1

    return answer

a,b,v= map(int,input().split())

print(snail_fast(a,b,v))