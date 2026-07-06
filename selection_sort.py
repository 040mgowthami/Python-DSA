numbers=[2,4,6,8,9]
n=len(numbers)
for i in range(n):
  min_index=i
  for j in range(i+1,n):
    if numbers[j]<numbers[min_index]:
      min_index=j
  numbers[i],numbers[min_index]=number[i]
print("sorted array:",numbers)
