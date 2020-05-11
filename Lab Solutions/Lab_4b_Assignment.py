'''
(b) Write a Python program that asks the user to enter a series of
single-digit numbers with nothing separating them.
The program should display the sum of all the single digit numbers
in the string. In addition, the sum should be displayed in
the format of 10-digit width and right alignment.
For example, if the user enters 2514, the method should return “ 12”,
which is the sum of 2,5,1, and 4.

'''

# Step 1 : Input the number 
number = str(input("Input a series of single digit number with nothing \
seperating them :  \n "))

#Step 2 : Seperate the number
'''
for digits in number:
      print (sum(int(digits)))
'''

def sum_digits(number):
      return sum(int(x) for x in number if '0' <= x <= '9')

print (sum_digits(number))