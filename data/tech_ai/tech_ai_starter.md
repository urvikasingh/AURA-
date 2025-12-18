# TECH-AI Starter Coding Dataset

---

## 1. Python Basics

Python is a high-level, interpreted programming language known for its readability and versatility.

### Key Features

* Dynamically typed
* Automatic memory management
* Large standard library
* Strong community support

### Example

```python
x = 10
y = 20
print(x + y)
```

---

## 2. Python OOP Concepts

Object-Oriented Programming (OOP) helps structure large programs using objects and classes.

### Core Concepts

* Class
* Object
* Inheritance
* Polymorphism
* Encapsulation

### Example

```python
class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}"
```

---

## 3. Python Decorators

A decorator is a function that modifies the behavior of another function without changing its source code.

### Why use decorators?

* Logging
* Authentication
* Timing functions

### Example

```python
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")
```

---

## 4. FastAPI Introduction

FastAPI is a modern Python web framework used for building APIs quickly and efficiently.

### Features

* High performance
* Automatic API documentation
* Based on Python type hints

### Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}
```

---

## 5. FastAPI CRUD Example

CRUD stands for Create, Read, Update, Delete.

### Example

```python
@app.post("/users")
def create_user(name: str):
    return {"name": name}
```

---

## 6. SQL Basics

SQL (Structured Query Language) is used to interact with relational databases.

### Common Commands

* SELECT
* INSERT
* UPDATE
* DELETE

### Example

```sql
SELECT * FROM users;
```

---

## 7. SQL Joins

Joins combine rows from two or more tables based on a related column.

### Types of Joins

* INNER JOIN
* LEFT JOIN
* RIGHT JOIN

### Example

```sql
SELECT users.name, orders.amount
FROM users
INNER JOIN orders ON users.id = orders.user_id;
```

---

## 8. Git Basics

Git is a version control system used to track code changes.

### Common Commands

* git init
* git status
* git add
* git commit
* git push

---

## 9. Common Python Errors and Fixes

### Error: NameError

Occurs when a variable is not defined.

```python
print(x)  # x is not defined
```

**Fix:** Define the variable before use.

---

## 10. API Design Principles

Good API design improves usability and maintainability.

### Principles

* Use clear endpoints
* Follow REST conventions
* Use proper HTTP status codes

---

## 11. Async Programming in Python

Async programming allows concurrent execution for I/O-bound tasks.

### Example

```python
import asyncio

async def main():
    await asyncio.sleep(1)
    print("Done")

asyncio.run(main())
```

---

## 12. Design Patterns (Basics)

Design patterns are reusable solutions to common software problems.

### Common Patterns

* Singleton
* Factory
* Observer

---

### End of Starter Dataset

This dataset is intentionally **small, clean, and concept-focused** to give TECH-AI strong foundational coding knowledge.

You can safely add more files later and rerun `ingest.py` to expand TECH-AI’s knowledge.
