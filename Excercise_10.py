#Group Members 
#Sajal Baral, Shawn Kiruba, Kevin Avila, Shail Patel


user_input = input('Enter a String: ')
second_string = list(user_input)
print(second_string)

lst = []
stop =3

for i in range(0, len(second_string),stop):
    lst.append(second_string[i:i+stop])
print(lst)





