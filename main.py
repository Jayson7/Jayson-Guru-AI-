from http import client
from tkinter import font
from turtle import color
from numpy import delete, size
import wolframalpha # to answer queries involving math and weather etc.
import wikipedia # to answer proled queries
import re #to check for words
from tkinter import * # for our graphical user interface
import datetime # to get the datetime
import time 
from PIL import ImageTk, Image

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
greeter_lable.grid(row=0, column=3, columnspan=3, sticky=W)

# dictacte screen size 
root.geometry("540x540")
root.minsize(540, 540)
root.maxsize(540, 540)
root.title('Jayson Guru AI')
# logo widget

my_img = ImageTk.PhotoImage(Image.open('./4.jpg').resize((200, 150), Image.ANTIALIAS))
my_label = Label(image=my_img)
""" make the image fit the label """             
my_label.grid(row=1, column=3, columnspan=3)
      
# input widget
entry = Entry(root, width=30, borderwidth=4, font=('monospace', 17) )
entry.grid(row=2, column=3, columnspan=3, padx=10, pady=60, ipady=6)
# entry placeholder text
entry.insert(0, "Ask me anything") 
def clear_placeholder(e):
    entry.delete(0, END)
    entry.config(fg='black') 
    
entry.bind("<FocusIn>",  clear_placeholder)

""" crate a function to get the input from the user """ 
def get_input():
    global input_text
    input_text = entry.get()
    print(input_text)

""" create clear placeholder function """
def clear_placeholder():
    entry.delete(0, END)
    entry.config(fg='black')

""" create a button to get the input from the user """
button_submit = Button(root, text="Ask", font=('monospace', 12), command=get_input, bg='lightgreen', fg='black', padx=10, pady=10)
""" place the button on the screen """
button_submit.grid(row=3, column=2, columnspan=3, ipady=10, ipadx=10)
""" create a button to clear the input """
button_clear = Button(root, text="Clear", font=('monospace', 12), command=clear_placeholder, bg='lightgreen', fg='black', padx=10, pady=10)
""" place the button on the screen """
button_clear.grid(row=3, column=4, columnspan=3, ipady=10, ipadx=10)

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