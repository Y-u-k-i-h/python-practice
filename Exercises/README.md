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
I first used a for loop to set up a base case which was the factorial of zero is one.<br>
```python
    if n == 0:
        return 1
```
In the else statement there is this `return n * factorial_recursive(n-1)` <br>
This returns `n` multiplied by calling the function in itself with the argument `n-1` <br>
The usefulness of this is that we generate new stack frames that will rely upon themselves. Let me present a visual to grasp the idea. Lets say we are to compute the factorial of `5`<br>
`factorial_recursive(5)` will call `factorial_recursive(5-1) ...`and so on and so forth till it reaches `factorial_recursive(0)` so now `1` gets returned and that is what is multiplied with the current value on `n` for each respective function.
```sql
factorial_recursive(5)
│
├── 5 * factorial_recursive(4)
│       │
│       ├── 4 * factorial_recursive(3)
│       │       │
│       │       ├── 3 * factorial_recursive(2)
│       │       │       │
│       │       │       ├── 2 * factorial_recursive(1)
│       │       │       │       │
│       │       │       │       └── 1 * factorial_recursive(0)
│       │       │       │               └── returns 1
│       │       │       │
│       │       │       └── returns 1 * 1 = 1
│       │       │
│       │       └── returns 2 * 1 = 2
│       │
│       └── returns 3 * 2 = 6
│
├── returns 4 * 6 = 24
│
└── returns 5 * 24 = 120

```

---

## 6. Sum of Digits of a Number
Started off by initializing a variable `total_sum` to hold the total sum. <br>
Had an if statement check numbers between the range of -9 to 9 and if the number falls between that then return the absolute value if the number. The reason for this is that for single digits we don't have neighbouring numbers to add them on to except for example, if it `1`, we can represent it as `01` so we'll have to do `0+1` which is just the number itself, and for negative numbers since we are just concerned with adding individual digits, we can just ignore it that's why I used the `abs()` function to give us the absolute value of the function.<br>
```python
# initialized a variable to hold the sum of the numbers
    total_sum = 0
    # i did this because if it's a single digit, then the sum would have to be the number itself
    # so i needed to return the range which contains single digits
    if n  >= -9 and n <= 9:
        return abs(n)
```
In the else block, I type casted the input to a string to enable to iterate through the individual digits as I add them to `total_sum` I type cast the individual string elements to type `int` before adding them.<br>
I then encountered a little problem where for negative numbers, the negative sign `-` could not be expressed as`int` so I had to add an if statement to check if the current element is equal to `-` so that I can skip it using the `continue` keyword.
```python
    else:
        # converted the number to a string
        # to help me iterate through individual digits
        n = str(n)
        for digit in n:
            # here i stripped off the '-' since it will throw an error as one can't add
            # a character and a number
            if digit == '-':
                continue
            total_sum += int(digit)
        return total_sum
```