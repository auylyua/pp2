class sh:
    def __init__(self):
        self.area_value = 0 

    def area(self):
        print(self.area_value)  

class sqr(sh):
    def __init__(self, leng):
        super().__init__() 
        self.length = leng 
        self.area_value = leng * leng 
shape = sh()
print("shape's area:", shape.area())