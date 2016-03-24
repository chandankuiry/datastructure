#!/usr/bin/python

class JustCounter:
   __secretCount = 0
  
   def count(self):
      self.__secretCount += 1
      print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()
#print counter.__secretCount
# here gives error because if we use "__" before a class variable that is hided 
#if you want to access tose variables then you have to repalce "print counter.__secretCount" as "object._className__attrName."like

print  counter._JustCounter__secretCount
#now it gives no error
