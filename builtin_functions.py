'''
print(), len(), input(), round(), 
 abs(), int(), str(), sum()min(), list(),
 dict(), max(),sum(), sorted(),open(), file(),help(), 
 type(), bool(), range(), id(), dir(),
'''

print('print will shows what is happening')
print('sukanya')
print(len('sukanya'))
#so len() will count blank space also.
print(len('sukanya k'))

#len() helps to print number of items in list 
print(len(['potato','curd','milk']))
print(min(10,20,30,40))
print(max(20,30,40,50))
print(sum([1,2,3]))


# variable in python
first_name='Rayaan'
last_name='khaan'
country='india'
city='bangalore'
age=28
is_married=True
skills=['python','java','selenium','javascript','css','html','sql']
personal_info = {
    'first_name':'Rayaan',
     'last_name':'khaan',
     'country':'india',
     'city':'bangalore',
     'age':28,
     'is_married':True,
     'skills':['python','java','selenium','javascript','css','html','sql']}
print('first_name:',first_name)
print('last_name:','khaan')
print('country name:','india')

print('personal_information:',personal_info)


#declairing multiple variables in a line


first_name,last_name,country,age='Rayaan','khaan','india','age'

print('First name:',first_name)
print('Last Name:',last_name)
print('Age:',age)

#checking data type and casting
first_name='Rayaan'
last_name='khaan'
country='india'
city='bangalore'
age=28

#print datatype
print(type('Rayaan'))
print(type(last_name))
print(type('india'))
print(type('bangalore'))
print(type(28))
print(type(True))
print(type(['python','java','selenium','javascript','css','html','sql']))
print(type(personal_info))
print(type((1,2)))
print(type(zip([1,2],[2,2])))



#int to float
num_int=10
print('Number Intiger:',num_int)
num_float=float(num_int)
print('Number Float:',num_float)


#float to int
gravity=9.81
int_num=(int(gravity))
print('intiger number:',gravity)


#int to str
int_num=11
print('intiger num:',int_num)
num_str=str(int_num)
print('string number:',num_str)


#str to int or float
num_str='10.6'
num_float=float(num_str)
print('num_float',num_float)
print(type(num_float))
print('num_int',int(num_float))


#str to list
first_name='lijo'
print(first_name)
list_of_first_name=list(first_name)
print(first_name)
print(type(first_name))








     








