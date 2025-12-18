# Python Debugging – Common Errors

## NameError: name is not defined
Cause:
Occurs when a variable is used before it is assigned.

Example:
print(x)

Fix:
Define the variable before using it.
x = 10
print(x)

---

## TypeError: unsupported operand type(s)
Cause:
Occurs when an operation is applied to incompatible data types.

Example:
"5" + 3

Fix:
Convert values to the same data type.
int("5") + 3

---

## IndexError: list index out of range
Cause:
Occurs when accessing an index that does not exist in a list.

Example:
numbers = [1, 2, 3]
print(numbers[5])

Fix:
Check list length before accessing indices.

---

## ZeroDivisionError: division by zero
Cause:
Occurs when dividing a number by zero.

Example:
x = 10 / 0

Fix:
Check divisor value before division.
