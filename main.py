from http import client
import wolframalpha # to answer queries involving math and weather etc.
import wikipedia # to answer proled queries
import re #to check for words
import PySimpleGUI as sg # for our graphical user interface

# save  app id for wolframalpha
app_id = "G4UAUE-K5JX8XPVYX"
client = wolframalpha.Client(app_id)
''' input box with PySimpleGUI  which can take text input from the user''' 

def inputBoxThatAcceptsTextAndNumbers():
    layout = [[sg.Text('Enter your query')],
              [sg.InputText()],
              [sg.Button('Ok'), sg.Button('Cancel')]]
    window = sg.Window('Input Box', layout)
    event, values = window.read()
    window.close()
    return values[0]  






# REG check for the words
re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search



res = client.query("who is the muhammad buhari?")

for pod in res.pods:
    for sub in pod.subpods:
        print(sub.plaintext)


        