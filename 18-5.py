"""
1. Even Number Break
   - Write a loop that iterates from 0 to 20. 
   Break the loop when the number is 10. Print all the numbers before the loop breaks.

2. Odd Number Continue
   - Write a loop that iterates from 0 to 20. 
   Use continue to skip even numbers and print only the odd numbers.

3. Prime Number Break
   - Write a loop to find the first prime number greater than 100. 
   Break the loop once you find that prime number and print it.

4. List Search with Break
   - Given a list of numbers, write a loop to search for the number 15.
     If found, print "Found 15" and break the loop.

5. List Filtering with Continue
   - Given a list of numbers, write a loop to print all numbers greater than 50, 
   skipping those less than or equal to 50 using continue.

6. Pass in a Loop
   - Write a loop from 0 to 10. If the number is 5, use pass to do nothing. 
   Otherwise, print the number.

7. Nested Loop Break
   - Write a nested loop (loop inside a loop) that iterates from 0 to 5 for both loops.
     Break the inner loop when the sum of the indices is 5, and print the indices.

8. Nested Loop Continue
   - Write a nested loop that iterates from 0 to 3 for both loops.
     Use continue in the inner loop if the product of the indices is even, 
     and print the indices otherwise.

9. Break in While Loop
   - Write a while loop that keeps asking for user input.
     Break the loop if the user types "exit".

10. Using Pass for Future Implementation
    - Create a loop that iterates over a list of strings. 
    If a string is "TODO", use pass as a placeholder for future implementation.
      Print the other strings. """


# Write a loop that iterates from 0 to 20. 
# Break the loop when the number is 10. Print all the numbers before the loop breaks.

# for i in range(21):
#   if i==10:
#     break
#   print(i)


#  - Write a loop that iterates from 0 to 20. 
#  Use continue to skip even numbers and print only the odd numbers


# for i in range(21):
#   if i%2==0:
#     continue
#   print(i)

#Write a loop to find the first prime number greater than 100. 
#Break the loop once you find that prime number and print it.

# for i in range (100,1000):
#   c=0
#   for j in range(1,i):
#     if i%j==0:
#       c+=1
#   if c<2:
#     print(i)
#     break

#Given a list of numbers, write a loop to search for the number 15.
   #  If found, print "Found 15" and break the loop.

# l=[1,4,6,4,15,19]
# for i in l:
#   if i==15:
#     print("found ",i)
#     break


# Given a list of numbers, write a loop to print all numbers greater than 50, 
# skipping those less than or equal to 50 using continue.

# l=[1,52,34,67,50,58,91,45,81]
# for i in l:
#   if i <=50:
#     continue
#   print(i)

#Write a loop from 0 to 10. If the number is 5, use pass to do nothing. 
#Otherwise, print the number.

# for i in range(11):
#   if i ==5:
#     pass
#   else:
#     print(i)



#Write a nested loop (loop inside a loop) that iterates from 0 to 5 for both loops.
#  Break the inner loop when the sum of the indices is 5, and print the indices.

# for i in range(6):
#   for j in range(6):
#     if i+j == 5:
#       print(i,j)
#       break


# Write a nested loop that iterates from 0 to 3 for both loops.
#  Use continue in the inner loop if the product of the indices is even, 
 #    and print the indices otherwise.

# for i in range(4):
#     for j in range(4):
#         m=i*j
#         if m%2!=0 or m ==0:
#            continue
#         print(i,j)


# Write a while loop that keeps asking for user input.  
# Break the loop if the user types "exit".


# while(1):
#   i = input("please enter any value :")
#   if i =="exit":
#     break

#Create a loop that iterates over a list of strings. 
# If a string is "TODO", use pass as a placeholder for future implementation.
#  Print the other strings.

# l= ["que","norton","init","TODO","wasp","kill"]
# for i in l:
#   if i == "TODO":
#     pass
#   else:
#     print(i)