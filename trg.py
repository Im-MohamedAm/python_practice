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

print ('=' * 50)


def xxx(y):
    if len(y) == 1:
        return y
    if y[0] == y[1]: #wwwoorrrlldd
       
        return xxx(y[1:])
    else:
          return y[0] + xxx(y[1:])
print(xxx("wwwooorrrlllddd"))






def show_info(name, role):
    print(f"name: {name}\nrole: {role}")


show_info('mohamed', 'master')
print('=' * 50)


def multiply(n1, n2):
    return n1 * n2


print(multiply(6, 7))
print('=' * 50)


def welcome(name):
    print(f"hello {name}!")


welcome('mohamed')
print('=' * 50)


def show_names(*names):
    for name in names:
        print(name)


show_names('gggg', 'ggggggggggg', 'ffffffffff')
print('=' * 50)


names = ['lllll', 'kkkkk', 'qqqqqq']


def introduce(n1, n2, n3):
    print(n1)
    print(n2)
    print(n3)


introduce(*names)
print('=' * 60)


def greet(name='guest'):
    print(f'Hello {name}')


greet()
greet('mohamed')
print('=' * 50)


def show_skills(**skills):
    for skill, score in skills.items():
        print(f'{skill}: {score}')


show_skills(js=60, php=70, go=80)


message1 = 'global'


def f1():
    message2 = 'internal'
    print(f'the message is: {message2}')


def f2():
    message3 = 'external'
    print(f'the message is: {message3}')


f1()
f2()
print(f'the global message is: {message1}')
print('=' * 50)


def countdown(n):
    for number in range(n, 0, -1):
        print(number)


countdown(10)
print('=' * 50)


square = lambda x: x * x
print(square(5))

print('end.')
