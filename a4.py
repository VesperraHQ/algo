def first_array_unic_elts(arr1, arr2):
    resulting_array = []
    i = 0
    j = 0

    for val in arr1:
        if val > arr2[j]:
            j += 1
            resulting_array.append(val)
        elif val == arr2[j]:
            j += 1
            i += 1
        else:
            i += 1
            resulting_array.append(val)

    return(resulting_array)

arr1 = [1, 2, 4, 8, 16]
arr2 = [1, 3, 8, 25]

print(first_array_unic_elts(arr1, arr2))