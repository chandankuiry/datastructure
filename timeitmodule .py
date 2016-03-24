>>> def test1():
...     if True:
...         return 1
...     else:
...         return 0

>>> print timeit("test1()", setup = "from __main__ import test1")
0.193144083023


>>> def test2():
...     if 1:
...         return 1
...     else:
...         return 0

>>> print timeit("test2()", setup = "from __main__ import test2")
0.162086009979


>>> def test3():
...     if True:
...             return True
...     else:
...             return False

>>> print timeit("test3()", setup = "from __main__ import test3")
0.214574098587

>>> def test4():
...     if 1:
...             return True
...     else:
...             return False

>>> print timeit("test4()", setup = "from __main__ import test4")
0.160849094391
