__author__ = 'GatewayControl'
from itertools import cycle

myIterator = cycle(range(2))





num = 5
y = 1


#
# for x in range(0, num):
#     print "num#: " + str(x)
#     if myIterator == 0:
#         print "value of " + myIterator
#     else:
#         print "IT is equal to 1"
#     myIterator.next()
#     x+=1


print myIterator.next()
print myIterator.next()
print myIterator.next()
