# this chapter made only for importin modules
## Task 0: Importing and Printing Addition Result
In this task, you need to write a program that imports the add function from the file add_0.py and prints the result of the addition 1 + 2 = 3.
FILE ---> ``0-add.py``

## Task 1: Importing Functions and Performing Maths
For this task, you are required to write a program that imports functions from the file calculator_1.py and performs various mathematical operations using those functions. The program should print the result of each operation.
FILE ---> ``1-calculation.py``

## Task 2: Printing Command-Line Arguments
In this task, you need to write a program that prints the number of command-line arguments passed to it and lists those arguments with their positions.
FILE ---> ``2-args.py``


## Task 3: Infinite Addition
For this task, you have to write a program that prints the result of adding all the command-line arguments together.
FILE ---> ``3-Infinite_add.py``

## Task 4: Discover Hidden Names
In this task, you need to write a program that prints all the names defined in the compiled module hidden_4.pyc, excluding the ones starting with "__".
FILE ---> ``4-hidden_discovery.py``

## Task 5: Importing a Variable
For this task, you are required to write a program that imports the variable "a" from the file variable_load_5.py and prints its value.
FILE ---> ``5-variable_load.py``

## Task 6: Building a Calculator
In this task, you need to write a program that imports all functions from the file calculator_1.py and performs basic mathematical operations based on command-line arguments.
FILE ---> ``100-my_calculator.py``
## Task 7: Easy Print
For this task, you need to write a program that prints the string "#pythoniscool" to the standard output.
FILE ---> ``101-easy_print.py``

## Task 8: ByteCode to Python
In this task, you need to write a Python function magic_calculation(a, b) that performs the same functionality as the provided Python bytecode.
Each task has specific requirements and instructions that need to be followed to achieve the desired output.
```
  3           0 LOAD_CONST               1 (0)
              3 LOAD_CONST               2 (('add', 'sub'))
              6 IMPORT_NAME              0 (magic_calculation_102)
              9 IMPORT_FROM              1 (add)
             12 STORE_FAST               2 (add)
             15 IMPORT_FROM              2 (sub)
             18 STORE_FAST               3 (sub)
             21 POP_TOP

  4          22 LOAD_FAST                0 (a)
             25 LOAD_FAST                1 (b)
             28 COMPARE_OP               0 (<)
             31 POP_JUMP_IF_FALSE       94

  5          34 LOAD_FAST                2 (add)
             37 LOAD_FAST                0 (a)
             40 LOAD_FAST                1 (b)
             43 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             46 STORE_FAST               4 (c)

  6          49 SETUP_LOOP              38 (to 90)
             52 LOAD_GLOBAL              3 (range)
             55 LOAD_CONST               3 (4)
             58 LOAD_CONST               4 (6)
             61 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             64 GET_ITER
        >>   65 FOR_ITER                21 (to 89)
             68 STORE_FAST               5 (i)

  7          71 LOAD_FAST                2 (add)
             74 LOAD_FAST                4 (c)
             77 LOAD_FAST                5 (i)
             80 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             83 STORE_FAST               4 (c)
             86 JUMP_ABSOLUTE           65
        >>   89 POP_BLOCK

  8     >>   90 LOAD_FAST                4 (c)
             93 RETURN_VALUE

 10     >>   94 LOAD_FAST                3 (sub)
             97 LOAD_FAST                0 (a)
            100 LOAD_FAST                1 (b)
            103 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
            106 RETURN_VALUE
            107 LOAD_CONST               0 (None)
            110 RETURN_VALUE

```
FILE ---> ``102-magic_calculation.py``
## Task 9: Fast alphabet
In this task, you need to write a program that prints the alphabet in uppercase, followed by a new line. The program should be a maximum of 3 lines long and must follow the given restrictions:

- You are not allowed to use any loops.
- You are not allowed to use any conditional statements.
- You are not allowed to use the str.join() method.
- You are not allowed to use any string literal.
- You are not allowed to use any system calls.

FILE ---> ``103-fast_alphabet.py``
