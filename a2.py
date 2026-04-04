def short_dist(arr):
    last_x = last_y = None
    min_dist = float('inf')

    for i, val in enumerate(arr):
        if val == "X":
            last_x = i
            if last_y is not None:
                min_dist = min(min_dist, abs(last_x - last_y))
        elif val == "Y":
            last_y = i
            if last_x is not None:
                min_dist = min(min_dist, abs(last_y - last_x))
        
    return min_dist if min_dist != float('inf') else None


input = ["Y", "O", "Y", "O", "O", "X"]
print(short_dist(input))
