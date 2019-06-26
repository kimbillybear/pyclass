import random

name = input("Hello, what is your name?")

print(f"Hello, {name}")

salary = int(input("What is your current salary? (exclude dollar signs and commas)"))

print(f"{name}, your current salary is ${salary}")

raise_per =  random.randint(1,99)

print(f"Your raise is {raise_per}%")

raise_amount = (raise_per * 0.01) * salary

new_salary = salary + ((raise_per * 0.01) * salary)

print(f"Your raise amount is ${raise_amount}")

print(f"{name}, your new salary is ${new_salary}")