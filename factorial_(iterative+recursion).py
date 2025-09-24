# Iterative
def factorial_iter(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Recursive
def factorial_rec(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_rec(n-1)

print(factorial_iter(5))  # 120
print(factorial_rec(5))   # 120
