# -*- coding: utf-8 -*-
"""Assignment_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zwSciQwl9sjI9QEx_H03PE15Pmvc2x5P

# CSE110 Lab Assignment 4 (List)

This Assignment is to help you develop your concept of Lists in Python.

**<font color='red'>[Please follow variable naming conventions including using meaningful variable names for all the tasks]</font>**\
<font color='red'>When you run your code, please make sure your outputs exactly match the sample outputs for each of the sample inputs given. Check if your code works for other valid inputs not given in the samples.</font>

## Write the code in Python to do the following tasks:

##Write your name, student ID and CSE110 theory section number below:
"""

#Write your name, student ID and theory section number below:
#Student Name: Puspita Barua
#Student ID: 21201359
#CSE110 Theory Section No: 08

"""### Task 1
Write a Python program that reads 5 numbers from the user into a list. After reading each number, print all the numbers that have been entered so far in the list.

**Example:**\
If the user enters 3, prints “Numbers in the list: [3]”\
If the user enters 5 next, prints “Numbers in the list: [3, 5]”\
If the user enters 34, prints “Numbers in the list: [3, 5, 34]”\
If the user then enters -11, prints “Numbers in the list: [3, 5, 34, -11]”\
Finally, if the user enters 0 as the last number, prints “Numbers in the list: [3, 5, 34, -11, 0]”
"""

#todo

list_1= []
for i in range(0,5):
  user=int(input("Enter the number:" ))
  list_1.append(user)
  print("Numbers in the list:", list_1)

"""### Task 2

Write a Python program that takes a list as an input from the user, then creates a new list excluding the first and last two elements of the given list and prints the new list. If there are not enough elements in the list to do the task, print "Not possible".

**Note:** You may use list slicing.

===================================================================

**Sample Input 1:**<br/>
[10, 20, 24, 25, 26, 35, 70]<br/>

**Sample Output 1:**<br/>
[24, 25, 26]<br/>

===================================================================

**Sample Input 2:**<br/>
[10, 20, 24, 25, 26]<br/>

**Sample Output 2:**<br/>
[24]<br/>

===================================================================

**Sample Input 3:**<br/>
[10, 20, 24, 25]<br/>

**Sample Output 3:**<br/>
[]<br/>

===================================================================

**Sample Input 4:**<br/>
[10, 20, 24]<br/>

**Sample Output 4:**<br/>
Not possible<br/>

===================================================================
"""

#todo

n=int(input())
list_1= []
for i in range(0,n):
  user=int(input("Enter the number:"))
  list_1.append(user)
print(list_1)
l=len(list_1)
if l>3:
  print(list_1[2:-2])
else:
  print("Not possible")

"""### Task 3

Write a python program that reads 5 numbers from the user into a list, and then prints them in the reverse order.

*Hint: You may create a list to store the input numbers and then use loop to print them in reverse order*

===================================================================

**Sample Input:**\
5\
-5\
100\
1\
0

**Sample Output:**\
Input data: [5, -5, 100, 1, 0]\
Printing values from the list in reverse order:\
0\
1\
100\
-5\
5

===================================================================
"""

#todo

list_1= []
for i in range(0,5):
  user=int(input("Enter the number:" ))
  list_1.append(user)
print("Input data:",list_1)
print("Printing values from the list in reverse order:")
lenght=len(list_1)
for j in range(lenght-1,-1,-1):
   print(list_1[j])

"""### Task 4

Write a Python program that turns every item of a list into its square. [Your program should work for any lists; make changes to the lists below and check whether your program works correctly]

===================================================================

**Given list 1:**\
[1, 2, 3, 4, 5, 6, 7]

**Sample Output 1:**\
[1, 4, 9, 16, 25, 36, 49]

===================================================================

**Given list 2:**\
[3, 5, 1, 6]

**Sample Output 2:**\
[9, 25, 1, 36]


===================================================================






"""

#todo

list_1 = [1, 2, 3, 4, 5, 6, 7]
list_2 = []
lenght=len(list_1)
for i in range(0,lenght):
  j=list_1[i]
  new=j**2
  list_2.append(new)
print(list_2)

"""### Task 5


Write a Python program that removes all Empty strings from a **given list** and prints the modified list. [Your program should work for any given list; make changes to the list below and check whether your program works correctly]

=========================================================================

**Given List:**

["hey", "there", "", "what's", "", "up", "", "?"]

**Sample Output:**

Original List:
['hey', 'there', '', "what's", '', 'up', '', '?']

Modified List:
['hey', 'there', "what's", 'up', '?']

==========================================================================



"""

