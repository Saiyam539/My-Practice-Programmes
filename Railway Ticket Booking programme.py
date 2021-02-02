class train:
    company = 'Railway'

    def __init__(self, name, fare, seats):
        self.name = name
        self.fare =  fare
        self.seats = seats
    def bookseats(self):
        s = int(input(f'Enter the number of seats you want to book:-\n'))
        
        
        if self.seats>s:
            print('Your ticket has been booked!!\n')
            self.seats = self.seats - s
        else:
            print('sorry, all the seats are booked\n')


    def getinfo(self):
        print(f'The name of the train is {self.name}')
        print(f'The fare of the {self.name} is {self.fare}')
        print(f'The seats left in the {self.name} is {self.seats}')
    @staticmethod
    def greet():
        print('\n***WELCOME TO THE INDIAN RAILWAY***\n')


train.greet()
hello = train("hello express", '1500 per person', 40)
hello.getinfo()

a = input('If you want to book a ticket press enter')

hello.bookseats()
hello.getinfo()




