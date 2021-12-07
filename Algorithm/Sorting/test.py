def bubblesort(arr):
    qw = 0
    while qw < len(arr):
        for i in range(0, len(arr)-1):
            print(arr[i])
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

        qw += 1
    return arr


arr = [5, 9, 1, 2, 7, 3, 8, 2]
print(bubblesort(arr))
