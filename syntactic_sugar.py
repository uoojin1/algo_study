'''
just some examples of cool syntacs
'''

list1 = [1,2,3,4]
list2 = range(1,5)
# print list1, list2

# mapList1 = [item*2 for item in list1]
# print mapList1

# filterList1 = [item for item in list1 if item%2 == 0]
# print filterList1

# filterAndMapList1 = [item*3 for item in list1 if item%2 == 1]
# print filterAndMapList1

'''
empty_array = []

if not empty_array   --> if array is not empty
if empty_array != [] --> if array is not empty
thus, same thing
'''

# array slicing
array1 = [0,1,2,3,4,5,6,7,8,9]
print array1[3::-1] # you start from index 3, gobackwards -1
print array1[1::-1] # 
print array1[::-1] # reverse array [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print 'what'
print array1[:5]
print array1[4::-1]