def my_func():
   a = 1
   yield a

   a = 2
   yield a

   a = 3
   yield a

def pairs_generator():
   pair_number = 0

   while pair_number <= 100:
      pair_number += 2
      yield pair_number



my_first_gen = my_func()

# print(next(my_first_gen))
# print(next(my_first_gen))
# print(next(my_first_gen))
pair = pairs_generator()


print(next(pair))
print(next(pair))
print(next(pair))
print(next(pair))
print(next(pair))
print(next(pair))
print(next(pair))
print(next(pair))
print(next(pair))
print(next(pair))
print(next(pair))
print(next(pair))
print(next(pair))