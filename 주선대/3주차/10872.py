def factorial(a):
    first = 1
    for i in range(1, a + 1):
        first *= i
    ans = first

    return ans

a = int(input())
print(factorial(a))