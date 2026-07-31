arr = [1,2,3,4]
result = []

for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if arr[j]>arr[i]:
            count+=1
    result.append(count)
print(result)
            