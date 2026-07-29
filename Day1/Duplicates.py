arr = [4,2,4,5,2,3,1,5]

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