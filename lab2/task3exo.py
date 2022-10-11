num1 = int(input("type a number:"))
num2 = int(input("type another number:"))
num3 = int(input('type a third number:'))

if num1 > num2 and num1 > num3 :
    print(f"{num1} is the greatest")
elif num2 > num2 and num2 > num3 :
    print(f"{num2} is the greatest")
else:
    print(f"{num3} is the greatest")
