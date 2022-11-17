def find_even(list_1):
     even_list = []
     return even_list

list_1 = input().split()

p = list_1[0:(len(list_1)+1):2]

even_list = p
print(p)




a = input().split()
for i in range(0, len(a), 2):
    print(a[i])




list = [int(s) for s in input(). split()]
for index in range(len(list)):
    if index % 2 == 0:
        print(list[index]) 