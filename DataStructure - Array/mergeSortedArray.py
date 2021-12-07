def mergeSortedArray(array1: list[int], array2: list[int]) -> list[int]:
    if not array1:
        return array2
    if not array2:
        return array1

    mergeArray = []
    i = j = 0

    counter = 1
    while i < len(array1) and j < len(array2):
        print(counter)
        counter += 1
        if array1[i] <= array2[j]:
            mergeArray.append(array1[i])
            i += 1
        else:
            mergeArray.append(array2[j])
            j += 1

    return mergeArray + array1[i:] + array2[j:]


arr1 = [1, 2, 3, 4, 5, 6, 7]
arr2 = [1, 2, 3, 4, 5, 6, 7]
# Time: O(a+b)
print(mergeSortedArray(arr1, arr2))
