## Write a guessing game where the user has to guess a secret number. After every guess the program tells the user whether their number was too large or too small. At the end the number of tries needed should be printed. It counts only as one try if they input the same number multiple times consecutively.

```python
import random

n = random.randint(1, 100)

p = 0
counter = 0
nn = 0
while True:
    userInput = int(input("Please enter your guessing number: "))
    p = nn
    nn = userInput

    if p != nn:
        counter += 1

    if n == userInput:
        print("you guessed it right!")
        print("Number of multiple tries is: " + str(counter))
        break

    elif n > userInput:
        print("Your guessing is too small!")

    elif n < userInput:
        print("Your guessing is too high!")

```
