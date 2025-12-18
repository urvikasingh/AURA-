# Python Exceptions

Exceptions are runtime errors that interrupt normal program execution.

Python uses try-except blocks to handle exceptions gracefully.

## Example
try:
    x = int("abc")
except ValueError:
    print("Conversion failed")

## Common Exceptions
- ValueError
- TypeError
- IndexError
- KeyError
- ZeroDivisionError

## Finally Block
The finally block always executes.

Example:
try:
    x = 10 / 2
finally:
    print("Done")
