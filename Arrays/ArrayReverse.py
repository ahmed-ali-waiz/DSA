arr = [1,3,2,4,5,13]

left = 0
right = len(arr)-1

while left < right:
    arr[left],arr[right] = arr[right],arr[left]

    left+=1
    right-=1

print(arr)