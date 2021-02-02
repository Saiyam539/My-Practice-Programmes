class cars:
    com = 'cars'
   
    def __init__(self, name , price , company):
        self.name = name
        self.price = price
        self.company = company
    
    def getname():
        n = input('Enter your name here:-\n')
        print('Hello', n, '\n')
    
    def getdetails(self):
        print(f'The name of the car is {self.name}')
        print(f'The price of {self.name} in Indian rupee is {self.price}')
        print(f'The company of {self.name} is {self.company}')

print('WELCOME TO SAIYAM CAR SERVISE\n')

cars.getname()
print('To check details of a car please select a car given below')

list = ['Verna', 'Grand i10', 'Audi Q7','mercedes gle 400']
for x in range(len(list)):
    print(list[x])

c = input('Enter the name of a car given above here:-\n')
if c=='verna':
    c = cars('Verna','7 lakh' , 'Hyundai')
    c.getdetails()
elif c=='grand i10':
    c = cars('Grand i10', '6 lakh', 'Hyundai')
    c.getdetails()
elif c=='audi q7':
    c = cars('Audi Q7','90 lakh', 'Audi')
elif c=='mercedes gle 400':
    c = cars('Mecedes gle 400','1 crore', 'Mercedes')
    c.getdetails()
else:
    print('Please enter a valid cars!!')
