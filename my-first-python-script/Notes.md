# 🐍 Python Fundamentals I Strengthened

## Key Concepts Learned
- **Functions**: Define with `def function_name(parameters):`
- **F-strings**: Build clean messages with `f"Hi {name}! Your favourite color is {color}"`
- **User Input**: Collect with `input()` and clean with `.strip()`
- **Script Structure**:
    - Main function
    - Helper functions
    - `if __name__ == "__main__":` pattern
- **File Writing**: Use `with open(...) as file:` context manager

These are foundational skills every Python developer uses daily.

## 🧠 Mistakes I Made (and What They Taught Me)

### 1. Accidentally Creating a Tuple Instead of a String
**Wrong:**
```python
("Hi", name, "Your favourite color is", color)
```
This creates a tuple, causing `TypeError: can only concatenate tuple (not "str") to tuple`

**Lesson:** Use a single f-string to build complete sentences.

### 2. Incorrect F-string Syntax
**Wrong:**
```python
message = f"Hi" {name}! Your favourite color is {color}"
```

**Lesson:** Keep everything inside the f-string:
```python
message = f"Hi {name}! Your favourite color is {color}"
```