#Group Members 
#Sajal Baral, Shawn Kiruba, Kevin Avila, Shail Patel


number = input('Enter a number ')
number= int(number)
my_list = []

for i in range(number):
    
    user_number= input("Enter a number ")
    user_number = float(user_number)
    my_list.append(user_number)

print(f'List : {my_list}')

sum = 0.0
counter=0
for elem in my_list:
    sum = sum+elem
    counter = counter+1
print (f'Average = {sum/counter}')






