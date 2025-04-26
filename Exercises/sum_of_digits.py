def sum_of_digits(n):
    # initialized a variable to hold the sum of the numbers
    total_sum = 0
    # I did this because if it's a single digit, then the sum would have to be the number itself
    # so I needed to return the range which contains single digits
    if n  >= -9 and n <= 9:
        return abs(n)
    else:
        # converted the number to a string
        # to help me iterate through individual digits
        n = str(n)
        for digit in n:
            # here I stripped off the '-' since it will throw an error as `-` can't be converted
            # to type int
            if digit == '-':
                continue
            total_sum += int(digit)
        return total_sum
