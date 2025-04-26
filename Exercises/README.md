## 1. Sum all elements in a list

```python
def sum_elements(list):
    x = 0
    for i in list:
        x += i
    return x
```
Initialized a variable x to store the sum
```py
x = 0
```
I then had a for loop to iterate through the list of numbers
```py
    for i in list:
```
Since with every iteration `i` becomes one of the numbers in the list, I add `i` to `x` and then return
```python
    x += 1
return x
```
---
## 2. Check if a number is even or odd

```python
    # I perfomed an AND operation since for a number to be odd, the least significant bit has to be set
    # as it is in the ones position.
    if num & 0x1 == 0:
        return "Even"
    else:
        return "Odd"

```
With this problem I realised that for a number to be odd, then the least significant bit has to be set <br>
In base 2, digits grow in place value by powers of two as you move to the left, and since the least significant bit(the one on the furthest right), can only have two states, either one or zero.<br>
```txt
2⁷ 2⁶ 2⁵ 2⁴ 2³ 2² 2¹ 2⁰
0  0  0  0  0  0  0  0
```
And since we know even numbers are divisible by 2 and odd numbers are not. We can thus express them as
```text
n = 2k (for an even number)
n = 2k + 1 (for an odd number)
```
This means that for a number to be odd, the last bit then has to be set and for a number to be even the last bit has to be unset.<br>
With this in mind we can then use a bit mask of 0X1 (a template basically) and perform an AND operation with the original number to check if a number is odd or even.<br>

**An AND operation compares two bits and returns:**<br>
* 1 if both bits are one
* 0 otherwise
```text
If we AND 8 and 0x1(hexadecimal representation of 1)
1000 
0001
----
0000 (notice the least significant bit has been unset)

If we AND 7 and 0x1
0111
0001
----
0001 (notice the least significant bit has been set)
```
**So we come to the conclusion that if you perform an AND operation with an even number and the mask 0x1, the least significant bit will always be unset and if you perform an AND operation with an even number using the same mask, the least significant bit will always be set.**<br>

So when you implement it in code, I had an if statement check for the result of the AND operation
```python
    if num & 0x1 == 0:
        return "Even"
    else:
        return "Odd"
```

---

## 3. Compute factorial using a loop.
A factorial of a number n is the product of all positive integers less than or equal to n.<br>
So to deal with this, I had to initialize a variable x to 1. The reasoning behind this is so that I could multiply it with the original number and use it to multiply the rest of the numbers as it updates itself.<br>
I then ued an if statement to check if the number is less than zero to return an error as we can't get the factorial of negative numbers with the normal mathematical definition of a factorial
```python
x = 1
    if n < 0:
        return 'Error'
```
Then I had to use another if statement to check if the number is zero as 0! is 1.<br>
Then in the else statement, I used a for loop to start from the number itself to one, and I subtract the original number with every iteration. I then had x get multiplied with the current value of I according to its respective iteration and return the value after the whole loop. <br>
```python
    else:
        # for loop to start from the highest number and keep reducing it till 1
        for i in range(n, 1, -1):
            x *= i
        return x
```

---

## 4. Reverse a string (without using [::-1] or built-in methods).
I first initialized an empty array to hold my revesed string.<br>
I then used a for loop to iterate through the whole string, but I used the `len()` function to get the length of the string and use that as the starting number and 0 the stoping number. The for loop then decrements `i` by one with each iteration.<br>
I then append `i-1` to my array. The reason for that is to cater for element indexing as counting starts from 0. I then return the reversed string, but I also realised that when I just return the array, output will be in array format, so I used `"".join(reversed_string)`, the `""` means that I do not want to separate the strings.
```python
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
```

---

## 5. Factorial (Recursive)
