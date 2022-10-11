#program displacing unique numbers
nums = []

for i in range(3):
    num = int(input("enter a number: "))
    nums.append(num)

print(len(set(nums)))