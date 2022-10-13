nums = []

for i in range(3) :
    num = int(input("enter a number: "))
    nums.append(num)

big =max(nums)
print(f"the maximum of the 3 numbers is {big}")

#exo3 lab3
n = 7
for i in range( 1, n + 1 ):
    for j in range( 1, i + 1 ):
        print( j, end = "" )
    print()

    #exo4 lab3
n = int(input("type a natural number :"))

for i in range(1, n + 1):
    spaces = " " * (n-i)
    for x in range(1, i + 1):
        spaces += str(x)
        
    for k in range(i-1,0,-1): 
        spaces += str(k)
        
    
    print(spaces)
