arr = [1,4,2,5,6,3,4,8]

Largest = arr[0]
Smallest = arr[0]

for num in arr:
    if num > Largest:
        Largest = num
    elif  num < Smallest:
      Smallest = num

Differnce = Largest - Smallest
print(Differnce)