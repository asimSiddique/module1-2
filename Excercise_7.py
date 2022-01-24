#Group Members 
#Sajal Baral, Shawn Kiruba, Kevin Avila, Shail Patel

my_list=[]
second_list =[]

while True:
    user_input = (input('Enter a number or Quit to quit '))
    if user_input == "Quit":
        break
    else:
        user_input = int(user_input)
        my_list.append(user_input)

for i in my_list:
    if i % 2 ==0:
        second_list.append(i)

print(second_list)