#todo

given_list=["hey", "there", "", "what's", "", "up", "", "?"]
list_1=["hey", "there", "", "what's", "", "up", "", "?"]
print("Original List:",list_1)
lenght=len(list_1)
n_list=[]
for i in range(0,lenght):
  if list_1[i] != "":
    n_list.append(list_1[i])
print("Modified List:",n_list)

"""### Task 6

Write a Python program that reads a string containing 7 numbers separated by commas, then makes a list of those numbers and prints the **largest number** and its location or index position in the list. <font color='red'>[You are not allowed to use the max(), sort(), sorted() function here]</font>

[Your program should work for any given list; make changes to the list below and check whether your program works correctly]

**Hint:** You may assume the first input to be the largest value initially and the largest value’s location to be 0.

**Note:** You may need to be careful while printing the output. Depending on your code, you might need data conversion.

===================================================================

**Sample Input:**\
 "7, 13, 2, 10, 6, -11, 0"

**Sample Output:**\
My list: [7, 13, 2, 10, 6, -11, 0]\
Largest number in the list is 13 which was found at index 1.

===================================================================
"""

#todo

s_list= "7, 13, 2, 10, 6, -11, 0"
list_1=s_list.split(",")
lenght=len(list_1)
n_list=[]
for i in range(0,lenght):
  n_list.append(int(list_1[i]))
print("My list:",n_list)
max=n_list[0]
for j in range(1,lenght):
  if max<n_list[j]:
    max=n_list[j]
    index=j
print("Largest number in the list is", max, "which was found at index", index)

"""## Task 7

Suppose you have been given two lists. Write a Python program that replaces the last element of the first list with the second list. [Your program should work for any two given lists; make changes to the lists below and check whether your program works correctly]


===================================================================

**Sample given lists 1:**\
List_one : [1, 4, 7, 5]\
List_two : [6, 1, 3, 9]

**Sample Output 1:**\
[1, 4, 7, 6, 1, 3, 9]

===================================================================

**Sample given lists 2:**\
List_one : [1, 3, 5, 7, 9, 10]\
List_two : [2, 4, 6, 8]

**Sample Output 2:**\
[1, 3, 5, 7, 9, 2, 4, 6, 8]

===================================================================




"""

#todo

List_one = [1, 4, 7, 5]
List_two = [6, 1, 3, 9]

n_list=List_one[:-1]
print(n_list+List_two)

"""### Task 8
Assume, you have been given two lists. [Your program should work for any two given lists; change the following lists and check whether your program works correctly for the code you have written]

list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9]\
list_two = [10, 11, 12, -13, -14, -15, -16]

Write a Python program that creates a new list with all the **even elements** of both of the given lists and prints the new list.

**Hint:** You may create a third list to store the even elements of the given lists.

===================================================================

**Output for the above lists:** [2, 4, 6, 8, 10, 12, -14, -16]

===================================================================
"""

#todo

list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_two = [10, 11, 12, -13, -14, -15, -16]
new_list=[]
l_1=len(list_one)
l_2=len(list_two)
for i in range(0,l_1):
  if list_one[i]%2==0:
    new_list.append(list_one[i])
for j in range(0,l_2):
  if list_two[j]%2 == 0:
     new_list.append(list_two[j])
print("Output for the above lists:",new_list)

"""### Task 9

Write a Python program that reads a string as an input from the user where multiple numbers are separated by spaces. Then, make a list of numbers from the input string without using the split() function and print the list. Finally, remove all the occurences of **even numbers** from the same input list and print the modified list.


=========================================================================

**Sample Input:**

7 12 4 55 96 2 11 61 33 42

**Sample Output:**

Original list: [7, 12, 4, 55, 96, 2, 11, 61, 33, 42]\
Modified list: [7, 55, 11, 61, 33]

=========================================================================




"""

#todo

user=input()
str_1= ""
list_1 = []
for i in user:
  if i == " ":
    list_1.append(int(str_1))
    str_1= ""
  else:
    str_1=str_1+i
list_1.append(int(str_1))
print("Original list:", list_1)
list_2=[]
for i in list_1:
  if i%2 != 0:
    list_2.append(i)
print("Modified list:",list_2)

