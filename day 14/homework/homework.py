# codewars ამოხსები

def multiply(a, b):
    return a*b

def even_or_odd(number):
    if number %2 == 1:
        return "Odd"
    else:
        return "Even"
    
def number_to_string(num):
    return str(num)

def opposite(number):
    return number * -1

def solution(string):
    return string[::-1]

def make_negative( number ):
    if number > 0:
        return number * -1
    else:
        return number
    
def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"
    
def positive_sum(arr):
    sum_of_positives = 0
    for num in arr:
        if num > 0:
            sum_of_positives += num
    return sum_of_positives

def repeat_str(repeat, string):
    return repeat * string

def remove_char(s):
    return s[1:-1]

def square_sum(numbers):
    my_sum = 0
    for num in numbers:
        my_sum += num ** 2
    return my_sum

def find_smallest_int(arr):
    return min(arr)

def summation(num):
    my_sum = 0
    for i in range(1,1+num):
        my_sum+=i
    return my_sum