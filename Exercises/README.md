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
This happens because 