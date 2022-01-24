#Group Members 
#Sajal Baral, Shawn Kiruba, Kevin Avila, Shail Patel



list_one = []
list_two = []
list_three =[]
for i in range(0,5):
    number = int(input('Enter a number for first list '))
    list_one.append(number)


for i in range(0,5):
    number = int(input('Enter a number for Second list '))
    list_two.append(number)

for i in list_one:
    if i in list_two:
        list_three.append(i)
print(list_three)





