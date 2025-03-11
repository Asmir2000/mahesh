# Iterative approach
def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Example usage
print(list(fibonacci_iterative(10)))
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Recursive approach
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Example usage
for i in range(10):
    print(fibonacci_recursive(i))
# Output: 0 1 1 2 3 5 8 13 21 34

# Recursive approach with memoization
def fibonacci_recursive_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    else:
        memo[n] = fibonacci_recursive_memo(n-1, memo) + fibonacci_recursive_memo(n-2, memo)
        return memo[n]

# Example usage
for i in range(10):
    print(fibonacci_recursive_memo(i))
# Output: 0 1 1 2 3 5 8 13 21 34

this line will get deleted 
