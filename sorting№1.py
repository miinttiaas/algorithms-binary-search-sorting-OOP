# list_of_groups = [5,2,21,1,3,4,5,6,7,8,9,10]
# for n in range(0,len(list_of_groups)):
#     for j in range(n+1,len(list_of_groups)):
#         if list_of_groups[n]>=list_of_groups[j]:
#             list_of_groups[n],list_of_groups[j] = list_of_groups[j],list_of_groups[n]
# print(list_of_groups)
# print(list_of_groups == sorted(list_of_groups))

def sorting_by_length(array):
    for n in range(len(array)):
        for i in range(n+1, len(array)):
            if array[n] <= array[i]:
                array[i], array[n] = array[n], array[i]
        print(array)
    return array == sorted(array,reverse=True)
print(sorting_by_length([5,2,2,21,1,3,4,5,6,7,8,9,10]))
