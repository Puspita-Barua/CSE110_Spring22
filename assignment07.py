# -*- coding: utf-8 -*-
"""Assignment_7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wgQuQC5cfuT5X3no4-zJy8iRH94AFN4y
"""

#Task 01

the_list = [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]
for i in range(0,len(the_list)-1):
  for j in range(0,len(the_list)-1-i):
    if the_list[j]>the_list[j+1]:
      holding = the_list[j]
      the_list[j] = the_list[j+1]
      the_list[j+1] = holding

print(the_list)

#Task 02

the_list= [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]
for i in range(0,len(the_list)):
   min = the_list[i]
   min_idx = i
   for j in range(i+1,len(the_list)-1):
     if the_list[j] < min:
       min = the_list[j]
       min_idx = j
   holding = the_list[i]
   hold_idx = i
   the_list[i] = min
   i = min_idx
   the_list[i] = holding
print(the_list)

#Task 03

the_list = [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]
for i in range(0,len(the_list)-1):
   for j in range(0,len(the_list)-1-i):
     if the_list[j]<the_list[j+1]:
       holding = the_list[j]
       the_list[j]=the_list[j+1]
       the_list[j+1]=holding
print(the_list)

#Task 04

sitting_lis = [10,30,20,70,11,15,22,16,58,100,12,56,70,80]
even_lis = []
odd_lis = []
new_sitting_list = []
for i in range(0,len(sitting_lis)):
  if i%2 == 0:
    even_lis.append(sitting_lis[i])
  else:
    odd_lis.append(sitting_lis[i])
for j in range(0,len(even_lis)-1):
  for k in range(0,len(even_lis)-1-j):
    if even_lis[k] > even_lis[k+1]:
      holding = even_lis[k]
      even_lis[k] = even_lis[k+1]
      even_lis[k+1] = holding
for j in range(0,len(odd_lis)-1):
   for k in range(0,len(odd_lis)-1-j):
     if odd_lis[k]<odd_lis[k+1]:
       holding = odd_lis[k]
       odd_lis[k]=odd_lis[k+1]
       odd_lis[k+1]=holding
for i in range(0,len(even_lis)):
   new_sitting_list.append(even_lis[i])
   new_sitting_list.append(odd_lis[i])
print(new_sitting_list)

#Task 05

the_students=int(input('please enter total students: '))
list_students=[]

for count in range(0,the_students):
  the_name=input('please enter the name: ')
  CSE110=int(input('please enter the mark: '))
  PHY111=int(input('please enter the mark: '))
  MAT110=int(input('please enter the mark: '))
  list_students.append([the_name,CSE110,PHY111,MAT110])
print(list_students)
code_number=input('please enter your code number: ')

if code_number=="CSE110":
  index=1
elif code_number=="PHY111":
  index=2
elif code_number=="MAT110":
  index=3

for counter in range(0,len(list_students)):
  maximum=list_students[counter][index]
  max_locate=counter
  maximum_list=list_students[counter]

  for i in range(counter+1,len(list_students)):
    if list_students[i][index]>maximum:
      maximum=list_students[i][index]
      max_locate=i
      maximum_list=list_students[i]

  holding = maximum_list
  list_students[max_locate]=list_students[counter]
  list_students[counter]=holding

for count in range(0,len(list_students)):
  print(list_students[count][0])

#Task 06

my_list = [4, 2, 3, 1, 6, 5]
the_new_list=[]
for i in range(0,len(my_list)-1):
    mini=my_list[i]
    min_index=i

    for j in range(i+1,len(my_list)):
        if (my_list[j]<mini):
          mini=my_list[j]
          min_index=j

    if (mini!=my_list[i]):
      holding=mini
      my_list[min_index]=my_list[i]
      my_list[i]=holding
      the_new_list.append(holding)
      the_new_list.append(my_list[min_index])
print(len(the_new_list))

#Task 07

numeral_1=int(input('please enter the number: '))
list_01=[]
for counter in range(0,numeral_1):
  user_01=int(input('please enter the value: '))
  list_01.append(user_01)
numeral_2=int(input('please enter the number: '))
list_02=[]
for counter in range(0,numeral_2):
  user_02=int(input('please enter the value: '))
  list_02.append(user_02)

previous_list=list_01+list_02
sorting_list=sorted(previous_list)
print("Sorted list=",sorting_list)

length=len(sorting_list)
if length%2!=0:
  the_median = (sorting_list[length//2])
else:
  the_median = (sorting_list[length//2-1]+sorting_list[length//2])/2
print("Median =",the_median)

#Task 8

numeral=int(input('please enter the number: '))
list_1=[]

for index in range(0,numeral):
  user=int(input('please enter the value: '))
  list_1.append(user)
print(list_1)

mini_sum=abs(list_1[0]+list_1[1])
num_1=0
num_2=1

for i in range(0,len(list_1)-1):
  for j in range(i+1,len(list_1)):
    if(abs(list_1[i]+list_1[j])<mini_sum):
      mini_sum=abs(list_1[i]+list_1[j])
      num_1=list_1[i]
      num_2=list_1[j]
print("Two pairs which have the smallest sum =",num_1,"and",num_2)

#Task 09

import math
the_points = [(1,7), (4,5), (-1,7), (-2,0), (1,1), (5,-1)]
minimum_dis=math.inf
minimum_point=[]
for i in the_points:
  distance=math.sqrt(i[0]**2+i[1]**2)
  if distance<minimum_dis:
    minimum_dis=distance
    minimum_point=i
print("Minimum distance=",minimum_dis)
print("Here the closest point is",tuple(minimum_point),"which has a distance of",minimum_dis,"from the origin")