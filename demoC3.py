import math
arr = [0,1,0,1,0,0,0,0]
tmp = []
res = []
idx = 0
while (idx < len(arr)):
    if arr[idx] == 0:
        tmp.append(arr[idx]) 
    if arr[idx] == 1 or idx == len(arr) - 1:
        print(tmp)
        res.append(tmp)
        tmp = []
    idx += 1
print(res)
jump = 0
for ele in res:
    jump += math.floor(len(ele)/2)

print (jump + len(res) - 1)