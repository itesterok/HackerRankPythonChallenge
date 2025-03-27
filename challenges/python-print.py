# Challenge: https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true
#
# Check Tutorial tab to know how to to solve.
#
# The included code stub will read an integer, , from STDIN.
#
# Without using any string methods, try to print the following:
#
#
# Note that "" represents the consecutive values in between.
#
# Example
#
# Print the string .
#
# Input Format
#
# The first line contains an integer .
#
# Constraints
#
#
# Output Format
#
# Print the list of integers from  through  as a string, without spaces.
#
# Sample Input 0
#
# 3
# Sample Output 0
#
# 123
import sys

if __name__ == '__main__':
    n = int(input())
    print('123', end="")
    if n < 4: sys.exit()

    next_element = 4
    for i in range(4, n + 1):
        print(i, end="")
