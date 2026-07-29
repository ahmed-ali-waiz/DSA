arr = [1,222,3,4,5,5,32,1,3,2,4]

target = 4
count = 0

for i in range(len(arr)):
    if target == arr[i]:
        count+=1

print(count)