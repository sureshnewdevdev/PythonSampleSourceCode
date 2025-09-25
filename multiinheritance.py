class Base1:
    def foo(self):
        print("foo from Base1")

class Base2:
    def bar(self):
        print("bar from Base2")

class Derived(Base1, Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)

d = Derived()
d.foo()  # Output: foo from Base1
d.bar()  # Output: bar from Base2
print(Derived.__mro__)