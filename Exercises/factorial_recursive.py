def factorial_recursive(n):
    # base case as to be zero as factorial of 0 is one
    if n == 0:
        return 1
    # multiply n with it's previous number as i call the function itself
    # the function will backtrace itself till it gets to the base case and move it's way back up
    else:
        return n * factorial_recursive(n-1)