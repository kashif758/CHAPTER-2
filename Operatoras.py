# 1. Arithmetic Operators
'''
| Operator | Description         | Example  | Result |
| -------- | ------------------- | -------- | ------ |
| `+`      | Addition            | `5 + 3`  | `8`    |
| `-`      | Subtraction         | `5 - 3`  | `2`    |
| `*`      | Multiplication      | `5 * 3`  | `15`   |
| `/`      | Division (float)    | `5 / 2`  | `2.5`  |
| `//`     | Floor Division      | `5 // 2` | `2`    |
| `%`      | Modulus (remainder) | `5 % 2`  | `1`    |
| `**`     | Exponentiation      | `5 ** 2` | `25`   |
'''
# 2. Assignment Operators
'''
| Operator | Description             | Example                |
| -------- | ----------------------- | ---------------------- |
| `=`      | Assign                  | `x = 5`                |
| `+=`     | Add and assign          | `x += 3` → `x = x + 3` |
| `-=`     | Subtract and assign     | `x -= 2` → `x = x - 2` |
| `*=`     | Multiply and assign     | `x *= 4` → `x = x * 4` |
| `/=`     | Divide and assign       | `x /= 2` → `x = x / 2` |
| `//=`    | Floor divide and assign | `x //= 2`              |
| `%=`     | Modulus and assign      | `x %= 3`               |
| `**=`    | Exponent and assign     | `x **= 2`              |
'''
# 3. Comparison Operators
'''
| Operator | Description           | Example  | Result  |
| -------- | --------------------- | -------- | ------- |
| `==`     | Equal to              | `5 == 5` | `True`  |
| `!=`     | Not equal to          | `5 != 3` | `True`  |
| `>`      | Greater than          | `5 > 3`  | `True`  |
| `<`      | Less than             | `5 < 3`  | `False` |
| `>=`     | Greater than or equal | `5 >= 5` | `True`  |
| `<=`     | Less than or equal    | `5 <= 3` | `False` |
'''
# 4. Logical Operators
'''
| Operator | Description             | Example          | Result  |
| -------- | ----------------------- | ---------------- | ------- |
| `and`    | True if **both** True   | `True and False` | `False` |
| `or`     | True if **any** is True | `True or False`  | `True`  |
| `not`    | Negates the value       | `not True`       | `False` |
'''

# Example Usage:
x = 10
y = 5

# Arithmetic
z = x + y  # 15

# Assignment
x += 2     # x = 12

# Comparison
print(x > y)  # True

# Logical
print(x > y and y < 10)  # True
