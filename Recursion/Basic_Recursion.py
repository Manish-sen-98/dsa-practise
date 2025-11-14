def printNum(n):
    if n==1:
        print(1)
        return
    print(n)
    printNum(n-1)

printNum(5)

## Factorial using recursion

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

print(fact(4))