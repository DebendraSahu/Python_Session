# Problem
# Add big Number
# We have a list of single digit positive numbers. This list is representation of digits of a large number,
# with 0th element being the most significant digit and nth element being the least significant digit.
# Your program need to add one to the number being represented while keeping the digits in list form.

# Solution

big_number_digits = [1, 3, 5, 0, 7, 4, 5, 8, 3, 7, 9, 4, 2, 7, 6, 9, 5]
addend = 1
carry = addend
result = []
for digit in reversed(big_number_digits):
    new_digit = digit + carry
    carry = new_digit // 10  # removed ones digit
    result.insert(0, new_digit % 10)  # taken ones digit

while carry > 0:
    result.insert(0, carry % 10)
    carry = carry // 10

print(big_number_digits.__str__() + " + " + addend.__str__() + " =")
print(result)
