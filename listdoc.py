list=["a","b","c","d","e","f"]
#insert method


list.append(5)# insert at last if we have to insert into agiven position then we have to use insert method "a.insert(len(a),x)" is equal to a.append
print list
a = [66.25, 333, 333, 1, 1234.5]
a = [66.25, 333, 333, 1, 1234.5]
print a.count(66.25),a.count(333)
a.append(999)
a.insert(1,2)#first argument is position and second argument is insert element
print a
a[len(a):]=list # qual to a.extend(list) 
print a

#delete an element 

#delete an element through the element value
a.remove(333)# here 1st 333 is deleted if 333 is not present in the list then it show error
print a
#delete an element through the index position 
a.pop(0)# if you delete an item in a given position then you use a.pop() method
print a

#know the position of an element
 
print a.index("a")# if you want to a element position then you have to use index method .this method return the position of an element if the number of element is more than one then it return the first position of an element :if element is not present in the list then it return error .


 #sorting
a.sort()
print a

customlist = [
    Custom('object', 99),
    Custom('michael', 1),
    Custom('theodore the great', 59),
    Custom('life', 42)
]
def getkey(
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

print sorted(customlist)
