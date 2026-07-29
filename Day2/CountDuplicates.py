arr = [1,2,1,3,2,3,4,1,4,2,5,5,6]
duplicates = []

for i in range(len(arr)):
    count = 0

    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1

    if count > 1 and arr[i] not in duplicates:
        duplicates.append(arr[i])

print(duplicates)