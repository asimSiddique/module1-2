#Group Members 
#Sajal Baral, Shawn Kiruba, Kevin Avila, Shail Patel
#Get a string. separate uppercase and lowercase into separate lists. merge them together and print out a string.

from curses.ascii import *

user_input = input("Enter a String: ")
upperList=[]
lowerList=[]

for elements in user_input:
    if elements.isupper():
        upperList.append(elements)
    if elements.islower():
        lowerList.append(elements)

mergedList = lowerList+upperList
new_string=""
for elem in mergedList:
    new_string+=elem
print(new_string)
