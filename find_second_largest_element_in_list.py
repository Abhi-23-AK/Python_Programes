lst = list(map(int, input("Enter numbers separated by space: ").split()))
unique = list(set(lst))
unique.sort()
if len(unique) >= 2:
    print("Second largest element:", unique[-2])
else:
    print("Not enough elements")
