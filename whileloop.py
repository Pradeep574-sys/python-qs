#print no 1 to 50

''' i=1
while i<=50:
    print(i)
    i+=1 '''

#print no in reverse from 100 to 1

''' i=100
while i>=1:
    print(i)
    i-=1 '''

#print even no between 2 and 100

''' i=2
while i<=100:
    print(i)
    i+=2 '''

#Calculate the sum of first N natural numbers
'''
n=int(input("Enter a no:"))
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print(f"sum of first {n} natural numbers is {sum}")  '''

# Print the multiplication table for a given no
'''
n=int(input("Enter a number:"))   
i=1
while i<=10:
    print(f"{n}*{i} ={n*i}")
    i+=1 '''

#Calculate the factorial of a no using a loop counter
'''
num=int(input("Enter a number:"))
fact=1
while num>0:
    fact*=num
    num-=1
print(fact)   '''

#Count how many digits are in given integer
'''
count=0
num=int(input("Enter a number: "))
while num>0:
    num=num//10
    count=count+1
print(count)    '''

#Print no's digit in reverse order
'''
rev=0
num=int(input("Enter a number: "))
while num>0:
    last_digit=num%10
    rev=rev*10+last_digit
    num=num//10
print(rev) '''

#To check if a given no is palindrome
'''
num=int(input("Enter a number: "))
rev=0
temp=num
while num>0:
    last_digit=num%10
    rev=rev*10+last_digit
    num=num//10
if rev==temp:
    print(f"{temp} is palindrome")
else:
    print(f"{temp} is not a palindrome") '''

#WAPP to launch a rocket
'''
count=10
while count>=1:
    print(count)
    count-=1
print("launch")    '''

#Add up all the individual digits of a number
'''
sum=0
num=int(input("Enter a number: "))
while num>0:
    last_digit=num%10
    sum=sum+last_digit
    num=num//10
print(sum)    '''

#Find the largest individual digit with a multi-digit number
'''
num=int(input("Enter a number: "))
max=0
while num>0:
    last_digit=num%10
    if last_digit>max:
        max=last_digit
    num=num//10
print(max) '''

# A small pet game

pet_name=input("Enter your pet's name: ")
hp=100
while True:
    choice=int(input("Enter your choice\n 1->Attack\n 2->Heal\n 3->Exit \n"))
    match choice:
        case 1:
            hp-=10
            print(f"{pet_name} is attacked and hp is reduced to {hp}")
            if hp<=0:
                print(f"{pet_name} is dead")
                break
        case 2:
            hp+=15
            if hp>=100:
                hp=100
                print(f"{pet_name} drank a healing potion and hp is {hp}")
        case 3:
            print(f"Thank you for playing with {pet_name}\n Game Over\n")
            break



    








