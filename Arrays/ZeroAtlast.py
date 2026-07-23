arr =[1,0,2,3,0,6,0,9]

arr1 = []

arr2 = []

for num in arr:
    if num!=0:
        arr1.append(num)

    else:
        arr2.append(num)
arr1.extend(arr2)

print(arr1)