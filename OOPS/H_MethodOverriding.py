class A:
    def show(self):
        print("In A show")
class B(A):
    # def show(self):
    #     print("In B show")
    pass
obj1 = B()
obj1.show()