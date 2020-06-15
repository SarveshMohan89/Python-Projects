# Finding Numbers in a Haystack

# In this assignment you will read through and parse a file with text and
# numbers. You will extract all the numbers in the file and compute the sum of
# the numbers.

# Data Files
# We provide two files for this assignment. One is a sample file where we give
# you the sum for your testing and the other is the actual data you need to
# process for the assignment.

import re
file=open('regex_sum_419680.txt', 'r')

a=0

for lin in file:
    num=re.findall('[0-9]+', lin)
    for numb in num:
        a=a + int(numb)

print (a)        
