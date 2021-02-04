'''
90-100 = A
80-89 = B
70-79 = C
60-69 = D
50-59 = E
40-below = F
'''
try:
    marks = int(input('Enter your marks here:-\n'))

    if(marks>=90 and marks<=100 or marks==100):
        print('your grade is:- A')

    elif(marks>=80 and marks<=89):
        print('your grade is:- B')

    elif(marks>=70 and marks<=79):
        print('your grade is:- C')

    elif(marks>=60 and marks<=69):
        print('your grade is:- D')

    elif(marks>=50 and marks<=59):
        print('your grade is:- E')

    elif(marks<40):
        print('your grade is:-F')

    else:
        print('Enter valid marks please ')
except Exception as e:
    print('Please enter valid marks')
