# Write a program that prints a multiplication table for numbers up to 12.
```python 
n = 12
t = [f"{j} *  {i}  =  {i * j} " for j in range(1,n+1) for i in range(1,n+1)]
print(t)
```
