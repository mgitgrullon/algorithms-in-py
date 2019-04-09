def bubble_sort(unsorted):
  is_sorted = 0

  while is_sorted == 0:
    for i in range(0, len(unsorted)-1):
      if unsorted[i+1] < unsorted[i]:
        # temp = unsorted[i]
        # unsorted[i] = unsorted[i+1]
        # unsorted[i+1] = temp
        unsorted[i], unsorted[i+1] = unsorted[i+1], unsorted[i]
        is_sorted = 1
  
  return unsorted