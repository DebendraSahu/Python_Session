# Problem
# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
# For example:
#
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...
#
#
# Example 1:
#
# Input: columnNumber = 1
# Output: "A"
#
# Example 2:
# Input: columnNumber = 28
# Output: "AB"
#
#
# Example 3:
# Input: columnNumber = 701
# Output: "ZY"

# Solution
def run(column_number):
    # Create a dictionary to map integers to characters ('A' to 'Z')
    alphabet_dict = {i: chr(64 + i) for i in range(1, 27)}

    # Initialize an empty string to store the column name
    column_name = ''

    # Iterate while column_number is greater than 0
    while column_number > 0:
        # Calculate the remainder of column_number divided by 26
        char_index = column_number % 26

        # If char_index is not 0, append the corresponding character to column_name
        if char_index != 0:
            column_name = alphabet_dict[char_index] + column_name
        else:
            # If char_index is 0, append 'Z' to column_name (last character)
            column_name = alphabet_dict[26] + column_name

        # Update column_number to the next set of characters
        column_number = (column_number - 1) // 26

    return column_name


print("test cases")
assert run(1) == "A"
assert run(28) == "AB"
assert run(701) == "ZY"
print("All test cases passed")

x = 1
column_array = []
while x < 100:
    column_array.append(run(x))
    x = x + 1
print(column_array)
