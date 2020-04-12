def factorical(n):
    if n <= 1: 
        return 1
    else:
        return n * factorical(n-1)
#print(factorical(5))

def fibonacci_recursion(index):
    if index in [1,2]:
        return 1
    else:
        return fibonacci_recursion(index-2)+fibonacci_recursion(index-1)
#print(fibonacci_recursion(10))

def fibonacci_iterative(index):
    arr = [1,1]
    for i in range(2,1000):
        arr.append(arr[i-1]+arr[i-2])
    return arr[index-1]
#print(fibonacci_iterative(10))

def naive_string_pattern(text, pattern):
    n = len(text)
    s = 0
    m = len(pattern)
    count = 0
    for s in range(0, n-m+1):
        if text[s:s+m] == pattern:
            print("exist pattern {0} from {1}".format(pattern, s))
            count = count + 1
    if count == 0:
        print("No pattern {0} exist in text".format(pattern)) 
#naive_string_pattern("abcdefabdssdsdab","ab")
#naive_string_pattern("abcdefabdssdsdab","dssd")

def sequential_search(arr, ele):
    count = 0
    for element in arr:
        if (element == ele):
            print("Ele first exist in index {0}".format(arr.index(element)))
            count = count + 1
    if count == 0:
        print("No ele {0} exist in arr".format(ele)) 
#sequential_search([1,2,3,4,5,6],10)

def selection_sort(arr):
    for i in range(0,len(arr)):
        min_ele = min(arr[i:])
        a = i
        b = arr.index(min_ele, i)
        arr[a], arr[b] = arr[b], arr[a]
    return arr
    
#print(selection_sort([1,3,2,4,3,2,6,54,65,34])) 
#print(selection_sort([1,2,3,4,5])) 

from functools import reduce
def func1(ar):
    return reduce(lambda x,y: x + y, ar)

#print(func1([1,2,3,4,5,6,7,8,9,10]))

def compareTriplets(a, b):
    score = [0,0]
    for i in range (0, len(a)):
        if (a[i] > b[i]):
            score[0] += 1
        elif (a[i] < b[i]):
            score[1] += 1
    return score

#print(compareTriplets([17,28,30],[99,16,18]))
#1000000001 1000000002 1000000003 1000000004 1000000005

def aVeryBigSum(ar):
    return reduce(lambda x,y: x + y, ar)

#print(aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]))

def diagonalDifference(arr):
    ele1 = 0
    for i in range(0, len(arr)):
       
        ele1 += arr[i][i] - arr[i][len(arr)-i - 1]    
    return abs(ele1)

#print(diagonalDifference([[11,2,4],[4,5,6],[10,8,-12]]))






