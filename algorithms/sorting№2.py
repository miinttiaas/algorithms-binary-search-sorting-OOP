def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
arr = [3,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10,10,221,121,10]
print(selection_sort(arr))
print(sorted(arr) == selection_sort(arr))