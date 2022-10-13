n = int(input('type a natural number :'))

for i in range(1,n+1):
    for x in range(1,i+1):
     print(x,end='')
     
    for k in range(i-1,0,-1):
     print(k,end='')
print( )