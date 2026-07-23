arr = [5,1,2,1,3,4,2,3,4]

visited = []
duplicates = []

for num in arr:
    if num in visited:
        if num not in duplicates:
            duplicates.append(num)

    else:
     visited.append(num)
print(duplicates)
print(visited)