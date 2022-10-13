lst = []

def total(nums):
    total = 0 
    for num in nums:
        total += num
    return total
    
for i in range(5):
    num = int(input("enter a number:"))
    lst.append(num)
print(f"the sum of the 10 numbers is {total(lst)}")