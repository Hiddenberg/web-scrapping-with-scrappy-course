my_list = [1,2,3,4,5]

# for element in my_list:
#    print(element)

# Let's reproduce what python does when iterating a list

my_iter = iter(my_list)
print(type(my_iter))

# Extracting elements
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))