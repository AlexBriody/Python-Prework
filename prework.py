# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 

# Creates the function "hello_name" which takes in the parameter "user_name"
def hello_name(user_name):
    # Creates a blank line for spacing
    print(" ")
    # Prints the parameter, namely the user name, between the two strings, in two concatenations
    print("Hello " + user_name + "!")

# Calls on the function "hello_name" and passes the name "Meg" as the parameter into the function
hello_name("Meg")

# Creates a blank line for spacing
print(" ")


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

# Creates a function called "first_odds"
def first_odds():

    # Creates a for loop iterating over all the numbers, in steps of 2, in the range of 1 to 100 (exclusive of 101) and prints each number
    for number in range(1, 101, 2):
        print(number)

# Creates the string message shown between the double quotation marks
print("The odd numbers from 1 to 100 are:")

# Calls upon the function "first_odds"
first_odds()


# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

# Creates the function "max_num_in_list" passing in a list parameter "a_list"
def max_num_in_list(a_list):

    # Makes the first element of the list the temporary maximum number
    temp_max = a_list[0]

    # For loop iterating over each number "num" of the list "a_list"
    for num in a_list:

        # If statement that says if the next number "num" of the list "a_list" is greater than the temporary maximum number, then it becomes the new temporary maximum number
        if num > temp_max:
            temp_max = num

    # Upon completion of the for loo, this assigns the temporary maximum number "temp_max" to the variable "max_num" , designating it as the maximum number
    max_num = temp_max

    # Returns the maximum number "max_num" from this function
    return max_num

# Define a list of numbers
number_set = [53, 12, 35, 54, 87, 32]

# Creates a blank line for spacing
print(" ")

# First part prints the string message, which includes the list
# Second part prints the return value (the maximum value)when the function "max_num_in_list" is called with the list "number_set" passed into it
print("The maximum number in the list -", number_set, "- is" , max_num_in_list(number_set))

# Creates a blank line for spacing
print(" ")


# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

# Creates a function named "is_leap_year" to determine if the parameter "a_year" is a leap year
def is_leap_year(a_year):

    # If the year "a_year" passed into the function is divisble by 4, then it's a leap year
    # However, it also has to satisfy one of two conditions: That the year is not divisible by 100 (If it is divisble by 100, it's NOT a leap year, but....)
    # But, if it is divisble by 100 but divisible by 400, then IT IS a leap year
    
    
    if a_year % 4 == 0 and (a_year % 100 != 0 or a_year % 400 == 0 ):

        # Boolean values are returned by this function: True if it is a leap year
        return True
    else:

        # If year doesn't satisfy the first condition AND one of the second in the parenthesis, it is not a leap year, and so the boolean value of False is returned
        return False

# Testing to see if year 2020 is a leap year
year = 2020

# First part: Prints "The year (year in question) is a leap year?" and a true or false value (boolean)
# Second part: Calls on the "is_leap_year" function and passes in the "year" for calculations in if/else statement
print("The year" , year, "is a leap year? " , is_leap_year(year))

# Creates a blank line for spacing
print(" ")


# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. The return should be boolean Type.

# Creating a function that accepts a list "a_list" as a parameter
def is_consecutive(a_list):

    # For loop iterating over the list, excluding the last one because the last number is referenced in the "i + 1"

    for i in range(len(a_list)-1):
        # If statement testing if any of the next number (i + 1) minus the current number (i) doesn't equal to 1, then the numbers aren't consecutive and the boolean value of false is returned
        if a_list[i + 1] - a_list[i] != 1:
            return False
    # If all the next number (i + 1) minus the current number (i) equal to 1, then the boolean value of true is returned because the numbers are consecutive
    return True

# Creating the two number lists
numbers_list1 = [10, 11, 13, 14, 15]
numbers_list2 = [15, 16, 17, 18, 19]

# First part prints the string message, which includes list 1
# Second part calls on the function "is_consecutive" and passes in the list and a boolean value is returned
print("The numbers in list 1 -" , numbers_list1, "- are consecutive numbers?", is_consecutive(numbers_list1))

# First part prints the string message, which includes list 2
# Second part calls on the function "is_consecutive" and passes in the list and a boolean value is returned
print("The numbers in list 2 -" , numbers_list2, "- are consecutive numbers?", is_consecutive(numbers_list2))

# Creates a blank line for spacing
print(" ")

