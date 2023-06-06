# loops and conditions in python 
## 0-positive_or_negative
Loop through random numbers using func ``random.randint()`` from the module ``random`` than check if the value is either positive, negative or zero
## 1-last_digit
loop throught random numbers and print the last number using modulo **% 10** and then compare it if it is greater than 5, equal to zero or less than 6 but not equal to 0
## 2-print_alphabet
printing alphabt from ```a -> z``` using **ASCII** code.  
## 3-print_alphabt
same as the previouse task but this time you ignore a specific character from the alphabt such as *q* or *n*
## 4-print_hexa
loop through out a specific range and convert every range to hex decimals using ``hex`` function
## 5-print_comb2
print numbers 0 to 99 using the pattern of 01 followed by new line.
## 6-print_comb3
combine two list of numbers that their range stand from 0 to 9 e.i ---> ``01, ...89``
## 7-islower
check if the character is lower or uppercase and return either ``True or false``
## 8-uppercase
convert string from lowercases to uppercases using functions ``len, ord, chr``
## 9-print_last_digit
A function that print the last digit using the modulo arthimatic besides the``abs`` function.
## 10-add
function that return an add of two numbers
## 11-pow
function that return the power of two numbers ``5^2 ---> 25``
## 12-fizzbuzz
Perform the FizzBuzz problem.
## 13-insert_number
function that add number into a sorted singly linked list
## 100-print_tebahpla
Print the ASCII alphabet in reverse order, alternating between lowercase and uppercase.
## 101-remove_char_at
Remove a specific character from a string.
## 102-magic_calculation
The magic_calculation function aims to replicate the behavior of the provided Python bytecode. Here's a description of what the bytecode does
```
  3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE

```
