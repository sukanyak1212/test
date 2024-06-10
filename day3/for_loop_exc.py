
'''
write program to get this out put
1  1  1  1
2  1  4  8
3  1  9  27
4  1  16  64
5  1  25  125
'''
for i in range(1,6):
     row = [i,1,i**2,i**3]
     print('  '.join(map(str,row)))