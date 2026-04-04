def find_difference(arr1, arr2):
    i, j = 0, 0
    result = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            # Элемент из первого массива меньше — значит, его нет во втором
            result.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            # Элемент во втором массиве меньше — пропускаем его
            j += 1
        else:
            # Элементы равны — пропускаем оба
            i += 1
            j += 1
            
    # Добавляем оставшиеся элементы из первого массива, если они есть
    result.extend(arr1[i:])
    return result

# Пример:
list1 = [1, 2, 5, 8, 10, 15]
list2 = [2, 8, 12]

print(find_difference(list1, list2))  # Вывод: [1, 5, 10, 15]
