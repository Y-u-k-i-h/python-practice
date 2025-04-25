def sum_of_digits(n):
    # i did this because if it's a single digit, then the sum would have to be the number itself
    # so i needed to return the range which contains single digits
    # initialized a variable to hold the sum too
    total_sum = 0
    if n  >= -9 and n <= 9:
        return n
    else:
        # i decided to also convert the number to a string
        # this is to also help me iterate through individual digits
        n = str(n)
        for digit in n:
            # here i stripped off the '-' since it will throw an error as one can't add
            # a character and a number
            if digit == '-':
                continue
            total_sum += int(digit)
        return total_sum
