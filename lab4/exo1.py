
#creaing a fnct


def even(lst):
    even = []
    for c in lst:
        if c % 2 == 0:
            even.append(c)
    return even

nums = [1,2,5,3,4]

print(even(nums))