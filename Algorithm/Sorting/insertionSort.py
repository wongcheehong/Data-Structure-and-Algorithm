def insertionSort(array):
    sortedEndIndex = 0
    for i in range(1, len(array)):
        predecessorIndex = sortedEndIndex
        while predecessorIndex >= 0 and array[i] < array[predecessorIndex]:
            # Swap
            array[predecessorIndex], array[i] = array[i], array[predecessorIndex]
            predecessorIndex -= 1
            i -= 1
        sortedEndIndex += 1

    return array


print(insertionSort([5, 1, 4, 3, 2]))
print(insertionSort([84, 56, 46, 57, 94, 35, 83, 88,
      53, 44, 98, 47, 99, 100, 82, 89, 67, 27]))
