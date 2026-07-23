arr = [1,2,4,6,8,12]

IsSorted = False

for i in range(len(arr)-1):
    if arr[i] < arr[i+1]:
      IsSorted = True

print(IsSorted)