# even num in a list 

# list = [2,4,5,8,3]
# for i in list :
#   if i % 2 == 0:
#     print(i)

# Count positive and negative numbers in a list

# list = [ 1,-3,4,5,-7,9,2]
# positive = 0
# negative = 0
# for i in list:
#   if i>0:
#     positive+=1
#   elif i<0:
#     negative+=1
#   else :
#     print("enter a non zer integer")

# print("no of positive nums in the list:",positive)
# print("no of negative nums in the list:",negative)

# MAx an min num in the list

# list=[45,67,89,101,25,33]
# max=list[0]
# min=list[0]

# for i in list:
#   if i>max:
#     max=i
#   if i<min:
#     min=i

# print("max is :",max)
# print("min is ", min)

# Filter  odd numbers from the list

# l = [23,34,56,47,31,75,88]
# odd = []
# for i in l:
#  if i % 2 != 0:
#   odd.append(i)
# print(odd)

# find duplicate numbers in a list

l = [23,56,78,98,88,23,67,78]
for i in range(len(l)):
  d=0
  for j in range(len(l)):    
    if l[i] == l[j]:
      d+=1
if d>=2:
   print(l[i],"has duplicates")


