class A:             
    def __init__(self):                             #constructor of class A
        print("In A init")
    def f1(self):
        print("f1 work")
class B(A):                                         #class B inheriting class A           
    # def __init__(self):
    #     print("In B init")
    def f2(self):
        print("f2 work")
c1 = B()
c1.f1()                                            #calling method of class A
print("-"*5)
class A:                                  
    def __init__(self):
        print("In A init")
    def f1(self):
        print("f1 work")
class B(A):                                         #class B inheriting class A                               
    def __init__(self):
        super().__init__()                          #calling constructor of superclass A
        print("In B init")
    def f2(self):
        print("f2 work")
c1 = B()
c1.f1()