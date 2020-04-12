# Binary Search
# Compare it to the middle element of array
# if it is equal return result
# else if it is lower , recursion first haft array
# else if it is greater, recursion second half array 
def binarySearch (arr, element):
    if arr == []:
        return False
    middle = arr.index(arr[(len(arr) - 1)//2])
    if element < arr[middle]:
        binarySearch(arr[:middle], element)
    elif element > arr[middle]:
        binarySearch(arr[middle+1:], element)
    return arr.index(element) if element in arr else False

a = binarySearch([1,2,3,4,11,6,7,8,9,10,11],111)
#print("Exist at index {0}".format(a))
# if element does not exist in array, last statement is still executed

#------------------------------------------------------------------------------------
#Quick Sort
#choose pivot is last element in array
def partition1(arr, low, high):
    pivot = arr[high]
    index = low - 1
    for i in range(low, high):   
        if (arr[i] < pivot): 
            index = index + 1
            arr[i], arr[index] = arr[index], arr[i]

    arr[index+1], arr[high] = arr[high], arr[index+1]
    return index + 1

def quickSort1(arr, low, high):
    if (low < high):
        pos = partition1(arr, low, high)
        print (arr)
        quickSort1(arr, low, pos - 1)
        quickSort1(arr, pos + 1, high)
    return arr

print(quickSort1([8,  9,  2,  1,  0,  0,  7,  6,  11,  4,  9, 5],0,11))

#--------------------------------------------------------------------------------------------------
def partition2(arr, low, high):
    #Choose most-left pivot
    pivot = arr[low]
    for i in range(low + 1, high + 1):
        if arr[i] <= pivot:
            continue
        for j in range(high - 1, low - 1, -1):
            if arr[j] > pivot:
                continue                
            if i < j:
                arr[i],arr[j] = arr[j], arr[i]
    tmp = -1        
    for i in range(low, high + 1): 
        if (arr[i] <= pivot):
            tmp += 1
            arr[i], arr[arr.index(pivot)] = arr[arr.index(pivot)], arr[i]
    return tmp + low

def quickSort2(arr, low, high):
    if low < high:
        pos = partition2(arr, low, high)
        quickSort2(arr, low, pos - 1)
        quickSort2(arr, pos + 1, high)
    return arr  
#print(quickSort2([10,9,8,7,3,2,4,13],0,7))
#print(quickSort2([1,2,3,4,3,6,7,8],0,7))
#print(quickSort2([8,8,8,8,8,8,8,8],0,7))
#print(quickSort2([8,7,6,5,4,3,2,1],0,7))


#----------------------------------------------------------------------------------------------------
# mergeSort
# determine middle element, seperate array into two halves, seperate util each halve has one element
# merge two halves into bigger sorted array
def mergeSort(arr):
    if len(arr) > 1:
        print("hihi")
        print(arr)
        middle = len(arr)//2
        L = arr[:middle]
        print(L)
        R = arr[middle:]
        print(R)
        mergeSort(L)
        mergeSort(R)
        i = 0
        j = 0
        k = 0
        print("start merge")
        print(arr)
        print(L)
        print(R)
        while (i < len(L) and j < len(R)):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while (i < len(L)):
            arr[k] = L[i]
            i += 1
            k += 1
        while (j < len(R)):
            arr[k] = R[j]
            j += 1
            k += 1
        print("After merge")
        print(arr)
    return arr
#print(mergeSort([10,9,8,7,3,2,4,13])) 

def binarySearchTree():
    pass
