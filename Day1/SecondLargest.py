arr = [2,4,3,2,6,7,13,5,6]

largest = arr[0]
secondLargest = arr[0]

for num in arr:
   if num > largest:
      secondLargest = largest
      largest = num
print(secondLargest)
