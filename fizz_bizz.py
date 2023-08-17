# Problem
# Loops through numbers from 1 to 100. If a number is divisible by 3, print "Three" in words.
# If a number is divisible by 5, print "Five" in words.
# If a number is divisible by both 3 and 5, print "Fifteen" in words.
# If it is not divisible by any of them, print the number as it is.

# Solution
n = 1
while n <= 100:
    if n % 3 == 0 and n % 5 == 0:
        print("Fifteen")
    elif n % 3 == 0:
        print("Three")
    elif n % 5 == 0:
        print("Five")
    else:
        print(n)
    n += 1

# Solution 2
print("Second Solution")

for number in range(0, 100):
    if number % 3 == 0 and number % 5 == 0:
        print("Fifteen")
    elif number % 3 == 0:
        print("Three")
    elif number % 5 == 0:
        print("Five")
    else:
        print(number)
