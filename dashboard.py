from tkinter import *
from PIL import ImageTk
import PIL.Image
from tkinter.tix import *
import os
import webbrowser
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
from tkinter import messagebox

class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("IMS | Developed by Amit")
        self.root.config(bg="white")
        photo = PhotoImage(file = "images\i1.png")
        self.root.iconphoto(False, photo)


        #------Title-------
        self.icon_title = PhotoImage(file="images\icon1.png")
        title = Label(self.root, text="Inventory Management System", image=self.icon_title, compound=LEFT, font = ("times new roman", 37, "bold"), bg="midnight blue", fg="azure", anchor="w", padx=30).place(x=0, y=0, width=1350, height=70)

        #-------Btn_logout----------
        btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"), bg="green yellow", cursor="hand2").place(x=1120,y=10,height=50, width=150)

        #---Clock---
        self.lbl_clock = Label(self.root, text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS", font = ("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #=========Left Menu==========
        self.MenuLogo = PIL.Image.open("images/l1.png")
        self.MenuLogo=self.MenuLogo.resize((200,200), PIL.Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu=Frame(self.root, bd=2, relief=RIDGE, bg="azure")
        LeftMenu.place(x=0,y=102, width=200, height=550)

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        lbl_menu = Label(LeftMenu, text="Menu", font=("times new roman", 20), bg="#009688").pack(side=TOP,fill=X)

        self.icon_side = PhotoImage(file="images\side1.png")

        btn_employee = Button(LeftMenu,command=self.employee, image=self.icon_side, compound=LEFT, text="Employee", font=("times new roman", 18, "bold"), bg="white", cursor="hand2", bd=2, padx=5, anchor="w", height=40).pack(side=TOP,fill=X)
        btn_supplier = Button(LeftMenu, command=self.supplier,image=self.icon_side, compound=LEFT, text="Supplier", font=("times new roman", 18, "bold"), bg="white", bd=2, cursor="hand2", padx=5, anchor="w", height=40).pack(side=TOP,fill=X)
        btn_category = Button(LeftMenu, command=self.category, image=self.icon_side, compound=LEFT, text="Category", font=("times new roman", 18, "bold"), bg="white", bd=2, cursor="hand2", padx=5, anchor="w", height=40).pack(side=TOP,fill=X)
        btn_products = Button(LeftMenu, command=self.product, image=self.icon_side, compound=LEFT, text="Products", font=("times new roman", 18, "bold"), bg="white", bd=2, cursor="hand2", padx=5, anchor="w", height=40).pack(side=TOP,fill=X)
        btn_sales = Button(LeftMenu, command=self.sales, image=self.icon_side, compound=LEFT, text="Sales", font=("times new roman", 18, "bold"), bg="white", bd=2, cursor="hand2", padx=5, anchor="w", height=40).pack(side=TOP,fill=X)
        btn_exit = Button(LeftMenu, command=self.exit,image=self.icon_side, compound=LEFT, text="Exit", font=("times new roman", 18, "bold"), bg="white", bd=2, cursor="hand2", padx=5, anchor="w", height=40).pack(side=TOP,fill=X)

        #===content====
        self.lbl_employee = Label(self.root,bd=5, relief=RIDGE, text="Total Employee\n[0]", bg="#33bbf9", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_employee.place(x=250, y=120, height=150, width=300)

        self.lbl_supplier = Label(self.root,bd=5, relief=RIDGE, text="Total Supplier\n[0]", bg="#ff5722", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_supplier.place(x=600, y=120, height=150, width=300)

        self.lbl_category = Label(self.root,bd=5, relief=RIDGE, text="Total Category\n[0]", bg="#009688", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_category.place(x=950, y=120, height=150, width=300)

        self.lbl_product = Label(self.root,bd=5, relief=RIDGE, text="Total Product\n[0]", bg="#607d8b", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_product.place(x=250, y=300, height=150, width=300)

        self.lbl_sales = Label(self.root,bd=5, relief=RIDGE, text="Total Sales\n[0]", bg="#ffc107", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_sales.place(x=600, y=300, height=150, width=300)                        


        #---footer---
        lbl_footer = Label(self.root, text="IMS-Inventory Management System | Developed by Amit", font = ("times new roman", 12), bg="#4d636d", fg="white")
        lbl_footer.pack(side=BOTTOM,fill=X)

        tip= Balloon(self.root, bg ="white")
        self.footer_image = PhotoImage(file="images\\footer1.png")
        self.btn_footer = Button(self.root, command=self.test1, image=self.footer_image, compound=RIGHT, cursor="hand2")
        self.btn_footer.place(x=1255, y=632)
        tip.bind_widget(self.btn_footer,balloonmsg="About")


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4

    def test1(self):
        webbrowser.open("https://amitkumardatta2005.wixsite.com/website-1/about-1")

    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employeeClass(self.new_win)

    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = supplierClass(self.new_win)

    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = categoryClass(self.new_win)
    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = productClass(self.new_win)

    def sales(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = salesClass(self.new_win)

    def exit(self):
        exit=messagebox.askyesno("Exit", "Do you really want exit?", parent=self.root)
        if exit==True:
            self.root.destroy()

if __name__ =="__main__":
    os.system('python start.py')
    root = Tk()
    obj = IMS(root)
    root.mainloop()