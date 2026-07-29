arr = [1,2,3,4,5,8]

target = 5

IsFound = False

for num in arr:

 if num == target:
  IsFound = True
  break
 
if IsFound:
 print("Number Found")

else :
 print("Number not Found")