"""### Task 10
Write a Python program that reads a string as an input from the user where multiple numbers are separated by commas. Then, make a list of numbers from the input string and print the list. Finally, remove multiple occurences of any numbers from the input list and print the modified list **without duplicate values**.

*Hint: You may create a third list to store the results but you may try doing it in the same input list. You can use membership operators (in, not in) to make sure no duplicates are added.*

===================================================================

**Sample Input 1:**<br/>
0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4<br/>


**Sample Output 1:**<br/>
Input list: [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]\
Modified list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

===================================================================

**Sample Input 2:**<br/>
7, 7, 7, 1, 0, 3, 3, 55, 9<br/>


**Sample Output 2:**<br/>
Input list: [7, 7, 7, 1, 0, 3, 3, 55, 9]\
Modified list: [7, 1, 0, 3, 55, 9]

===================================================================
"""

#to do

u= input("Please enter the numbers:")
list_1= u.split(", ")
print("Input list:",list_1)
for i in range(len(list_1)):
  list_1[i]=int(list_1[i])
n_list= []
for i in list_1:
  if i not in n_list:
    n_list.append(i)
print(n_list)

"""### Task 11
Assume, you have been given two lists: List_one and List_two. [Your program should work for any two given lists; change the following lists and check whether your program works correctly for the code you have written]

Write a Python program that prints "True", if the given two lists have at least one common member. Otherwise, print "False".

Note: Please use concepts of flag and break to solve this task.

===================================================================

**Given lists 1:**\
List_one : [1, 4, 3, 2, 6]\
List_two : [5, 6, 9, 8, 7]

**Sample Output 1:**\
True

===================================================================

**Given lists 2:**\
List_one : [1, 4, 3, 2, 5]\
List_two : [8, 7, 6, 9]

**Sample Output 2:**\
False

===================================================================

"""

#todo

list_1= [1, 4, 3, 2, 6]
list_2= [5, 6, 9, 8, 7]
list_3=[]
list_4=[]
if len(list_1)>=len(list_2):
  list_3=list_3+list_1
  list_4=list_4+list_2
else:
  list_3=list_3+list_2
  list_4=list_4+list_1
for i in list_3:
   if i in list_4:
      flag=True
   else:
      flag=False
print(flag)

"""## Optional Tasks (12-17) [Ungraded]

### Task 12


Write a Python program that reads 7 numbers into a list and prints the **second largest number** and its location or index position on the list. <font color='red'>[You are not allowed to use the max(), sort(), sorted() function here]</font>

===================================================================

**Sample Input:**\
 7, 13, 2, 10, 6, -11, 0

**Sample Output:**\
My list: [7, 13, 2, 10, 6, -11, 0]\
Second largest number in the list is 10 which was found at index 3.

===================================================================
"""

#todo

"""### Task 13

Write a Python program that reads 5 numbers into a list and prints the smallest and largest number and their locations in the list. <font color='red'>[You are not allowed to use the max(), min(), sort(), sorted() functions here]</font>

**Hint:** You may assume the first input to be the largest value initially and the largest value’s location to be 0. Similarly, you can assume the first input to be the smallest value initially and the smallest value’s location to be 0.

**Note:** You may need to be careful while printing the output. Depending on your code, you might need data conversion.

===================================================================

**Sample Input:**\
7, 13, -5, 10, 6

**Sample Output:**\
My list: [7, 13, -5, 10, 6]\
Smallest number in the list is -5 which was found at index 2\
Largest number in the list is 13 which was found at index 1

===================================================================
"""

#todo

"""### Task 14
Write a Python program that takes two lists as an input from the user. Then print a new list with the **common elements** of both the input lists.

*Hint: You may need to create a third list to store the results. You can use membership operators (in, not in) to make sure similar elements are added.*

===================================================================

**Sample Input 1:**<br/>
A, B, C, D


C, E, F, B


**Sample Output 1:**<br/>
['C', 'B']

===================================================================

**Sample Input 2:**<br/>
1, 3, A, H, P


A, G, 1, P, O


**Sample Output 2:**<br/>
['1', 'A', 'P']

===================================================================

"""

# todo

