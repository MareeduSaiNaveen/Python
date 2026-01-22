class multple_inheritance:
    class A:                                  
        def f1(self):
            print("f1 work")
        def f2(self):
            print("f2 work")
        def show(self):
            print("In class A")
    class B:
        def f3(self):
            print("f3 work")
        def f4(self):
            print("f4 work")
        def show(self):
            print("In class B")
    class C(A, B):                                  #class C inheriting class A and B       
        def f5(self):
            print("f5 work")
        # def show(self):
        #     print("In class C")
c1 = multple_inheritance.C()                        #object of class C
c1.f1()                                             #calling method of class A
c1.f3()                                             #calling method of class B
c1.f5()                                             #calling method of class C
c1.show()                                           #calling overridden method
print("-"*5)
class multlevel_inheritance:
    class A:                                  
        def f1(self):
            print("f1 work")
        def f2(self):
            print("f2 work")
        def show(self):
            print("In class A")
    class B(A):                                     #class B inheriting class A
        def f3(self):
            print("f3 work")
        def f4(self):
            print("f4 work")
        def show(self):
            print("In class B")
    class C(B):                                     #class C inheriting class B 
        def f5(self):
            print("f5 work")
        # def show(self):
        #     print("In class C")
c1 = multlevel_inheritance.C()                        #object of class C
c1.f1()                                             #calling method of class A
c1.f3()                                             #calling method of class B
c1.f5()                                             #calling method of class C
c1.show()                                           #calling overridden method