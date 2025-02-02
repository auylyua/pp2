class handler:
    def get(self):
        self.inp = input("Enter a string: ") 
    def prn(self):
        print(self.inp.upper()) 
handler = handler()
handler.get()
handler.prn()
