from sqlite3.dbapi2 import Cursor, connect
from tkinter import *  
from PIL import ImageTk
import PIL.Image
from tkinter import ttk, messagebox
import sqlite3
import os

class salesClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1055x485+205+127")
        self.root.title("Sales | IMS | Developed by Amit")
        self.root.config(bg="white")
        photo = PhotoImage(file = "images\i1.png")
        self.root.iconphoto(False, photo)
        self.root.focus_force()
        self.root.resizable(False, False)
        #root.overrideredirect(1)

        #----Variables----
        self.var_invoice = StringVar()
        self.bill_list=[]

        #title
        title = Label(self.root, text="View Customer Bill", font=("goudy old style", 20, "bold"), bg="purple4", fg="white", bd=1,relief=RIDGE).pack(side=TOP, fill=X, padx=10,pady=10)

        lbl_invoice = Label(self.root, text="Invoice no.", font=("times new roman", 15), bg="white").place(x=50,y=100)

        txt_invoice = Entry(self.root, textvariable=self.var_invoice, font=("times new roman", 15), bg="azure2").place(x=160,y=100, width=180, height=28)

        btn_search = Button(self.root, command=self.search, text="Search", font=("times new roman", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2").place(x=360,y=99, width=120, height=28)
        btn_clear = Button(self.root,text="Clear", command=self.clear, font=("times new roman", 15, "bold"), bg="lightgray", fg="black", cursor="hand2").place(x=490,y=99, width=120, height=28)


        #---Bill list---
        sales_frame = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        sales_frame.place(x=50,y=140,width=250, height=300)

        scrolly = Scrollbar(sales_frame, orient= VERTICAL)

        self.Sales_List = Listbox(sales_frame,font=("goudy old style", 15), bg="white", yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.Sales_List.yview)
        self.Sales_List.pack(fill=BOTH, expand=1)
        self.Sales_List.bind("<ButtonRelease-1>", self.get_data)

        #---Bill Area---

        bill_Frame = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        bill_Frame.place(x=330,y=140,width=410, height=300)
        
        title22 = Label(bill_Frame, text="Customer Bill Area", font=("goudy old style", 20), bg="spring green").pack(side=TOP, fill=X)

        scrolly2 = Scrollbar(bill_Frame, orient= VERTICAL)

        self.bill_area = Text(bill_Frame,font=("goudy old style", 15), bg="azure2", yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT, fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH, expand=1)

        #---Images---

        self.im1= PIL.Image.open("images/sal1.png")
        self.im1=self.im1.resize((250,200),PIL.Image.ANTIALIAS)
        self.im1=ImageTk.PhotoImage(self.im1)

        self.lbl_im1 = Label(self.root, image=self.im1, bg="white")
        self.lbl_im1.place(x=770, y=170)
        
        self.show()
    #############################################################33333

    def show(self):
        del self.bill_list[:]
        self.Sales_List.delete(0, END)

        for i in os.listdir("bill/"):
            if i.split('.') [-1] == 'txt':
                self.Sales_List.insert(END,i)
                self.bill_list.append(i.split('.')[0])

    def get_data(self, ev):
        index_ = self.Sales_List.curselection()
        file_name=self.Sales_List.get(index_)
        self.bill_area.delete('1.0', END)
        fp=open(f'bill/{file_name}', 'r')
        for i in fp:
            self.bill_area.insert(END, i)
        fp.close()

    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error", "Invoice no. should be required", parent=self.root)

        else:
            if self.var_invoice.get() in self.bill_list:
                fp=open(f'bill/{self.var_invoice.get()}.txt', 'r')
                self.bill_area.delete('1.0', END)
                for i in fp:
                    self.bill_area.insert(END, i)
                fp.close()
            else:
                messagebox.showerror("Error", "Invalid invoice No.", parent=self.root)


    def clear(self):
        self.show()
        self.bill_area.delete('1.0', END)




if __name__ =="__main__":
    root = Tk()
    obj = salesClass(root)
    root.mainloop()        