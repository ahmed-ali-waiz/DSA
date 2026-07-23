arr = [5,4,2,3,0]

arr.sort()

for i in range(len(arr)):
    if arr[i] != i:
        print(i)
        break
else:
        print(len(arr))