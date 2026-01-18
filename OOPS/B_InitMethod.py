class computer:
    def __init__(self, CPU, Ram, SSD):              #method for initialization
        self.CPU = CPU                              #instance variable
        self.Ram = Ram                              #instance variable    
        self.SSD = SSD                              #instance variable
    def confger(self):                              #method
        print("Configuration is set : ", self.CPU, self.Ram, self.SSD)
com1 = computer("i5", "8GB", "512TB")               #object
com2 = computer("i7", "16GB", "1TB")                #object
com1.confger()                                      #method calling
com2.confger()                                      #method calling