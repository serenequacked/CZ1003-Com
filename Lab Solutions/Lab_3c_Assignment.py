'''
Write a program to generate two tables of currency
conversions from Singapore dollars to US
dollars. Assume the following conversion rate:
1 US dollar(US$) = 1.2008 Singapore dollars (S$)
'''


while True:
      try:
            global start, end ,step
            start = int(input("start S$:"))
            end = int(input("end S$:"))
            step = int(input("step S$:"))
            break
      
      except ValueError:
            print ("please enter valid values for start and end amount")


wallet = list(range(start,end+1))
print (wallet)
sequence = wallet[:end+1:step]
print (sequence)

print ("Table 1 with for")
for money in range(start,end+1,step):
      print ("S$", money, "= US$", money/1.2008) 

print ("Table 2 with while")
money = start
while (money < end+1):
      print ("S$", money, "= US$", money/1.2008)
      money = money + step