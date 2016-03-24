squares = []
for x in range(10):
     squares.append(x**2)
print squares
squaresss = [x**2 for x in range(10)]#same as above  code
print squaresss
squaressss = map(lambda x: x**2, range(10))# same as above but its more concise and readable
print squaressss
z=[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print z
# its equivalent to
combs = []
for x in [1,2,3]:
     for y in [3,1,4]:
         if x != y:
             combs.append((x, y))
print combs
from math import pi
print [str(round(pi, i)) for i in range(1, 6)]
matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 14]]

print [[row[i] for row in matrix] for i in range(4)]
#is equivalent to
print zip(*matrix)

