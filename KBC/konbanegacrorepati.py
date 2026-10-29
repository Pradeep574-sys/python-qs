def welcome(name):
    print(f"Welcome to KBC {name}")

def question_bank():
    price=0
    #question 1:-
    q1="\n1.largest river in the world?\na)neil river\tb)amazon river\tc)ganga river\td)yamuna river\n"
    ans1="amazon river"
    price=ask_questions(q1,ans1,price)
    if price==-1:
        return print("you failed\n")
    else:
        print(f"you have won {price}")
    #question 2:-    
    q2="\n2.largest economic city?\na)delhi\tb)kerela\tc)chennai\td)mumbai\n"
    ans2="mumbai"
    price=ask_questions(q2,ans2,price)
    if price==-1:
            return print("you failed\n")
    else:
            print(f"you have won {price}")
    #question 3:-        
    q3="\n3.Highest GDP state of India?\na)punjab\tb)karnataka\tc)maharashtra\td)gujrat\n"
    ans3="maharashtra"
    price=ask_questions(q3,ans3,price)
    if price==-1:
            return print("you failed\n")
    else:
            print(f"you have won {price}")
    #question 4:-        
    q4="\n4.Richest man in india?\na)Gautam adani\tb)Mukash ambani\tc)Sanjeev Goenka\td)Elon musk\n"
    ans4="Gautam adani"
    price=ask_questions(q4,ans4,price)
    if price==-1:
            return print("you failed\n")
    else:
            print(f"you have won {price}")
    #question 5:-        
    q5="\n5.Who invented 0?\na)arya bhat\tb)albert einstien\tc)newton\td)apj abdul kalam\n"
    ans5="arya bhat"
    price=ask_questions(q5,ans5,price)
    if price==-1:
            return print("you failed\n")
    else:
            print(f"you have won {price}")
    #question 6:-        
    q6="\n6.Who is founder of qspider?\na)Sachin sir\tb)Girish sir\tc)saarang sir\td)Tanuja mam\n"
    ans6="saarang sir"
    price=ask_questions(q6,ans6,price)
    if price==-1:
                return print("you failed\n")
    else:
                print(f"you have won {price}")
    #question 7:-
    q7="\n7.inflation rate in world?\na)6.23\tb)2.29\tc)5.54\td)7.01\n"
    ans7="5.54"
    price=ask_questions(q7,ans7,price)
    if price==-1:
                return print("you failed\n")
    else:
                print(f"you have won {price}")
                print("---Congratulation you won 7 crores---")
                print("Deviyo aur Sajano shukriya humara sath khelna ka liya aapki dhan rashi aajegi aapka account ma sath crore")
            

def ask_questions(ques,answer,current_price):

    print(f"{ques}")
    user_ans=input("Enter your answer\n")
    if user_ans == answer:
        current_price+=10000000
        return current_price
    else:
        return -1
#main program
print("\n---WELCOME TO KBC---\n")        
name =input("enter your name\n")
welcome(name)
choice=input("are you ready(y/n)\n")
if choice=="n":
    print("thank u for playing\n")
elif choice=="y":
    print("---Thank you for joining the game---\nLETS STARTS!!!")

    question_bank()    
