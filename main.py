from http import client
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
    hour = int(time.strftime("%H"))
    if hour >= 0 and hour < 12:
        greet =  "Good Morning I'm Jayson AI, How can I help you"
    elif hour >= 12 and hour < 18:
        greet = "Good Afternoon I'm Jayson AI, How can I help you"
    else:
        greet =  "Good Evening I'm Jayson AI, How can I help you"

GreetUsersBasedOnTimeOfTheDay()
greeter_lable = Label(root, text=greet).grid(row=0, column=0)

# dictacte screen size 
root.geometry("500x500")
root.minsize(400, 400)
root.maxsize(700, 700)
root.title('Jayson Guru AI')


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