"""
### 1. Remove Duplicates from a List
Write a Python program that removes duplicates from a list while maintaining the original order.

### 2. Find the Second Largest Number in a List
Write a Python program to find the second largest number in a list.

### 3. Rotate a List by n Positions
Write a Python program to rotate a list by n positions.

### 4. Find Common Elements in Two Lists
Write a Python program to find all common elements between two lists.

### 5. Find the Longest Sublist of Unique Elements
Write a Python program to find the longest sublist of unique elements from a given list.

### 6. Merge Two Sorted Lists
Write a Python program to merge two sorted lists into a single sorted list.

### 7. Find the Intersection of Multiple Lists
Write a Python program to find the intersection of multiple lists.

### 8. Group Elements by Frequency
Write a Python program to group elements in a list by their frequency of occurrence.

### 9. Find the Most Frequent Element in a List
Write a Python program to find the most frequent element in a list.
### 10. Split a List into Sublists of Equal Length
Write a Python program to split a list into sublists of equal length. If the list cannot be divided evenly, the last sublist should contain the remaining elements.

### 11. Reverse Each Word in a List of Strings
Write a Python program to reverse each word in a list of strings while maintaining their order in the list.

### 12. Flatten a Nested List
Write a Python program to flatten a nested list into a single list.

### 13. Find the Cumulative Sum of a List
Write a Python program to compute the cumulative sum of the elements in a list.

### 14. Pairwise Swap Elements of a List
Write a Python program to swap every two adjacent elements in a list. If the list has an odd number of elements, leave the last element as is.

### 15. Find the Longest Increasing Subsequence in a List
Write a Python program to find the longest increasing subsequence in a list of integers.

### 16. Check if a List is a Palindrome
Write a Python program to check if a list is a palindrome (reads the same forward and backward).

### 17. Find the Difference Between Two Lists
Write a Python program to find the elements that are present in the first list but not in the second.

### 18. Replace Elements in a List
Write a Python program to replace all occurrences of a specified value in a list with another value.

### 19. Find All Subsequences of a List
Write a Python program to find all subsequences of a list.

### 20. Group Anagrams from a List of Strings
Write a Python program to group anagrams from a list of strings. Anagrams are words that contain the same characters in different orders.
"""

# Write a Python program that removes duplicates from a list
# while maintaining the original order

# l= [1,3,5,6,5,8,4,8,2]
# l1=[]
# for i in l:
#   if i not in l1:
#     l1.append(i)
# print(l1)



# Write a Python program to find the second largest number in a list.

# l= [1,3,5,6,5,8,4,8,2]
# l1=[]
# for i in l:
#   if i not in l1:
#     l1.append(i)
# l1.sort(reverse="True")
# print("second largest number in the list:",l1[1])

# Write a Python program to rotate a list by n positions.

# l=[1,2,3,4,5]
# p=int(input("enter the input :"))
# for i in range(p):
#   m=l.pop()
#   l.insert(i,m)
# print(l)





# Write a Python program to find all common elements between two lists.

# l= [1,3,5,6,5,8,4,8,2]
# l1=[5,15,8,4,27]
# l2=[]
# l3=[]
# for i in l:
#   if i in l1:
#     l2.append(i)
# k=set(l2)
# l2=list(k)
# print(l2)

#Write a Python program to find
# the longest sublist of unique elements from a given list

# l= [1,3,5,6,5,8,7,4,8,2,1,7,5,6,3]
# m=[]
# for i in range(len(l)):
#   l2=[]
#   l2.append(l[i])
#   ind=0
#   for j in range (i+1,len(l)):
#     if l[j] in l2:
#       break
#     else:
#       if l[i]!=l[j]:
#         l2.append(l[j])
#         ind+=1
#       else:
#         break
#   m.append(l2)
# max1=0
# for i in m:
#   if max1<len(i):
#     max1=len(i)
# for j in m:
#   if len(j)==max1:
#     print(j)

#### Write a Python program to merge two sorted lists into a single sorted list.

# l1=[5,1,3,6,7,8]
# l2=[17,3,5,51,23]
# l1.extend(l2)
# l1.sort()
# print(l1)

#### 