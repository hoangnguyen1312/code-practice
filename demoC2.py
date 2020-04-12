#Dynamic Programming Example
#1 Fibonacci
def fib(n):
    dp = [0]*(n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
#print(fib(100))

#2 Coin exercise
def min_amount(n, S, w):
    dp = [0]*(S + 1)
    dp[0] = 0
    for P in range(1, S + 1):
        dp[P] = min([dp[P - tmp] for tmp in w if tmp <= P]) + 1
    return dp[S]
#print(min_amount(3, 100, [1,3,5]))

#3 find longest sub-string:
def longest_substring(s1,s2):
    arr = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    for i, x in enumerate(s1,1):
        for j, y in enumerate(s2, 1):
            if (x == y):
                arr[i][j] = arr[i-1][j-1] + 1
            else:
                arr[i][j] = max(arr[i][j-1],arr[i-1][j])
    print(arr)
    return arr[-1][-1] 

#print(longest_substring("quetzalcoatl","tezcatlipoca"))

# Tìm dãy con đơn điệu dài nhất
def findUpSubarray(lst):
    n = len(lst)
    arr = [-10000]
    for i in range(len(lst)):
        arr.append(lst[i])
    arr.append(10000)
    L = [0] * (n + 2)
    T = [0] * (n + 1)
    L[n + 1] = 1
    for i in range(n,-1,-1):
        jmax = i
        for j in range(i + 1, len(arr)):
            if (arr[j] > arr[i]) and L[j] > L[jmax]:
                jmax = j

        L[i] = L[jmax] + 1
        T[i] = jmax
    print(L)
    print(T)
    print(L[0] - 2)
    index = T[0]
    while (index != n + 1):
        print(arr[index])
        index = T[index]
findUpSubarray([1,2,3,4,5,6,7,8,9,11,2,1,1,1,1])    
findUpSubarray([5, 2, 3, 4, 9, 10, 5, 6, 7, 8])

def findDownSubarray(lst):
    n = len(lst)
    arr = [10000]
    for i in range(len(lst)):
        arr.append(lst[i])
    arr.append(-10000)
    L = [0] * (n + 2)
    T = [0] * (n + 1)
    L[n + 1] = 1
    for i in range(n,-1,-1):
        jmin = i
        for j in range (i + 1, len(arr)):
            if arr[j] < arr[i] and L[j] > L[jmin]:
                jmin = j
        L[i] = L[jmin] + 1
        T[i] = jmin
    print(L)
    print(T)
    
    index = T[0]
    while(index != n + 1):
        print(arr[index])
        index = T[index]
     
findDownSubarray([9,8,7,6,5])
findDownSubarray([1,2,3,4,5,6,7,8,9,11,2,1,1,1,1])    
        


