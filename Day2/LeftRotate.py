arr = [1,2,3,4,5]

last = arr[0]

for i in range(0,len(arr)-1,1):
    arr[i] = arr[i+1]


arr[-1] = last

print(arr)