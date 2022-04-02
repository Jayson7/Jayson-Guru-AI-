from http import client
from tkinter import font
from turtle import color, width
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
        greeter_lable = Label(root, text=greet, font =("Ubuntu", 15,) , fg='black', anchor='center', pady =20, padx = 20, )
        root.configure(bg='white')
        
GreetUsersBasedOnTimeOfTheDay()
greeter_lable.grid(row=1, column=3, columnspan=3)

# dictacte screen size 
root.geometry("500x500")
root.minsize(500, 500)
root.maxsize(500, 500)
root.title('Jayson Guru AI')
# logo widget

my_img = ImageTk.PhotoImage(Image.open('./4.jpg').resize((200, 150), Image.ANTIALIAS))
my_label = Label(image=my_img)
""" make the image fit the label """             
my_label.grid(row=5, column=3, columnspan=3, pady=20)
      
# input widget
entry = Entry(root, width=30, borderwidth=4, font=('monospace', 17) )
entry.grid(row=6, column=3, columnspan=3, padx=10, pady=40, ipady=6)
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
    input_checker()
    
""" create clear placeholder function """
def clear_placeholder():
    entry.delete(0, END)
    entry.config(fg='black')

""" create a button to get the input from the user """
button_submit = Button(root, text="Ask", font=('monospace', 12), command=get_input, bg='lightgreen', fg='black', padx=7, pady=7)
""" place the button on the screen """
button_submit.grid(row=8, column=2, columnspan=3, ipady=7, ipadx=7)
""" create a button to clear the input """
button_clear = Button(root, text="Clear", font=('monospace', 12), command=clear_placeholder, bg='lightgreen', fg='black', padx=7, pady=7)
""" place the button on the screen """
button_clear.grid(row=8, column=4, columnspan=3, ipady=7, ipadx=7)
""" button_clear rounded corners """
button_clear.config(relief=RIDGE)
""" button_submit rounded corners """
button_submit.config(relief=RIDGE)

""" search for input_text in wolframalpha """
def input_checker():  
    res = client.query(input_text)
    try:
        answer = next(res.results).text
        print(answer) 
        """ show answer in a popup """
        popup_answer = Toplevel()
        popup_answer.geometry("500x500")
        popup_answer.minsize(500, 500)
        popup_answer.maxsize(500, 500)
        popup_answer.title('Jayson Guru AI')
        popup_answer.configure(bg='black')
        answer_label = Label(popup_answer, text=answer, font =("Ubuntu", 15,) , fg='white', bg='black', anchor='center', pady =20, padx = 20)
        answer_label.grid(row=1, column=3, columnspan=3)
    except:
        print("No results found")
        """ if answer doen't exist, show this in a popup """
        popup_answer = Toplevel()
        """ fix  popup to the size of answer"""
        popup_answer.geometry("200x70")
        popup_answer.maxsize(200, 70) 
        popup_answer.title('Jayson Guru AI')
        popup_answer.configure(bg='black')
        answer_label = Label(popup_answer, text="No results found", font =("Ubuntu", 15,) , fg='red', bg='black', anchor='center', pady =20, padx = 20)
        answer_label.grid(row=1, column=4, columnspan=4)
            
    
        



root.mainloop()        