def mergeSort(array):
    if len(array) == 1:
        return array

    # Split array into left and right
    middle = int(len(array) / 2)
    left = array[:middle]
    right = array[middle:]

    return merge(
        mergeSort(left),
        mergeSort(right)
    )


def merge(left, right):
    array = []
    leftIndex = 0
    rightIndex = 0
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] < right[rightIndex]:
            array.append(left[leftIndex])
            leftIndex += 1
        else:
            array.append(right[rightIndex])
            rightIndex += 1

    array += left[leftIndex:] + right[rightIndex:]

    return array


print(mergeSort([5, 1, 4, 3, 2, 9, 10]))
print(mergeSort([84, 56, 46, 57, 94, 35, 83, 88,
      53, 44, 98, 47, 99, 100, 82, 89, 67, 27]))
