arr = [1, 2, 3, 2, 4, 5, 1]

duplicates = []

for num in arr:
    if arr.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Duplicates:", duplicates)
