# Read through a file and sum all of the numbers that appear using regular expressions.

import re

# open the file
fname = "/Users/mashrufhossain/Desktop/Seed of Life 2.0/JTC/VS Code Projects/Completed Python Excercises/regex_sum.txt"
handle = open(fname)

total = 0
for line in handle:
    nums = re.findall(r'[0-9]+', line)  # find all digit groups
    for n in nums:
        total += int(n)  # convert and add

print("Sum:", total)
