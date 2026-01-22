class Student:
    def __init__(self, name, marks):                     #constructor
        self.name = name
        self.marks = marks

    def show(self):                                      #method       
        print(self.name, self.marks)

s1 = Student("Naveen", 90)
s1.show()