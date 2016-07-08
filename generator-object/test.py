# generator object execute only once , not more than once
def  test():
    for split_values in [[1,2,3,4],[5,6,7,8]]:
        for i in split_values:
            yield (i)


# a = []
# a.extend(test())
# print a

# b = test()
# print b
# print set(b)

# for i in b:
#  print i
#
#
# for i in b:
#  print i
# yeild by default use ()
# we can send list by yield[]
def test2():
     for i in [[(1,10)],[(1,10)],[(1,10)]]:
          yield (i)

# print set(test2())
a = []
a.extend(test2())
print a
