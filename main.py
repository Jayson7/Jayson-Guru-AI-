from http import client
from tkinter import font
from turtle import color
from numpy import size
import wolframalpha # to answer queries involving math and weather etc.
import wikipedia # to answer proled queries
import re #to check for words
from tkinter import * # for our graphical user interface
import datetime # to get the datetime
import time 
# save  app id for wolframalpha
app_id = "G4UAUE-K5JX8XPVYX"
client = wolframalpha.Client(app_id)

# initialize Tk
root = Tk()

# create a greeter function
def GreetUsersBasedOnTimeOfTheDay():
    global greet
    global greeter_lable
    
    hour = int(time.strftime("%H"))
    if hour >= 0 and hour < 12:
        greet =  "Good Morning I'm Jayson AI, How can I help you ?"
        greeter_lable = Label(root, text=greet, font =("Ubuntu", 15,) , fg='lightgreen', anchor='center', pady =20, padx = 20)
        root.configure(bg='black')
    elif hour >= 12 and hour < 18:
        greet = "Good Afternoon I'm Jayson AI, How can I help you ?"
        greeter_lable = Label(root, text=greet, font =("Ubuntu", 15,) , fg='yellow', bg='black', anchor='center', pady =20, padx = 20)
        root.configure(bg='black')
    else:
        greet =  "Good Evening I'm Jayson AI, How can I help you ?"
        greeter_lable = Label(root, text=greet, font =("Ubuntu", 15,) , fg='dark', anchor='center', pady =20, padx = 20, )
        root.configure(bg='white')
        
GreetUsersBasedOnTimeOfTheDay()
greeter_lable.grid(row=0, column=0, columnspan=3)

# dictacte screen size 
root.geometry("600x600")
root.minsize(550, 550)
root.maxsize(550, 550)
root.title('Jayson Guru AI')

entry = Entry(root, width=50, borderwidth=5 )
entry.grid(row=2, column=0, columnspan=3, padx=20, pady=100, ippady=10)

# while True:  
    #pass
''' input box with PySimpleGUI  which can take text input from the user''' 


    



    # this section is for words manipulation and extraction 
        # REG check for the words
        # re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search




    # res = client.query("who is the muhammad buhari?")

    # for pod in res.pods:
    #     for sub in pod.subpods:
    #         print(sub.plaintext)



root.mainloop()        