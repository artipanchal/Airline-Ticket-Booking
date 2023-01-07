from tkinter import *

root = Tk()
root.title("Airline Booking")
root.geometry("500x500")

global entry1
global entry2

Label(root, text="AIRGO", bg="blue", fg="white", width="30", height="2", font=("Calibri", 30)).place(x=450, y=10)
root.mainloop()
ws = Tk()
ws.title('PythonGuides')
ws.geometry('500x500')

from tkinter import *
from tkinter import ttk

root = Tk()
airline = PhotoImage(file=r'C:\Users\User\Desktop\PYTHON MINI PROJ\airline.png')
label = ttk.Label(root,image= airline)
PhotoImage(file=r'C:\Users\User\Desktop\PYTHON MINI PROJ\airline.png')
label.pack()


