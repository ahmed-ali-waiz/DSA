arr = [1,1,2,1,2,3,1,3,4,1,4,5,5,3,6,6]


duplicates = []

for num in arr:
    if num not in duplicates:
        duplicates.append(num)
arr[:] = duplicates
print(arr)