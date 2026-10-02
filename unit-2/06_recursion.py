def factorial(n):
    # Return n factorial recursively.
    # Base case: 0! or 1! is 1
    if n <= 1:
        return 1
    # Recursive step
    return n * factorial(n - 1)

print(factorial(5))
print(factorial(0), factorial(1))


def factorial_traced(n, depth=0):
    # Return n factorial and print the call stack.
    pad = " " * depth
    print(f"{pad}factorial({n}) called")
    
    # Base case stops the recursion
    if n <= 1:
        print(f"{pad}-> base case returns 1")
        return 1
        
    # Recursive step with increased depth for indentation
    result = n * factorial_traced(n - 1, depth + 1)
    print(f"{pad}-> returns {result}")
    return result

factorial_traced(4)


def countdown(n):
    # Print n down to 1 and then liftoff.
    # Base case: stop when n reaches 0 or below
    if n <= 0:
        print("liftoff")
        return
    print(n)
    countdown(n - 1)

countdown(3)


def factorial_loop(n):
    # Return n factorial using a loop.
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial_loop(5), factorial(5))