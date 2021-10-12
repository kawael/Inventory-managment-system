import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image,ImageTk



root = Tk()
root.title("IMS")
root.geometry("500x300+400+200")
   
root.resizable(False, False)

bg_1 = PhotoImage(file="D:\Python\Python Projects\Pycharm projects\Inventory Management System\images\s1.png")

f1 = Label(root,bd=0,relief=GROOVE, font=("times new roman", 15, "bold"), image=bg_1)
f1.place(x=0,y=0,width=500,height=300)
#label1 = Label(f1, text="Welcome to IMS", font='times 25 bold', fg="orange", bg="DodgerBlue3", padx=10)
#label1.pack(padx=15, pady=10)

#label2 = Label(root, text="Developed by Amit", font=("times new roman", 12, "bold"), fg="orange", bg="DodgerBlue3", padx=12)
#label2.place(x=345, y=269)



root.after(4000,root.destroy) #after(ms,func)
root.overrideredirect(1)
root.mainloop()