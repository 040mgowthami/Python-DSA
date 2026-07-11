arr1=[1,2,3,4,5]
arr2=[3,4,5,6,7]
common=[]
for num in arr1:
  if num in arr2:
    common.append(num)
print("common element:",common)
