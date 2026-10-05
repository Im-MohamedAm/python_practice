numbers = [10,2,3,5,4,3,6,2,5,6,2,5,7,3]

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

print(f'{type(numbers)} is finished')

print ('=' * 50)

mybooklist=[]
print ('please fill your  book list')

i=0
while len(mybooklist) >= 0 :
   book= str(input('please enter a book name :'))
   mybooklist.insert(i,book)
   answer= input('do u want to add another book name? choose yes or no \n')
   if (answer == 'y' or answer == 'yes') :
     i +=1
   else:
     break
print(f'your book list is finished and here what did u chose : {mybooklist}')
