# Write a program that prints all prime numbers. (Note: if your programming language does not support arbitrary size numbers, printing all primes up to the largest number you can easily represent is fine too.)

```python
import math


def p(x):
    if x < 2: return 0
    if x == 2: return 1
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0: return 0
    return 1


x = 100000000
s = ""
for i in range(1, x + 1):
    if p(i) == 1:
        s += str(i)
        s += ' '
print(s)
```
