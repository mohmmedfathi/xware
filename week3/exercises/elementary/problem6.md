# Write a program that asks the user for a number n and gives them the possibility to choose between computing the sum and computing the product of 1,…,n.

```python

def sum (n):
    sum = 0
    
    for i in range(1,n+1):
        sum+=i
        
    return sum


def product (n) :
    product= 1 
    for i in range(1,n+1):
        product*=i
        
    return product
    
n=int(input('enter number : '))

choice= int (input ('enter 1 to sum  ,or, enter 2 to product : '))

if choice == 1 :
    print(sum(n))
if choice == 2 :
    print (product(n))
```
