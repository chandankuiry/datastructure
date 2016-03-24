from collections import deque
#here collections is class where deque(double ended queue) is defined if you want to know then type in search botton "file:///media/chandan/New%20Volume/C%20and%20C++/python/docs.python.org/2.7/library/collections.html#collections.deque"
d=deque(['g', 'h', 'i'])
print d
print "insert at last"
print d.append('j')                    # add a new entry to the right side
print d
print "insert at first"
d.appendleft('f')                 # add a new entry to the left side
print d                                # show the representation of the deque
print "delete last element"
print d.pop() 
print d                         # return and remove the rightmost item
print "first element"
print d.popleft() 
                     # return and remove the leftmost item

print list(d)                          # list the contents of the deque
print "first element"
print d[0]                             # peek at leftmost item
print "second element"
print  d[-1]                            # peek at rightmost item

print "reverse"
print list(reversed(d))                # list the contents of a deque in reverse
print "h is present in d or not"
print 'h' in d                         # search the deque
print "add jkl at last"
d.extend('jkl')
print d                  # add multiple elements at once
print "rotate right"
d.rotate(2)                      # right rotation
print d
print "left rotation"

d.rotate(-1)                     # left rotation
print d
print "reverse the deque"
deque(reversed(d))               # make a new deque in reverse order
print d
d.clear()                        # empty the deque>> d.pop()                          # cannot pop from an empty deque



d.extendleft('abc')              # extendleft() reverses the input order




