'''
- In multple  inheritance, any specified attribute is first searched in the current class
- If not found, the search continues into the parent class in depth-first then left-right fashion without searching the same class twice
- The set of rules used to define this order is called Method Resolution Order (MRO)
- MRO must prevent the local precedence ordering and also provide monotonicity 
- MRO can be found using __mro__() or mro()

'''
class X : pass
class Y : pass
class Z : pass

class A(X,Y): pass
class B(Y,Z): pass

class N(A,B,Z): pass

for obj in N.mro():
    print(obj)