num1 = input("type a number>")
num1 = int(num1)
num2 = int(input("type another number>"))

if num1 < num2 :
    print(f"{num1} is the smallest")
elif num2 < num1 :
    print(f"{num2} is the smallest")
else:
    print(f"{num1} = {num2}")

