def reverse_string(string):
    # initialized an empty array to store the reversed string
    reversed_string = []
    for i in range(len(string), 0, -1):
        # used the length of the string to find the total number if characters
        # appended the characters in the array from the highest index to the lowest (0)
        # i - 1, is to cater for array indexing starting from 0
        reversed_string.append(string[i-1])
    # join back the words to return a string and not an array of reversed characters
    return "".join(reversed_string)
