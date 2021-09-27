from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests
from PIL import Image,ImageTk





app = Tk()
app.title("weather app")
app.geometry("600x350")
app.iconbitmap('icon.ico')
app.config(bg='azure1')

def search():
    pass

city_text = StringVar()
city_entry = Entry(app, textvariable = city_text,bg='azure1')
city_entry.pack()

search_btn = Button(app, text="search button",font=('bold',10), width=13,command=search,bg='aquamarine4',fg="gray1")
search_btn.pack()

location_lbl = Label(app,text='',font=('calibri bold',20),bg='azure1')
location_lbl.pack()



temp_lbl = Label(app, text ="",font=('calibri bold',12),bg='azure1')
temp_lbl.pack()

weather_lbl = Label(app,text ="",font=('calibri bold',12),bg='azure1')
weather_lbl.pack()

app.mainloop()