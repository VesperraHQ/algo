n = int(input())

def decomp(n):
    def primes_up_to(n):
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i*i, n + 1, i):
                    sieve[j] = False
        return [i for i in range(2, n + 1) if sieve[i]]

    result = []
    
    for p in primes_up_to(n):
        power = 0
        k = p
        while k <= n:
            power += n // k
            k *= p
        
        if power == 1:
            result.append(str(p))
        else:
            result.append(f"{p}^{power}")
    
    return " * ".join(result)

print(decomp(n))