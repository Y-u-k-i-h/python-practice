def factorial(n):
    # factorial of zero is one
    if n == 0:
        return 1
    else:
        # having x equal to one to act as the starter as it would be multiplied by the initial number
        # thus acting as the first number
        x = 1
        # for loop to start from the highest number and keep reducing it till 2,
        # i saw no point in including one as it would result to the same answer
        for i in range(n, 1, -1):
            x *= i
        return x
