arr = [4,2,4,2,1,2,3,5]

duplicates = []


for num in arr:
    if num not in duplicates:
        duplicates.append(num)

print(duplicates)