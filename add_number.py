# Problem
# Add two big Numbers
# You are given two large positive numbers represented as lists of their individual digits,
# With 0th element being the most significant digit and nth element being the least significant digit.
# Your program need to add both numbers and returns the sum as a list of digits.

# Solution
# Function to add two big numbers represented as lists of digits
def add_big_numbers(first_digits, second_digits):
    # Initialize indexes for iterating through digits in reverse order
    first_digit_index = len(first_digits) - 1
    second_digit_index = len(second_digits) - 1

    # Determine the number of iterations required based on the longer number
    iteration_count = max(first_digit_index, second_digit_index) + 1
    carry = 0  # Initialize carry for addition
    added_digits = []  # List to store the sum of digits

    # Iterate through digits and perform addition
    while iteration_count or carry > 0:
        # Retrieve digits from each number, considering if any digits remain
        first_digit = first_digits[first_digit_index] if first_digit_index >= 0 else 0
        second_digit = second_digits[second_digit_index] if second_digit_index >= 0 else 0

        # Update digit indexes for the next iteration
        first_digit_index -= 1
        second_digit_index -= 1

        # Perform addition of digits along with the carry
        new_digit = first_digit + second_digit + carry
        carry = new_digit // 10  # Calculate the carry for the next iteration
        added_digits.insert(0, new_digit % 10)  # Store the least significant digit

        # Decrease the iteration count
        iteration_count -= 1

    return added_digits  # Return the list of sum digits


# Given numbers represented as lists of digits
first_number_digits = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 9, 9, 9, 9, 9, 9, 9, 9, 9, 5, 9]
second_number_digits = [1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 1, 1, 1, 1, 1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1]

# Print the given numbers
print(first_number_digits)
print("+")
print(second_number_digits)
print("______________________________________________________________________________________________")

# Calculate and print the sum using the add_big_numbers function
print(add_big_numbers(first_number_digits, second_number_digits))
