#Group Members 
#Sajal Baral, Shawn Kiruba, Kevin Avila, Shail Patel
# Solution was worked upon as a group. We referenced stackoverflow and programinz.com
#https://www.programiz.com/python-programming/matrix
#https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array

first_number = int(input('Enter a row number from 1 to 5: '))
second_number = int(input('Enter a column number from 1 to 5: '))
matrix = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

matrix[first_number-1][second_number-1]=1

for i in range(5):
    print(matrix[i])



