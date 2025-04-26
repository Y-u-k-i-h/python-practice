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
Since with every iteration 'i' becomes one of the numbers in the list, i add i to x and then return
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
In base 2, digits grow in place value by powers of two as you move to the left, and since the least significant bit(the one on the furthest right), can only have two states, either one or rezo.<br>
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
