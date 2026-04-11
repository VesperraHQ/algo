import sys

def solve():
    
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    if n == 1:
        print(1)
        return
    
    a = list(map(int, input_data[1:]))
    
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i+1] = pref[i] + a[i]
        
    res = [0] * n
    
    first_can_start = -1
    for i in range(1, n):
        if a[i] > a[0]:
            first_can_start = i
            break
            
    if first_can_start == -1:
        print(*( [0] * n ))
        return

    res[n-1] = 1
    
    for i in range(n - 2, first_can_start - 1, -1):
        if pref[i+1] > a[i+1] and res[i+1] == 1:
            res[i] = 1
        else:
            break
            
    print(*(res))