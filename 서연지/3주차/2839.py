n = int(input())
count = 0

while n>0:
    if (n%5)==0:
        count += n//5
        n -= 5*(n//5)
    elif (n/3)>=1:
        count += 1
        n -= 3
    else :
        count = -1
        break

print(int(count))