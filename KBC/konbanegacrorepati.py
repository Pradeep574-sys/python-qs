def welcome(name):
    print(f"Welcome to KBC {name}")

def question_bank():
    q1="largest river in the world"
    ans1="neil river"
    q2="largest economic city"
    ans2="mumbai"
    q3="hieghest GDP"
    ans3="maharashtra"
    q4="richest man in india"
    ans4="mota bhai"
    q5="who invented 0"
    ans5="arya bhatt"
    q6="who is founder of qspider"
    ans6="saarang sir"
    q7="inflation rate in world"
    ans7="5.54"


name =input("enter your name\n")
welcome(name)
choice=input("are you ready(y/n)\n")
if choice=="n":
    print("thank u for playing\n")
elif choice=="y":
    print("thank you for joining the game\nLETS STARTS!!!")
