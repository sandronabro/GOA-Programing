#Q. 1. What is the function used to display text in Python?
#A. We use a function called print to display text in Python
print("Hello World!")

#Q. 2. In Python, which data type is used to store a whole number?
#A. There are data types such as Integer, String, Float etc. for a whole number we use Integers AKA int
x = 1
print(type(x))

#Q. 3. Which of the following data types is used to store text in Python?
#A. As i said there are data types in Python. We use String aka str to store text.
name = "This is a text"
print(type(name))

#Q. 4. What is the result of the expression 10 + 5 * 2 in Python?
#A. This is just basic math. its 20. If you dont trust me lets see the code
x = 10 + 5 * 2
print(x)

#Q. 5. Which of the following is the correct way to assign the value 42 to a variable named answer in Python? 
#A. The correct way is to just put the varieble followed with the "="" and then the value
varieble = 42
print(varieble)

#Q. 6. What is the process of identifying and fixing errors in a program called?
#A. Identifying and fixing errors is called Debugging in programming. Heres an example.
#step 1. Identify the issue.
def calculate_sum(a, b):
    result = a - b  # Bug: subtraction instead of addition
    return result

num1 = 5
num2 = 3
result = calculate_sum(num1, num2)
print("The sum of", num1, "and", num2, "is: ", result)

#step 2. Fix the bug
def calculate_sum(a, b):
    result = a + b  # Fix: change subtraction to addition
    return result

num1 = 5
num2 = 3
result = calculate_sum(num1, num2)
print("The sum of", num1, "and", num2, "is: ", result)

#step 3. Test and BOOM

#Q. 7. Which is commonly used in Python for naming variables and functions, where words are separated by underscore?
#A. This is called the "snake_case" in python. Its bassically where you separate words with underscores
for_example = "the varieble is separated with underscores"
print(for_example)

#Q. 8. What is the primary purpose of adding comments to your Python code?
#A. The primary purpose of adding comments to Python code is to provide explanation for humans. A Python code cannot execute a comment
# This is a comment
This_is_a_varieble = "This is not a comment"
print(This_is_a_varieble)

#Q. 9. How can you take user input in Python? 
#A. To take an user input in Python we basically use the "input()" function
user_input = input()
print(user_input)

#Q. 10. Which of the following is not a built-in data type in Python? A. str B. int C. float D. array
#A. The answer is D. because array is not a built in data type
# Integer (int):
x = 5
y = -10
# Floating-point (float):
pi = 3.14159
price = 19.99
# String (str):
name = "Alice"
message = 'Hello, world!'
# Boolean (bool):
is_true = True
is_false = False
# List (list):
numbers = [1, 2, 3, 4, 5]
names = ['Alice', 'Bob', 'Charlie']

#Q. 11. What function can be used to check the data type of a variable in Python?
#A. In python we use "type()" to check the data type of a varieble
varieble = "this is a string"
print(type(x))

#Q. 12. How can you convert an integer to a string in Python?
#A. For this we can use the "str()" function
int_varieble = 7
print(str(int_varieble))

#Q. 13. What is the term for converting one data type into another in Python?
#A. We use the term "Converting" for this.
non_converted = 7
converted = str(non_converted)
print(converted)

#Q. 14. Which operator is used to check if two values are equal in Python?
#A. The answer is "==" because it checks if two values are equal. some get it mixed up with "="
print(4 == 8)

#Q. 15. What is the result of the logical AND operation between True and False in Python?
#A. In Python, the logical AND operation is represented by the "and" keyword. When you perform the logical AND operation between True and False, the result is "False"
result = True and False
print(result)

#Q. 16. What will the expression (5 > 3) and (10 < 20) evaluate to in Python?
#A if both conditions are True it will evaluate to "True". In this case it is.
y = (5 > 3) and (10 < 20)
print(y)

#Q. 17. In Python, what is used to make decisions and execute different code blocks based on conditions?
#A. Its the "if" and "else" statement. "if" is used to execute the prgram if the conditions is True. "else" is used if its False
x = 10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

#Q. 18. Which type of loop is used to iterate over a sequence (e.g., a list or string) in Python?
#A. The for loop is used to iterate over a sequence in Python.
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)

#Q. 19. What type of loop is used when you want to repeat a block of code as long as a condition is true?
#A. Like i said: For Loop: Iterates over a sequence. While Loop: Repeats code while a condition is true.
count = 0
while count < 5:
    print(count)
    count += 1

#Q. 20. What does the range() function in Python return?
#A. The range() function in Python returns a sequence of numbers
for i in range(5):
    print(i)

#Q. 21. Which keyword is used to start an "if" statement in Python?
#A. We use the "if" keyword to start and if statement. Come on bro. its in the question
if 3 > 2:
    print("3 is bigger than 2")

#Q. 22. What is the purpose of the "else" statement in Python's "if-else" construct?
#A. else in Python's "if-else" specifies what to do if the initial if condition is false.
x = 10
if x > 0:
    print("x is positive")
else:
    print("x is non-positive")

#Q. 23. Which data structure is used to store an ordered collection of items in Python?
#A. The answer is the "list" data structue
fruits = ["Apple", "Banana", "Orange"]
print(fruits)

#Q. 24. In Python, which index represents the first element of a sequence? 
#A. The first element of a squence is 0
fruits = ["Apple", "Banana", "Orange"]
print(fruits[0])

#Q. 25. How can you access the third element of a list in Python?
#A. In Python, you can access the third element of a list using indexing. List indices start from 0, so the third element would have an index of 2
my_list = [10, 20, 30, 40, 50]
print(my_list[2])

#Q. 26. What does slicing allow you to do with a sequence in Python?
#A.Slicing in Python lets you extract and create a new sequence by specifying start, end, and optional step.
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
slice_result = numbers[2:6]
print(slice_result)

#Q. 27. How can you extract a subsequence of a list from index 2 to index 5 (5 must be included) in Python?
#A. To extract a subsequence of a list from index 2 to index 5 in Python, you can use slicing.
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
subsequence = my_list[2:6]
print(subsequence)

#Q. 28. What does the "step" value in slicing indicate?
#A. In slicing, the "step" value specifies the interval between elements in the range.
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[1:8:2])

#Q. 29. What is a reusable block of code in Python that performs a specific task called?
#A. Its called "Function"
def square(number):
    return number ** 2
result = square(3)
print(result)

#Q. 30. In Python, what are the values passed to a function called? 
#A. In Python, the values passed to a function are called arguments
def greet(name):
    print("Hello", name)
greet("Sandro")

#Q. 31. Which string method is used to convert a string to uppercase in Python?
#A. To turn a string to uppercase we must use the "upper()"" method
text = "text"
text = text.upper()
print(text)

#Q. 32. What list method is used to add an element to the end of a list in Python?
#A. The method that adds elements at the end of the list is called "append()"
fruits = ["Apple", "Banana", "Orange"]
fruits.append("Pineapple")
print(fruits)

#Q. 33. In Python, which keyword is used to define a new function?
#A. We use the "def" keyword to define a new function.
def greet(name):
    print("Hello", name)
greet("Sandro")

#Q. 34. What keyword is used to return a value from a function in Python?
#A. We use the "return" keyword to return a value from a function.
def add_numbers(x, y):
    sum_result = x + y
    return sum_result
result = add_numbers(3, 5)
print(result)