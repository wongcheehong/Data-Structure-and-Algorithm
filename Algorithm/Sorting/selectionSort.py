def selectionSort(array):
    i = 0
    while i < len(array):
        minIndex = i
        # Element from the beginning is slowly sorted from index 0 to n
        for j in range(i, len(array)):
            if array[j] < array[minIndex]:
                minIndex = j

        # Swap
        array[i], array[minIndex] = array[minIndex], array[i]
        i += 1
    return array


print(selectionSort([84, 56, 46, 57, 94, 35, 83, 88,
      53, 44, 98, 47, 99, 100, 82, 89, 67, 27]))
