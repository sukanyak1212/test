name='Sukanya'
print(name.count('a'))
print(name.find('y'))
print(name.rfind('a'))
print(name.find('a'))
print(name)


name='    mariya  P V   '
print(name)
print(name.count(' '))   #10, count space also
print(name.strip())    #both side strip
print(name.lstrip())   #lef strip
print(list(name))
print('what is the index',name.find('i'))
print('what is the index',name.find('I'))




print('i love python'.capitalize())
print('i love python'.title())    






country='finland'
print(country.startswith('fin'))
print(country.startswith('f'))
print(country.startswith('fin'))
print(country.startswith('Fin'))
print(country.startswith('F'))

print(country.endswith('d'))
print(country.endswith('land'))
print(country.endswith('D'))


skills = ['html','css','java','javaScript','python']
print(', '.join(skills))
print('### '.join(skills))

print('abcd'.isalpha())
print('122abc132'.isalpha())
print('1123'.isalnum())
print('1123'.isnumeric())
print('1123'.isdigit())
print('1123'.isdecimal())

#identifiers will not statrts with symbols, and numbers
print('name'.isidentifier())

sentance='I love javaScript. javaScript is very important langauge in the world.'
print(sentance.replace('javaScript','Python'))

first_name='Riya'
second_name='john'
age='25'
skills=['java','java','Script','html','css','python']

formatedSkills=(', ').join(skills) 
print(formatedSkills)

full_name = first_name +' ' + second_name
print(full_name)
print(f'My name is {full_name} my age is {age} My skills are {formatedSkills}')
print('My name is {} my age is {} My skills are {}'.format(full_name,age,formatedSkills))


#using format
a=6
b=4
print('{}+{}={}'.format(a,b,a+b))
print('{}+{}={}'.format(a,b,a-b))
print('{}+{}={}'.format(a,b,a*b))
print('{}+{}={:.1f}'.format(a,b,a/b))
print('{}+{}={}'.format(a,b,a//b))
print('{}+{}={}'.format(a,b,a%b))
print('{}+{}={}'.format(a,b,a**b))

div=a/b
print(f'{a}+{b}={a+b}')
print(f'{a}+{b}={a-b}')
print(f'{a}+{b}={a*b}')
print(f'{a}+{b}={div:0.2f}')
print(f'{a}+{b}={a//b}')
print(f'{a}+{b}={a%b}')
print(f'{a}+{b}={a**b}')

sentance1='i love python'
print(sentance1.split('love'))

print('i \nlove \nindia')
print('java\javaScript\python\html\css')
print("i don't like")
print('i don\'t like')
print("the old cliche of \"an apple a day keep the doctor away\" might not work")
print('the old cliche of "an apple a day keep the doctor away" might not work')


#table
print('name','\t','age','\t','Qualification','\t','Designation','\t')
print('Riya','\t','30','\t','BCA','\t','T.E','\t')
print('Zain','\t','29','\t','MCA','\t','manager','\t')
print('john','\t','31','\t','BTech','\t','Dev ','\t')






'''
name='anu'
surname='george'
name_with_surname=name +' '+ surname
print(name_with_surname)
'''



