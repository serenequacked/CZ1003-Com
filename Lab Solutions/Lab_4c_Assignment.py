'''
(c) Write a Python program that reads a string from the user containing
a data in the form of dd/mm/yyyy, e.g., 12/03/2016.
The program should print the date in the form of 12 Mar, 2016

'''
import time

date = str(input("Enter any date in the form dd/mm/yyyy: \n" ))

day = int(date[0:2]) 
month = int(date[3:5]) -1
year = int(date[6:])

# print (day, month, year)

allmonth = ["Jan" , "Feb", "Mar" , "Apr" , "May", "Jun"," Jul" , "Aug", "Sep" , "Oct"," Nov", "Dec"]

namemonth = allmonth[month]
# print (namemonth)

print ("Okay the date is :", str(day) +" "+ namemonth+", " + str(year))