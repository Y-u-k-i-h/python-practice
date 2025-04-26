def factorial(n):
    # having x equal to one to act as the starter as it would be multiplied by the initial number
    # thus acting as the first number
    x = 1
    if n < 0:
        return 'Error'
    # factorial of zero is one
    if n == 0:
        return 1
    else:
        # for loop to start from the highest number and keep reducing it till 1
        for i in range(n, 0, -1):
            x *= i
        return x
