print ("please input birthday of 1st person")
year1 = input("year:")
month1 = input("month:")
day1 = input("day:")

print ("please input birthday of 2nd person")
year2 = input("year:")
month2 = input("month:")
day2 = input("day:")


if year1 > year2:
    print ("person 1 is older")
elif year2 > year1:
    print ("person 2 is older")
else:
      if month1 > month2:
            print("person 1 is older")
      elif month2 > month1:
            print ("person 2 is older")
      else:
            if day1 > day2:
                  print ("person 1 is older")
            elif day2 >day1:
                  print ("person 2 is older")
            else:
                  print ("They are the same age")