# try and Exceptions concept

## Task 0: Safe list printing


- Write a function that prints x elements of a list.

    - Prototype: ``def safe_print_list(my_list=[], x=0)``:
    - my_list can contain any type **(integer, string, etc.)**.
    - All elements must be printed on the same line followed by a new line.
    - x represents the number of elements to print.
    - x can be bigger than the length of my_list.
    - Returns the real number of elements printed.
    - You have to use try/except.
    - You are not allowed to import any module.
    - You are not allowed to use len().
```py
Example usage:

python

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
```

```py
Output:

makefile

12
nb_print: 2
12345
nb_print: 5
12345
nb_print: 5
```

***File: 0-safe_print_list.py***

## Task 1: Safe printing of an integers list


- Write a function that prints an integer with "{:d}".format().

    - Prototype: `def safe_print_integer(value)`:
    - value can be any type (integer, string, etc.).
    - The integer should be printed followed by a new line.
    - Returns True if value has been correctly printed (it means the - value is an integer).
    - Otherwise, returns False.
    - You have to use try/except.
    - You have to use "{:d}".format() to print as an integer.
    - You are not allowed to import any module.
    - You are not allowed to use type().

```py
Example usage:

python

value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))
```
```py
Output:

vbnet

89
-89
School is not an integer
```
***File: 1-safe_print_integer.py***

## Task 2: Print and count integers

Write a function safe_print_list_integers that prints the first x elements of a list, considering only integers. The function should adhere to the following requirements:

- Prototype: def safe_print_list_integers(my_list=[], x=0):
- my_list can contain any type (integer, string, etc.).
- All integers should be printed on the same line, followed by a new line. Other types of values in the list must be skipped silently.
- x represents the number of elements to access in my_list.
- x can be larger than the length of my_list. In such cases, an exception is expected to occur.
- Returns the real number of integers printed.
- Use try and except for error handling.
- Use "{:d}".format() to print an integer.
- Do not import any module.
- Do not use len().

```py

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
```
```py
OUTPUT:
12
nb_print: 2
12345
nb_print: 5
12345Traceback (most recent call last):
  File "./2-main.py", line 14, in <module>
    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
  File "/0x05/2-safe_print_list_integers.py", line 7, in safe_print_list_integers
    print("{:d}".format(my_list[i]), end="")
IndexError: list index out of range
```
***File: 2-safe_print_list_integers.py***

## 4. List Division


Write a function that divides element by element 2 lists.

- Prototype: `def list_division(my_list_1, my_list_2, list_length):`
- `my_list_1` and `my_list_2` can contain any type (integer, string, etc.).
- `list_length` can be bigger than the length of both lists.
- Returns a new list (length = `list_length`) with all divisions.
- If two elements can't be divided, the division result should be equal to 0.
- If an element is not an integer or float, print: "wrong type".
- If the division can't be done (`/0`), print: "division by 0".
- If `my_list_1` or `my_list_2` is too short, print: "out of range".
- You have to use `try`, `except`, `finally`.
- You are not allowed to import any module.

Example usage:

```python
my_list_1 = [10, 8, 4]
my_list_2 = [2, 4, 4]
result = list_division(my_list_1, my_list_2, max(len(my_list_1), len(my_list_2)))
print(result)
# Output: [5.0, 2.0, 1.0]

print("--")

my_list_1 = [10, 8, 4, 4]
my_list_2 = [2, 0, "H", 2, 7]
result = list_division(my_list_1, my_list_2, max(len(my_list_1), len(my_list_2)))
print(result)
----
# Output: division by 0
#         wrong type
#         out of range
#         [5.0, 0, 0, 2.0, 0]
```

## 5. Raise Exception



Write a function that raises a type exception.

- Prototype: `def raise_exception():`
- You are not allowed to import any module.

Example usage:

```python
try:
    raise_exception()
except TypeError as te:
    print("Exception raised")
# Output: Exception raised
```
## 6. Raise a Message
**Mandatory**
**Score: 100.0%** (Checks completed: 100.0%)

Write a function that raises a name exception with a message.

- Prototype: `def raise_exception_msg(message=""):`
- You are not allowed to import any module.

Example usage:

```python
try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)
# Output: C is fun
```
## 7. Safe Integer Print with Error Message


Write a function that prints an integer.

- Prototype: `def safe_print_integer_err(value):`
- `value` can be any type (integer, string, etc.).
- The integer should be printed followed by a new line.
- Returns `True` if `value` has been correctly printed (it means the value is an integer).
- Otherwise, returns `False` and prints in stderr the error preceded by `Exception:`.
- You have to use `try:` and `except:` for error handling.
- You have to use `"{:d}".format()` to print as an integer.
- You are not allowed to use the `type()` function.

Example usage:

```python
value = 89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))
```

```py
OUTPUT
89
-89
Exception: Unknown format code 'd' for object of type 'str'
School is not an integer
```
## 8. Safe Function


Write a function that executes a function safely.

- Prototype: `def safe_function(fct, *args):`
- You can assume `fct` will always be a pointer to a function.
- Returns the result of the function.
- Otherwise, returns `None` if something happens during the function and prints in stderr the error preceded by `Exception:`.
- You have to use `try:` and `except:` for error handling.

Example usage:

```python
def my_div(a, b):
    return a / b

result = safe_function(my_div, 10, 2)
print("result of my_div: {}".format(result))

result = safe_function(my_div, 10, 0)
print("result of my_div: {}".format(result))

def print_list(my_list, length):
    i = 0
    while i < length:
        print(my_list[i])
        i += 1
    return length

result = safe_function(print_list, [1, 2, 3, 4], 10)
print("result of print_list: {}".format(result))
```

```py
result of my_div: 5.0
Exception: division by zero
result of my_div: None
1
2
3
4
Exception: list index out of range
result of print_list: None
```
