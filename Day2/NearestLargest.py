arr = [1,2,4,5,1,2]

result = []

for i in range(len(arr)):
    greater = 0

    for j in range(len(arr)):
        if arr[j]>arr[i]:
            greater = max(greater,arr[j])

    result.append(greater)
print(result)