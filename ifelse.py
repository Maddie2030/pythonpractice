# Leap year checker

y = int(input("enter the year:\t"))

if  y > 0 :
  leap = "False"
  if y % 4 == 0 :
    leap = "True"
    if y % 100 == 0 :
      leap = "False"
      if y % 400 == 0 :
        leap = "True"
  print(leap)      
else :
  print("invalid number")

