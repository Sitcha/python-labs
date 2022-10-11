#this is a file about functions 


#this function adds two numbers together 
def add(num1,num2):
    total = num1 + num2
    return total 

#this function greets me
def greet_me():
    print("Hello, Audrey")
    return None

#this function greets anyone who types his name as an argument
def greet(name):
    print(f"Hello, {name}. Its good to have you here.")
    return None


#num1 = float(input("enter a real number: "))
#num2 = float(input("enter a real number: "))    
#print(add(num1,num2))


greet_me()

#your_name = input("Please enter your name: ")
#greet(your_name)

for i in range(1,10):
        print("*" * i)



for i in range(1,10):
    for x in range(1,i+1):
        print(x,end="")

    for k in range(i-1,0,-1):
        print(k,end="")
    print()
    
    