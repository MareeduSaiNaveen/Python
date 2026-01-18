class computer:
    brand = "Dell"                                  #class variable
    def __init__(self, CPU, Ram, SSD):              #method for initialization
        self.CPU = CPU                              #instance variable
        self.Ram = Ram                              #instance variable    
        self.SSD = SSD                              #instance variable
    def confger(self):                              #method
        print("Configuration is set : ", self.CPU, self.Ram, self.SSD)
    
    @classmethod
    def info(cls):                                  #class method
        return cls.brand
    
    @staticmethod
    def gb_into_bytes(gb):                          #static method   
        return gb * (1024 ** 3)
print("Brand :", computer.info())                   #calling class method without creating object
com1 = computer("i5", "8GB", "512TB")               #object
com2 = computer("i7", "16GB", "1TB")                #object
com1.confger()                                      #method calling
com2.confger()                                      #method calling

print("Gb into Bytes :", computer.gb_into_bytes(16))    #calling static method without creating object