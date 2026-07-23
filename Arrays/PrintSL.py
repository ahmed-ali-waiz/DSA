arr = [1,2,5,4,8,13,2,15,3]

Largest = arr[0]    
Secondlargest = arr[0]

Smallest = float('inf')
SecSmallest = float('inf')

for num in arr:
    if num>Largest:
        Secondlargest = Largest
        Largest = num

    elif num>Secondlargest and num!= Largest:
       Secondlargest = num


    if num < Smallest:
     SecSmallest = Smallest
     Smallest = num

    elif num<SecSmallest and num!= Smallest:
       SecSmallest = num

print(Largest)
print(Smallest)
print(Secondlargest)
print(SecSmallest)

 