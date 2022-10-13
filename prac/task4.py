n = int(input("type a natural number :"))

for i in range(1, n + 1):
    spaces = " " * (n-i)
    for x in range(1, i + 1):
        spaces += str(x)
        
    for k in range(i-1,0,-1): 
        spaces += str(k)
        
    
    print(spaces)
