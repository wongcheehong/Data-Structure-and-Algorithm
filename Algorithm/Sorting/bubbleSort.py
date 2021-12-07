def bubbleSort(array):
    n = len(array)-1
    i = 0
    while i < n:
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
        i += 1
        if i == n:  # Element at the back is sorted (Largest)
            i = 0
            n -= 1

    return array


print(bubbleSort([84, 56, 46, 57, 94, 35, 83, 88,
      53, 44, 98, 47, 99, 100, 82, 89, 67, 27]))
