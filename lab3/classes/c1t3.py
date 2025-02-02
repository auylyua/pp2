class rectang:
    def __init__(self, length, width):
        self.length = length 
        self.width = width   
    def area(self):
        return self.length * self.width  
    def perimeter(self):
        return 2 * (self.length + self.width) 
length = float(input())
width = float(input())
rect = rectang(length, width)
print("S", rect.area())
print("P:", rect.perimeter())
