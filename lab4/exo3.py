def change_max_min(array):
    min_index=0
    max_index=0

    for i in range(len(array)):
      if array[i] < array[min_index]:
          min_index = i
      if array[i] >array[max_index]:
          max_index = i
    

    array[min_index], array[max_index] = array[max_index], array[min_index]   
   
    return array


print(change_max_min([1,4,5,6,7,9]))
