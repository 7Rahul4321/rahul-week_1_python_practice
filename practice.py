#  1st program
text = input("Enter a string: ")

reverse = text[::-1]

print("Reversed string:", reverse)

# 2nd program
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not prime")
            break
    else:
        print(num, "is prime")
else:
    print("Not a prime number")

# 3rd program
n = int(input("How many terms? "))

a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# 4th program
import random

secret = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == secret:
    print("Correct!")
else:
    print("Wrong! Number was", secret)
  
# 5th program
text = input("Enter text: ")

count = 0

for char in text.lower():
    if char in "aeiou":
        count += 1

print("Vowels:", count)
