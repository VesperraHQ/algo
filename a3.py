def quad_sum(arr):
    sum = 0
    n = len(arr)

    for i, val in enumerate(arr, start=1):
        if n % val == 0:
            sum += val**2
    return sum

input = [1, 2, 3, 4]
print(quad_sum(input))