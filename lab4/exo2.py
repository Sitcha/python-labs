def bigger(lst): 
     a = []
     for i in range(len(lst) - 1):
          if  lst[i + 1] > lst[i]:
                a.append(lst[i+1])
     return a


print(bigger([1,9,3,4,5,6,7,8,9,4,3,5]))     