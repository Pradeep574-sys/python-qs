# age=int(input("enter age:"))
# if age>=18:
#     print("eligible to drive")

# else:
#     print("not eligible to vote")

'''Check whether a student has passed, and if passed, 
check whether marks are above 75 for distinction.'''
'''marks=int(input("Enter marks: "))
if marks>=35:
        print("pass")
        if marks>75:
            print("First Class")
        else:
            print("Not distinction")   
else:
    print("Not passed")        '''

'''Check ATM withdrawal:
First check whether PIN is correct.
If correct, 
check whether sufficient balance is available.'''

pin = 1234
balance = 50000

e_pin = int(input("Enter PIN: "))

if pin == e_pin:
    print("PIN is correct")

    bal = int(input("Enter amount to withdraw: "))

    if bal <= balance:
        print("Sufficient balance is available")
    else:
        print("Insufficient balance")

else:
    print("PIN is incorrect")