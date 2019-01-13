# itertools!

from itertools import *

a = range(0,10)
b = ['a','b','c','d','e','f','g','h','i','j']

'''CHAIN'''
# for i in itertools.chain(a, b):
#     print i

# print list(itertools.chain(a[:1],b[:2]))


# for i in islice(count(), 0, 101, 5):
#     print i

# evens = [x for x in a if x%2 == 0]
# odds = [x for x in a if x%2 == 1]

# print evens, odds


'''MAP'''
def my_function(x):
    return x ** 2
# for item in a:
#     print my_function(item)
# for i in map(my_function, a):
#     print(i)
squared = [x for x in map(my_function, a)]
print squared


'''ZIP'''
list1 = ['x', 'y', 'z']
list2 = [1, 2]
list3 = [4]

for x,y,z in izip_longest(list1, list2, list3):
    print x,y,z

for x,y,z in zip(list1, list2, list3): # zips the lists into a list of tuples
    print x, y, z