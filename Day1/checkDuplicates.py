arr = [1,2,1,3,4,1,2,2,4,56,2,5,4,3,2,3,3,3,4]

visited = []
Duplicates = []

for num in arr:
    if num in visited:
        if num not in Duplicates:
            Duplicates.append(num)

    else:
        visited.append(num)

print(Duplicates)