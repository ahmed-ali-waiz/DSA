arr = [1,4,3,5,6,7]

largest = arr[0]
smallest =arr[0]

for num in arr:
    if num>largest:
        largest = num

    if num<smallest:
        smallest = num

Difference = largest - smallest
print(Difference)