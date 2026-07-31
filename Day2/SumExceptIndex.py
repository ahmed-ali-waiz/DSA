arr = [1,2,3,4]

for i in range(len(arr)):
    sum = 0
    for j in range(len(arr)):
        if i!=j:
          sum+=arr[j]
    print(sum,end = ' ')