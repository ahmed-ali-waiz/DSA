arr = [3, 0, 1]

arr.sort()

for i in range(len(arr)):
    if arr[i] != i:
        print(i)
        break
else:
    print(len(arr))