"""### Task 15

Assume, you have been given two lists. [Your program should work for any two given lists; make changes to the lists below and check whether your program works correctly]

list_one = [1, 2 , 2, 4, 5, 5, 7, 99, 200, 303, 70]\
list_two = [1, 1, 2, 3, 3, 3, 4, 5, 200, 500, -5]

Write a Python program that creates a new list with all the **unique elements** of both the given lists.
<font color='red'> **You need to make sure that there are no duplicates in the resulting list.**</font> Finally, print the updated list.

**Hint:** You may create a third list to store the results. You can use membership operators (in, not in) to make sure no duplicates are added.

===================================================================

**Output for the above two lists**:
[1, 2, 4, 5, 7, 99, 200, 303, 70, 3, 500, -5]

===================================================================
"""

# todo

"""### Task 16

Write a python program to take a list as a string input from the user and print it back to the user as a list. Please look at the examples below for clarification.

**<font color='red'>[Must use string split() and strip() functions]</font>**

================================================================

**Sample Input 1:**\
'1, &nbsp; &nbsp;&nbsp; &nbsp; 2  ,&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;3, 50, 4'

**Sample Output 1:**\
Original data: 1, &nbsp; &nbsp;&nbsp; &nbsp; 2  ,&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;3, 50, 4\
After removing square brackets: 1, &nbsp; &nbsp;&nbsp; &nbsp; 2  ,&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;3, 50, 4\
Numbers in string format with extra white spaces: ['1', '&nbsp; &nbsp;&nbsp; &nbsp; 2'  ,'&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;3', '50', '4']\
Final data (numbers in list format): [1, 2, 3, 50, 4]
                
                
================================================================
                
  
**Sample Input 2:**
'[1,&nbsp; &nbsp;&nbsp; &nbsp;2&nbsp; &nbsp;,&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;3, 50, 4]'

**Sample Output 2:**\
Original data: [1,&nbsp; &nbsp;&nbsp; &nbsp;2&nbsp; &nbsp;,&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;3, 50, 4]\
After removing square brackets: 1,&nbsp; &nbsp;&nbsp; &nbsp;2&nbsp; &nbsp;,&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;3, 50, 4\
Numbers in string format with extra white spaces: ['1', '&nbsp; &nbsp;&nbsp; &nbsp;2&nbsp; &nbsp;', '&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;3', '50', '4']\
Final data (numbers in list format): [1, 2, 3, 50, 4]
                
                
================================================================

                
  
**Sample Input 3:**\
"&nbsp; &nbsp;&nbsp; &nbsp;[1,&nbsp; &nbsp;2&nbsp; &nbsp;,&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;3,&nbsp; &nbsp;50,&nbsp; &nbsp;4]&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;"

**Sample Output 3:**\
Original data: &nbsp; &nbsp;&nbsp; &nbsp;[1,&nbsp; &nbsp;2&nbsp; &nbsp;,&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;3,&nbsp; &nbsp;50,&nbsp; &nbsp;4]&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;\
After removing square brackets: 1,&nbsp; &nbsp;2&nbsp; &nbsp;,&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;3,&nbsp; &nbsp;50,&nbsp; &nbsp;4\
Numbers in string format with extra white spaces: [' 1', '&nbsp; &nbsp;2&nbsp; &nbsp;', '&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;3', '&nbsp; &nbsp;50', '&nbsp; &nbsp;4']\
Final data (numbers in list format): [1, 2, 3, 50, 4]

                
================================================================
"""

#todo

"""
### Task 17
Write a Python program that takes a single string as an input from the user where few numbers are separated by commas. Now, make a list with the numbers of the given string.Then your task is to remove multiple occurences of any number and then finally print the list **without any duplicate values**.

*Hint (1): For obtaining the numbers from the string, use split(). For cleaning the data, use strip().*

*Hint (2): You may create a third list to store the results. You can use membership operators (in, not in) to make sure no duplicates are added.*

===================================================================

**Sample Input 1:**<br/>
0, 0, 1, 2, 3, 4,&nbsp;&nbsp; &nbsp;&nbsp; 4, 5, 6, 6, 6,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7, 8, 9, 4,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4<br/>


**Sample Output 1:**<br/>
Given numbers in list: [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]\
List without any dupliacte values: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]<br/>

===================================================================

**Sample Input 2:**<br/>
7, 7, 7, 1, &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0, 3, 3, &nbsp;&nbsp;55, 9<br/>


**Sample Output 2:**<br/>
Given numbers in list: [7, 7, 7, 1, 0, 3, 3, 55, 9]\
List without any dupliacte values: [7, 1, 0, 3, 55, 9]<br/>

===================================================================
"""

#todo