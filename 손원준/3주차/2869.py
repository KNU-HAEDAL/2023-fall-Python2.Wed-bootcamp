A, B, V = map(int, input().split()) #A는 올라, B는 떨어 V는 목적

if (V-B) % (A-B) == 0 :
    print((V-B) // (A-B))
else :
    print(((V-B) // (A-B)) +1)