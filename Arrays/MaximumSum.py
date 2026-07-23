arr = [1,2,3,4,8,5,6,9]

Largest = arr[0]
Smallest = arr[0]

for num in arr:
    if num>Largest:
        Largest = num

    elif num<Smallest:
        Smallest = num

Differnce = Largest - Smallest
print(Differnce)