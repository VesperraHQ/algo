arr = []
n = int(input())
i = 0

def is_prime(n):
    for d in range(2, n+1):
        if n % d == 0:
            break
    return d == n

def counter(n, arr):
    i = 0
    while True:
        if is_prime(n) == True:
            arr.append(n)
            break
        else:
            n -= 1
            i += 1
    if i != 0:
     arr.append(i)
    return arr



arr1 = counter(n, arr)

print(len(arr1))
print(*arr1)