#Normal Bubble sort

def bubble_sort(arr):

    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):  
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#Modified Bubble sort

def modified_bubble_sort(arr):

    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:  
            break
    return arr

#Selection sort

def selection_sort(arr):

    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr



input_arr = [65, 25, 10, 20, 9]
result_arr = input_arr
print("Original Array:", input_arr)

print("Bubble Sort:", bubble_sort(result_arr))
print("Modified Bubble Sort:", modified_bubble_sort(result_arr))
print("Selection Sort:", selection_sort(result_arr))
