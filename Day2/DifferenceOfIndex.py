arr = [2,4,6]

result = []

for i in range(len(arr)):
    sum = 0
    for j in range(len(arr)):
        if i!=j:
            sum+= arr[j]

    result.append(arr[i]-sum)
print(result)