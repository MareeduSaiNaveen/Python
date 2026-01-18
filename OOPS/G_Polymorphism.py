class Desktop:
    def build(self):                        #method of Desktop class
        print("Desktop is built")
class Laptop:                               
    def build(self):                        #method with same name as in Desktop class
        print("Laptop is built")
class Tablet:
    def open_pdf(self):
        print("PDF is Opend")
class Operation:
    def start(self, mechine):
        print("Operation is started")
        mechine.build()
        print("Operation is Completed")
        print("-"*5)
d1 = Desktop()
l1 = Laptop()
t1 = Tablet()
op1 = Operation()
op1.start(d1)
op1.start(l1)
# op1.start(t1)