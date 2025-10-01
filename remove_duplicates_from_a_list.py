lst = list(map(int, input("Enter numbers separated by space: ").split()))

# Using set
print("Without duplicates (set):", list(set(lst)))

# Without set (preserve order)
res = []
for i in lst:
    if i not in res:
        res.append(i)
print("Without duplicates (order preserved):", res)
