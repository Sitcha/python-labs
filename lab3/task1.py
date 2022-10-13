def total(nums):
    total = 0 
    for num in nums:
        total += num
    return total

def tot10():
    nums=[]
    for i in range(10):
        num = int(input("enter a number:"))
        nums.append(num)

    total = sum(nums)
    return total


print(f"the sum of the 10 numbers is {tot10()}")




