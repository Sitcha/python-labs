#program to calculate the average of ten numbers entered from the keyboard

#Algorithm 
#1. get the numbers from the keyboard 
#2. add all the ten numbers
#3  divide the sum of the numbers by 10


#program using for statement with a list 
print("-----first variation-----")
nums = []
for i in range(2):
    num = int(input("enter a number: "))
    nums.append(num)

total = sum(nums)
av = total/2

print(f"the average of the 2 numbers is {av}")

print("-----second variation-----")

#program using a for statement but without a list 
total = 0
for i in range(4):
     num = int(input("enter a number: "))
     total = total + num
print(f"the average of the 4  numbers is {total/4}")

print("-----third variation-----")

#program using a while statement 
i = 1
tot = 0
while i <= 4:
    num = int(input("enter a number: "))
    tot += num
    i += 1

print(f"the average of the 4  numbers is {tot/4}")

count = 0
for name in ["audrey","macmillan","tatenda","macmillan"]:
    if name == 'macmillan':
        count += 1
        print("name found")
    else:
        print("name not found")
print(f"name has been found {count} times!")


