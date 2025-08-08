#1.def is_leap(year): """ Determines whether a given year is a leap year.
def is_leap(year):
    """
    Determines whether a given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.

    Parameters:
    year (int): The year to be checked.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    if year <= 0:
        raise ValueError("Year must be a positive integer.")
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

try:
    year_input = int(input("Enter a year: "))
    if is_leap(year_input):
        print(f"{year_input} is a leap year.")
    else:
        print(f"{year_input} is not a leap year.")
except ValueError as e:
    print(f"Error: {e if str(e) == 'Year must be an integer.' else 'Please enter a valid integer.'}")
#2.Conditional Statements Exercise
# Given an integer, n, perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird
try:
    n = int(input("Enter a number: "))
    if not (1 <= n <= 100):
        print("Error: Number must be between 1 and 100 inclusive.")
    else:
        if n % 2 != 0:
            print("Weird")
        elif 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        else:  # n % 2 == 0 and n > 20
            print("Not Weird")
except ValueError:
    print("Error: Please enter a valid integer.")
# 3.Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.
# Give two solutions.
# Solution 1 with if-else statement.
try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    if a > b:
        print("Error: a must be less than or equal to b.")
    else:
        if a % 2 != 0:
            a += 1
        if b % 2 != 0:
            b -= 1
        even_numbers = list(range(a, b + 1, 2))
        print("Even numbers (Solution 1):", even_numbers)
except ValueError:
    print("Error: Please enter valid integers for a and b.")
# Solution 2 without if-else statement.
try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    if a > b:
        print("Error: a must be less than or equal to b.")
    else:
        a = a + (a % 2)  # Round up to next even number
        b = b - (b % 2)  # Round down to previous even number
        even_numbers = list(range(a, b + 1, 2))
        print("Even numbers (Solution 2):", even_numbers)
except ValueError:
    print("Error: Please enter valid integers for a and b.")













