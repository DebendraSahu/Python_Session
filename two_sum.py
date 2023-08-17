# Problem
# Given an array of integers nums and an integer target, return two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Solution
# Converts a list of numbers to a dictionary where the keys are indices and the values are numbers.
def convert_list_to_dictionary(numbers):
    numbers_dictionary = {}
    for index, number in enumerate(numbers):
        numbers_dictionary[index] = number  # Storing index as the key and value as number.
    return numbers_dictionary


# Finds a pair of numbers from list that add up to the target.
def run(numbers, target):
    numbers_dictionary = convert_list_to_dictionary(numbers)  # Converted list to Dictionary
    for first_value in numbers:
        second_value = target - first_value
        if second_value in numbers_dictionary:  # Check if the calculated second value exists in the numbers_dictionary.
            return first_value, second_value
    return None


# Test the run() function with a sample input.
pair = run([2, 3, 4, 9, 10, 8, 5, 6], 8)
print("Pair is " + str(pair))

# Checking run() function with assert.
# assert run([2, 3, 4, 9, 10, 8, 5, 6], 8) == (2, 6)
print("Worked Well")
