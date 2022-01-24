#Group Members 
#Sajal Baral, Shawn Kiruba, Kevin Avila, Shail Patel

stringone = input('Enter the first')

stringTwo = input('Enter the second word')

#if stringone in stringTwo:
#   print('True')
#lif stringTwo in stringone:
#    print('True')
#else:
#    print('False')

if stringTwo.startswith(stringone):
    print('True')
elif stringone.startswith(stringTwo):
    print('True')
else:
    print('False')