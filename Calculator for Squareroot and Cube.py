class calculater:

    def __init__(self, num):
        self.number = num

    def square(self):
        print(f'The square of {self.number} is {self.number **2}')
    
    def squareroot(self):
        print(f'The square root of {self.number} is {self.number **0.5}')
    
    def cube(self):
        print(f'The cube of {self.number} is {self.number **3}')
    

a = calculater(int(input("Enter the number here:-")))
a.cube()
a.square()
a.squareroot()