print "here you see the difference of not usING key function"

class Custom(object):
    def __init__(self, name, number):
        self.name = name
        self.number = number
 
    def __repr__(self):
        return '{}: {} {}'.format(self.__class__.__name__,
                                  self.name,
                                  self.number)
 
    def __cmp__(self, other):
        if hasattr(other, 'number'):
            return self.number.__cmp__(other.number)
customlist = [
    Custom('object', 99),
    Custom('michael', 1),
    Custom('theodore the great', 59),
    Custom('life', 42)]
print sorted(customlist)
