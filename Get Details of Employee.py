class employee:
    company = 'Apple'

    def __init__(self, name, age,product,how):
        self.name = name
        self.age = age
        self.product = product
        self.how = how
    
    def getinfo(self):
        print(f'The name of the employee is {self.name}')
        print(f'The age of the employe is {self.age} years')
        print(f'The product with the emloyee work in is {self.product}')
        print(f'The performence of the employee is {self.how}')
       

saiyam = employee('Saiyam', 15, 'Mac os developer', 'very good')
siya = employee('Siya', 12, 'ios developer', 'brilliant')
samriti = employee('Samriti',37, 'Apple pencil', 'superb')
arun = employee('Arun', 39,'imac', 'very nice')
doda = employee('Doda',2, 'iphone manufacturer', 'very bad')

n = input('Enter the name of the employee here:-\n')
if n=='saiyam':
    saiyam.getinfo()
elif n=='siya':
    siya.getinfo()
elif n=='samriti':
    samriti.getinfo()
elif n=='arun':
    arun.getinfo()
elif n=='doda':
    doda.getinfo()
else:
    print(f'There is no employee name, {n}')

