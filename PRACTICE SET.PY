# PRACTICE SET
'''
1. Write a python program to Add two number.
2. write a program to find remainder when a number is divide by Z.
3. check the type of variable assigned using input () function.
4. Use comparison operator to find out whether a given variable a is greater then 'b' or not. take a=34 and b=80.
5. write a python program find an average of two numbers entered by the user.
6. write a Python program to Calculate the square the square of number entered by this user.
'''

# Solution 1

x = int(input("Enter the firrst number: "))
y = int(input("Enter the second Number: "))

Result = x + y
print("The sum of the two Number Is: ", Result)

# Solution 2
# Program to find remainder when a number is divided by Z
num = int(input("Enter a number: "))
Z = int(input("Enter the divisor (Z): "))

remainder = num % Z
print("Remainder =", remainder)

 
# Solution 3
# Check the type of variable from input()
value = input("Enter something: ")

print("The type of value is:", type(value))


# Solution 4
# Comparison operator example
a = 34
b = 80

print("Is a greater than b?", a > b)


# Solution 5
# Program to find average of two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

average = (num1 + num2) / 2
print("Average =", average)


# Solution 6

# Program to calculate square of a number
num = float(input("Enter a number: "))

square = num * num   # or num ** 2
print("Square of the number is:", square)
