from http import client
import wolframalpha # to answer queries involving math and weather etc.
import wikipedia # to answer proled queries
import re #to check for words
import PySimpleGUI as sg # for our graphical user interface
import datetime # to get the datetime
import time 
# save  app id for wolframalpha
app_id = "G4UAUE-K5JX8XPVYX"
client = wolframalpha.Client(app_id)

''' input box with PySimpleGUI  which can take text input from the user''' 

# create a greeter function
def GreetUsersBasedOnTimeOfTheDay():
    hour = int(time.strftime("%H"))
    if hour >= 0 and hour < 12:
        print ("Good Morning")
    elif hour >= 12 and hour < 18:
        print ("Good Afternoon")
    else:
        print ("Good Evening")

GreetUsersBasedOnTimeOfTheDay()

# while True:  
#     pass




# this section is for words manipulation and extraction 
def inputBoxThatAcceptsTextAndNumbers():
    layout = [[sg.Text('Enter your query')],
              [sg.InputText()],
              [sg.Button('Ok'), sg.Button('Cancel')]]
    window = sg.Window('Input Box', layout)
    event, values = window.read()

    # REG check for the words
    # re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search
    
    window.close()
    return values[0]



# res = client.query("who is the muhammad buhari?")

# for pod in res.pods:
#     for sub in pod.subpods:
#         print(sub.plaintext)


        