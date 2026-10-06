numbers = [10,2,3,5,4,3,6,2,5,6,2,5,7,3]

i = 0
while i < len(numbers):
     print(numbers[i])
    i +=1

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


print ('=' * 50)



key=['password']

tr= str(input('please enter your password:\n'))
k=1

while tr not in key :

 print (f'your {k} guess is wrong please try again: ')
 k +=1
 tr= input()
else :
 print (f'u got the password correct in the {k} try')



print ('=' * 50)


peoples=['mohamed','ddddd','mmm']
jobs=['html','css','js']

for people in peoples:
  print (f" {people}'s skills are : ")
  for job in jobs
   print ( f'-{job} ')



print ('=' * 50)


def message(a,b,c){

  print (f'hello {a}')
  print (f'hello {b}')
  print (f'hello {c}')

}

print (f'{message(a)}')
print (f'{message(a)}')
print (f'{message(a)}')

print ('=' * 50)

def task(*names,**skills):
 for name in names:
   print(f'hi {name} your skills are:') 
   for skill in skills:
      print(f'#{skill} => {skills[skill]}')
 task('moh','ff','ffffff',python=20,php=50)
