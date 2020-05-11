'''
4(a) Write a Python program that gets a string containing a person’s first,
middle, and last names, and then display their first, middle,
and last initials. For example, if the user enters John William Smith,
the program should display J. W. S.
'''

#step 1 : Get the Full name of the User

print ("This is a program to generate the initials of your name.\n")
firstname = input("What's your First Name ? \n")

middlename = input("What's your Middle Name ? \
If you do not have a middle name input nil \n")

if (middlename == "nil"):
      middlename = " "

lastname = input("What's your Last Name ? \n")

#step 2 : Output the initials 

#s.find = is used to find a smaller string in a larger string
#s[0] will find the letter that sits in that position

first = str(firstname[0])
middle = str(middlename[0])
last = str(lastname[0])


# Step 3: convert to upper case

upfirst = first.upper()
upsecond = middle.upper()
uplast = last.upper()

#Step 4 : print

if upsecond == " ": 
      print (upfirst + "." + uplast + ".")

else:
      print (upfirst + "." + upsecond + "." + uplast + ".")
      
      


