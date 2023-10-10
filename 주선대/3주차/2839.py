def func_sugar(a):
    bag = 0
    while a >= 0 :
        if a % 5 == 0 :  
            bag += (a // 5)  
            break
        else:
            a -= 3  
            bag += 1 
    else:
        bag = -1
    
    return bag

a = int(input())
print(func_sugar(a))