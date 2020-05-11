import math

while True:
      try:
            x = float(input("input x:"))
            y = float(input("input y:"))
            break
      except ValueError:
            print ("please enter a valid value for x and y")

if x > 0 and y > 0:
      print ("at quadrant one")
elif x < 0 and y > 0:
      print ("at quadrant two")
elif x <0 and y <0:
      print ("at quadrant three")
elif x > 0 and y <0:
      print ("at quadrant four")
else:
      print ("at origin")


def coordinate():
      while True:
            try:
                  x = float(input("input x:"))
                  y = float(input("input y:"))
                  break
            except ValueError:
                  print ("please enter a valid value for x and y")
                  
      if x >0 and y > 0:
            print ("at quadrant one")
      elif x < 0 and y > 0:
            print ("at quadrant two")
      elif x <0 and y <0:
            print ("at quadrant three")
      elif x > 0 and y <0:
            print ("at quadrant four")
      else:
            print ("at origin")
coordinate()