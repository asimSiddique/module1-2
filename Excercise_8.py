#Group Members 
#Sajal Baral, Shawn Kiruba, Kevin Avila, Shail Patell
#Methods such as not in list are from phyton loop documentations. 


my_list =[]
second_list = []
for i in range(10):
    user_input = int(input("Enter a number "))
    if user_input in my_list :
        my_list.remove(user_input)
        second_list.append(user_input)
    else:
        if(user_input not in second_list):
            my_list.append(user_input)
print(my_list)

