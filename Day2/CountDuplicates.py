arr = [1,2,1,3,2]

result = []

for i in range(len(arr)):
    count = 0

    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1

    result.append(count)

print(result)