"""
This is program for chatbot.
This chatbot mainly focuses on the the list of festivals in particular month 
and finding square roots of number,
1.Firstly, It greet the User and asks the name of a user.
2.After it welcomes the user and asks how to help the user.
3.Next it offer choices and asks to pick one of the choices based upon user requirement.
4.If users picks option 1 about festivals... then it asks enter a Month
5.After it will give the list of festivals in that particular month.
6.If users pick the option 2 about square root of number then it asks User to enter a Number.
7.After it evaluate the number and give the square root of number. 
8.If users pick the otion 3 to end chat then it Thankful User. 
9.Finally Ends chat....when User choose to end chat.

"""


import random 
from datetime import datetime

def greet():
    responses=["Hi","Hello","Nice to meet you"]
    print(random.choice(responses))

def welcome(name):
        messages=[" welcome to festivals chatbot,How can you assit you?",
                    "It's glad to see you ,welocome to bot,how can yoy help you?"
        ]
        print(f"{get_time_greeting()}, {random.choice(messages)}")

def get_time_greeting():
    current_time=datetime.now()
    time_greeting="Good Morning"
    if(current_time.hour>12 and current_time.hour<17):
        time_greeting="Good Afternoon"
    elif(current_time.hour>=17 and current_time.hour<22):
        time_greeting="Good Evening"
    elif(current_time.hour>=22):
        time_greeting="It's too late"
    return(time_greeting)
         
def list_festivals(month):
        l=["January","Feburary","March","April","May","June","July","August","September","October","November","December"]
        if (month=="January"):
            print("1-1-2020 : New year\n14-1-2020 : Lohri\n15-1-2020 : Sankranthi\n23-1-2020 : Subhash Chandra bose jayanthi\np26-1-2020 : Republic Day")
        elif (month=="Feburary"):
            print("21-2-2020 : Mahashivaratri")
        elif (month=="March"):
            print("9-3-2020 : Holika Dhan\n10-3-2020 : Holi\n25-3-2020 : Ugadhi , Gudi padwa\n26-3-2020 : cheti chand")
        elif (month=="Aril"):
            print("2-4-2020 : Ram Navami\n3-4-2020 : chaitra Navaratri parana\n8-4-2020 : Hanuman Jayanthi\n14-4-2020 : Ambedkar Jayanthi\n26-4-2020 : Akshaya Tritya")
        elif (month=="May"):
            print("1-5-2020 : May day")
        elif (month=="June"):
            print("23-6-2020 : jaganath Ratha Yatra")
        elif (month=="july"):
            print("5-7-2020 : Guru purinama\n23-7-2020 : Hariyali Teej\n25-7-2020 : Nag panchami")
        elif (month=="August"):
            print("3-8-2020 : Raksha Bandhan\n12-8-2020 : janmastami\n15-8-2020 : Independence day\n22-8-2020 : Ganesh chaturthi , 31-8-2020 : Onam")
        elif(month=="september"):
            print("1-9-2020:Anant Chaturdashi")
        elif(month=="October"):
            print("2-10-2020 : Gandhi Jyanathi\n17-10-2020: Sharad Navarathri\n24-10-2020 : Durga Puja Ashtami\n25-2-2020 : Dussehra")
        elif(month=="November"):
            print("4-11-2020 : karva Chath\n14-11-2020 : Diwali,Childrens day\n15-11-2020 : Govardhan puja\n16-11-2020 : Bhai dooj")
        elif(month=="December"):
            print("25-12-2020 : Merry chirstmas")
        else:
            print("Invalid Month")
        return(list_festivals)
import math
def square_root():
        number=int(input("Enter a Number :"))
        print(math.sqrt(number))
def show_menu():
        print(".............")
        print("1.List of festivals.")
        print("2.square root of number.")
        print("3.End chat.")
        print("..............")
        try:
            return(int(input("Enter choice[1-3]:")))
        except:
            print("Enter only numbers between 1 to 3")
            return 0
def bot():
        greet()
        print("What is your name ?")
        name=input("Enter name:")
        welcome(name)
        print("pick any one of the choices.")
        choice=show_menu()
        while (choice!=3):
            if (choice==1):
                print("hey there!\nyou selected 1 option\nwant to know about the festivals in particular month.")
                month=input("Enter a month :")
                list_festivals(month)
            elif(choice==2):
                print("hey there!\nyou selected 2 option\nwant to know to square root of a number.")
                square_root()
            else:
                print("I am unable to Understand\nplease enter a correct option")
            choice=show_menu()
        print("Thank You for Visting..\nHope u meet you soon\nVISIT AGAIN....")
bot()
