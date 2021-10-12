from sqlite3.dbapi2 import Row
from tkinter import *
from PIL import ImageTk
import PIL.Image
import os
from tkinter import ttk, messagebox
import sqlite3
import time

class BillClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed by Amit")
        self.root.config(bg="white")
        photo = PhotoImage(file = "images\i1.png")
        self.root.iconphoto(False, photo)

        #---#
        self.cart_list=[]


        #------Title-------
        self.icon_title = PhotoImage(file="images\icon1.png")
        title = Label(self.root, text="Inventory Management System", image=self.icon_title, compound=LEFT, font = ("times new roman", 37, "bold"), bg="midnight blue", fg="azure", anchor="w", padx=30).place(x=0, y=0, width=1350, height=70)

        #-------Btn_logout----------
        btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"), bg="green yellow", cursor="hand2").place(x=1120,y=10,height=50, width=150)

        #---Clock---
        self.lbl_clock = Label(self.root, text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS", font = ("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #======Main Frame=======
        main_frame = Frame(self.root, bd=0, bg="honeydew2")
        main_frame.place(x=1, y=100, relwidth=1, relheight=1)


        #=================================================================================================================================================================================================================================================================================================================
        #=====Product Frame=====

        ProductFrame1 = Frame(self.root, bd=4, relief=RIDGE, bg="linen")
        ProductFrame1.place(x=6, y=106, width=410, height=545)

        pTitle=Label(ProductFrame1, text="All product", font=("goudy old style", 20, "bold"), bg="tan4", fg="white").pack(side=TOP, fill=X)
        
        #----Frame2----
        self.var_search=StringVar()

        ProductFrame2 = Frame(ProductFrame1, bd=2, relief=RIDGE, bg="alice blue")
        ProductFrame2.place(x=2, y=42, width=398, height=90)

        lbl_search = Label(ProductFrame2, text="Search Product | By name", font=("times new roman", 15, "bold"), bg="alice blue", fg="green").place(x=2,y=5)

        lbl_search1 = Label(ProductFrame2, text="Product Name", font=("times new roman", 15, "bold"), bg="alice blue").place(x=2,y=45)
        txt_search = Entry(ProductFrame2, textvariable=self.var_search, font=("times new roman", 15), bg="azure2").place(x=130,y=49, width=150,height=25)
        btn_search=Button(ProductFrame2, command=self.search, text="Search", cursor="hand2", font=("goudy old style",15),bg="navy", fg="white", bd=1).place(x=285, y=48, width=100, height=25)
        btn_show_all=Button(ProductFrame2, command=self.show, text="Show All", cursor="hand2", font=("goudy old style",15),bg="#083531", fg="white", bd=1).place(x=285, y=10, width=100, height=25)

        #----Frame3----

        ProductFrame3 = Frame(ProductFrame1, bd=2, relief=RIDGE)
        ProductFrame3.place(x=2,y=138,width=398, height=372)

        scrolly = Scrollbar(ProductFrame3, orient= VERTICAL)
        scrollx = Scrollbar(ProductFrame3, orient= HORIZONTAL)



        self.product_Table = ttk.Treeview(ProductFrame3, columns=("pid", "name", "price", "qty", "status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)

        self.product_Table.heading("pid", text="Product ID")
        self.product_Table.heading("name", text="Name")
        self.product_Table.heading("price", text="Price")
        self.product_Table.heading("qty", text="QTY")
        self.product_Table.heading("status", text="Status")
        self.product_Table["show"] = "headings"

        self.product_Table.column("pid", width=65)
        self.product_Table.column("name", width=150)
        self.product_Table.column("price", width=100)
        self.product_Table.column("qty", width=60)
        self.product_Table.column("status", width=70)
        self.product_Table.pack(expand=1, fill=BOTH)
        self.product_Table.bind("<ButtonRelease-1>", self.get_data)

        lbl_note=Label(ProductFrame1, text="Note: Enter 0 quantity to remove product from cart", bg="light cyan",font=("goudy old style", 12), fg="red").pack(side=BOTTOM, fill=X)


        #=================================================================================================================================================================================================================================================================================================================
        #====Customer Frame====
        self.var_cname = StringVar()
        self.var_contact = StringVar()

        CustomerFrame = Frame(self.root, bd=4, relief=RIDGE, bg="seashell2")
        CustomerFrame.place(x=420, y=106, width=530, height=75)

        cTitle=Label(CustomerFrame, text="Customer Details", font=("goudy old style", 15), bg="SeaGreen4").pack(side=TOP, fill=X)
        lbl_name = Label(CustomerFrame, text="Name", font=("times new roman", 15), bg="seashell2").place(x=5,y=35)
        txt_name = Entry(CustomerFrame, textvariable=self.var_cname, font=("times new roman", 13), bg="azure2").place(x=65,y=37, width=180)
        
        lbl_contact = Label(CustomerFrame, text="Contact No.", font=("times new roman", 15), bg="seashell2").place(x=255,y=35)
        txt_contact = Entry(CustomerFrame, textvariable=self.var_contact, font=("times new roman", 13), bg="azure2").place(x=360,y=37, width=160)
  
        #==================================================================================================================================================================================================================================================================================================================
        #===Calculator & Cart Frame===
        Cal_Cart_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="seashell2")
        Cal_Cart_Frame.place(x=420, y=185, width=530, height=360)

        #---Calculator---
        #+++Frame+++
        self.var_cal_input= StringVar()
        Cal_Frame = Frame(Cal_Cart_Frame, bd=8, relief=RIDGE, bg="wheat1")
        Cal_Frame.place(x=5, y=10, width=268, height=340)

        #++++++GUI++++++
        txt_cal_input = Entry(Cal_Frame, textvariable=self.var_cal_input, font=("arial", 15, "bold"), width=21, bd=10, relief=GROOVE, state="readonly", justify=RIGHT)
        txt_cal_input.grid(row=0, columnspan=4)

        btn_7 = Button(Cal_Frame, text="7", font=('arial', 15, 'bold'), command=lambda:self.get_input(7), bd=5, width=4, pady=12, cursor="hand2", bg="gray63").grid(row=1, column=0)
        btn_8 = Button(Cal_Frame, text="8", font=('arial', 15, 'bold'), command=lambda:self.get_input(8), bd=5, width=4, pady=12, cursor="hand2", bg="gray63").grid(row=1, column=1)
        btn_9 = Button(Cal_Frame, text="9", font=('arial', 15, 'bold'), command=lambda:self.get_input(9), bd=5, width=4, pady=12, cursor="hand2", bg="gray63").grid(row=1, column=2)
        btn_sum = Button(Cal_Frame, text="+", font=('arial', 15, 'bold'),  command=lambda:self.get_input('+'), bd=5, width=4, pady=12, cursor="hand2", bg="orange").grid(row=1, column=3)

        btn_4 = Button(Cal_Frame, text="4", font=('arial', 15, 'bold'), command=lambda:self.get_input(4),  bd=5, width=4, pady=12, cursor="hand2", bg="gray63").grid(row=2, column=0)
        btn_5 = Button(Cal_Frame, text="5", font=('arial', 15, 'bold'), command=lambda:self.get_input(5),  bd=5, width=4, pady=12, cursor="hand2", bg="gray63").grid(row=2, column=1)
        btn_6 = Button(Cal_Frame, text="6", font=('arial', 15, 'bold'), command=lambda:self.get_input(6), bd=5, width=4, pady=12, cursor="hand2", bg="gray63").grid(row=2, column=2)
        btn_sub = Button(Cal_Frame, text="-", font=('arial', 15, 'bold'), command=lambda:self.get_input('-'), bd=5, width=4, pady=12, cursor="hand2", bg="orange").grid(row=2, column=3)

        btn_1 = Button(Cal_Frame, text="1", font=('arial', 15, 'bold'), bd=5, command=lambda:self.get_input(3), width=4, pady=12, cursor="hand2", bg="gray63").grid(row=3, column=0)
        btn_2 = Button(Cal_Frame, text="2", font=('arial', 15, 'bold'), bd=5, command=lambda:self.get_input(2), width=4, pady=12, cursor="hand2", bg="gray63").grid(row=3, column=1)
        btn_3 = Button(Cal_Frame, text="3", font=('arial', 15, 'bold'), bd=5, command=lambda:self.get_input(1), width=4, pady=12, cursor="hand2", bg="gray63").grid(row=3, column=2)
        btn_mul = Button(Cal_Frame, text="x", font=('arial', 15, 'bold'), bd=5, command=lambda:self.get_input('*'), width=4, pady=12, cursor="hand2", bg="orange").grid(row=3, column=3)

        btn_0 = Button(Cal_Frame, text="0", font=('arial', 15, 'bold'), command=lambda:self.get_input(0), bd=5, width=4, pady=12, cursor="hand2", bg="gray63").grid(row=4, column=0)
        btn_c = Button(Cal_Frame, command=self.clear_cal, text="C", font=('arial', 15, 'bold'), bd=5, width=4, pady=12, cursor="hand2", bg="firebrick1").grid(row=4, column=1)
        btn_eq = Button(Cal_Frame, command=self.perform_cal, text="=", font=('arial', 15, 'bold'), bd=5, width=4, pady=12, cursor="hand2", bg="green").grid(row=4, column=2)
        btn_div = Button(Cal_Frame, text="÷", font=('arial', 15, 'bold'), command=lambda:self.get_input('/'), bd=5, width=4, pady=12, cursor="hand2", bg="orange").grid(row=4, column=3)





        #---Cart---

        cart_Frame = Frame(Cal_Cart_Frame, bd=2, relief=RIDGE)
        cart_Frame.place(x=278,y=9,width=245, height=341)
        
        self.cartTitle=Label(cart_Frame, text="Cart \t Total Product: [0]", font=("goudy old style", 15), bg="lavender")
        self.cartTitle.pack(side=TOP, fill=X)

        scrolly = Scrollbar(cart_Frame, orient= VERTICAL)
        scrollx = Scrollbar(cart_Frame, orient= HORIZONTAL)



        self.CartTable = ttk.Treeview(cart_Frame, columns=("pid", "name", "price", "qty"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)

        self.CartTable.heading("pid", text="Product ID")
        self.CartTable.heading("name", text="Name")
        self.CartTable.heading("price", text="Price")
        self.CartTable.heading("qty", text="QTY")
        self.CartTable["show"] = "headings"

        self.CartTable.column("pid", width=70)
        self.CartTable.column("name", width=100)
        self.CartTable.column("price", width=100)
        self.CartTable.column("qty", width=60)
        self.CartTable.pack(expand=1, fill=BOTH)
        self.CartTable.bind("<ButtonRelease-1>", self.get_data_cart)


        #====================================================================================================================================================================================================================================================================================================================
        #====Menu Frame=====
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()

        Add_cartwidgetsFrame = Frame(self.root, bd=2, relief=RIDGE, bg="light steel blue")
        Add_cartwidgetsFrame.place(x=420,y=550,width =530, height=100)
          
        lbl_p_name=Label(Add_cartwidgetsFrame, text="Product Name", font=("times new roman", 15), bg="light steel blue").place(x=5,y=2, height=22)
        txt_p_name=Entry(Add_cartwidgetsFrame, textvariable=self.var_pname, font=("times new roman", 15), bg="azure2", state='readonly').place(x=5,y=32, width=150, height=22)

        lbl_p_price=Label(Add_cartwidgetsFrame, text="Price per QTY", font=("times new roman", 15), bg="light steel blue").place(x=190,y=2, height=18)
        txt_p_price=Entry(Add_cartwidgetsFrame, textvariable=self.var_price, font=("times new roman", 15), bg="azure2", state='readonly').place(x=190,y=32, width=150, height=22)

        lbl_p_qty=Label(Add_cartwidgetsFrame, text="Quantity", font=("times new roman", 15), bg="light steel blue").place(x=375,y=1, height=20)
        txt_p_qty=Entry(Add_cartwidgetsFrame, textvariable=self.var_qty, font=("times new roman", 15), bg="azure2").place(x=375,y=32, width=120, height=22)

        self.lbl_inStock=Label(Add_cartwidgetsFrame, text="In stock [0]", font=("times new roman", 15), bg="light steel blue")
        self.lbl_inStock.place(x=5,y=65)

        btn_clear_cart = Button(Add_cartwidgetsFrame, command=self.clear_cart,text="Clear", font=("times new roman", 15, "bold"), bg="yellow", cursor="hand2").place(x=190, y=65,  width=100, height=25)
        btn_add_cart = Button(Add_cartwidgetsFrame, command=self.add_update_cart,text="Add | Update Cart", font=("times new roman", 15, "bold"), bg="RoyalBlue1", cursor="hand2").place(x=320, y=64,  width=200, height=25)


        #=====================================================================================================================================================================================================================================================================================================================
        #---Billing area---
        billFrame=Frame(self.root, bd=2,relief=RIDGE, bg="white")
        billFrame.place(x=955,y=105, width=320, height=410)

        bTitle=Label(billFrame, text="Customer Bill", font=("goudy old style", 18, "bold"), bg="red4", fg="white").pack(side=TOP, fill=X)

        scrolly = Scrollbar(billFrame, orient= VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)

        self.txt_bill_area=Text(billFrame, yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH, expand=1)
        scrolly.config(command=self.txt_bill_area.yview)


        #---------Billing Buttons----------
        billMenuFrame=Frame(self.root, bd=2,relief=RIDGE, bg="white")
        billMenuFrame.place(x=955,y=520, width=320, height=130)
        #labels

        self.lbl_amnt=Label(billMenuFrame, text="Bill Amount\n [0]", font=("goudy old style", 15, "bold"), bg="#3f51b5", fg="white")
        self.lbl_amnt.place(x=2, y=2, width=110, height=65)

        self.lbl_discount=Label(billMenuFrame, text="Discount\n [5%]", font=("goudy old style", 15, "bold"), bg="#8bc34a", fg="white")
        self.lbl_discount.place(x=114, y=2, width=87, height=65)

        self.lbl_net_pay=Label(billMenuFrame, text="Net Pay\n [0]", font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white")
        self.lbl_net_pay.place(x=203, y=2, width=112, height=65)

        #Buttons

        btn_print= Button(billMenuFrame, text="Print", font=("goudy old style", 15, "bold"), bg="lightgreen", fg="white", cursor="hand2")
        btn_print.place(x=2, y=72, width=72, height=50)

        btn_clear_all= Button(billMenuFrame, command=self.clear_all, text="Clear", font=("goudy old style", 15, "bold"), bg="gray", fg="white", cursor="hand2")
        btn_clear_all.place(x=76, y=72, width=72, height=50)

        btn_generate= Button(billMenuFrame, text="Generate/Save Bill", command=self.generate_bill, font=("goudy old style", 15, "bold"), bg="#009688", fg="white", cursor="hand2")
        btn_generate.place(x=150, y=72, width=165, height=50)

        self.show()
        


#============================================================================================================================================================================================================================================================================================================================
    #=========All Function========
    def get_input(self, num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)

    def clear_cal(self):
        self.var_cal_input.set('')

    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))

    ###---###
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select pid, name, price, qty, status from product where status='Active'")
            rows=cur.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in rows:
                self.product_Table.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)



    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_search.get()=="":   
                messagebox.showerror("Error", "Select input should be required", parent=self.root)

            else:
                cur.execute("Select pid, name, price, qty, status from product where name LIKE '%"+self.var_search.get()+"%' and status='Active'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.product_Table.delete(*self.product_Table.get_children())
                    for row in rows:
                        self.product_Table.insert('',END,values=row)

                else:
                    messagebox.showerror("Error", "No record found.", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


    def get_data(self, ev):
        f=self.product_Table.focus()
        content=(self.product_Table.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])        
        self.lbl_inStock.config(text=f"In stock [{str(row[3])}]")
        self.var_stock.set(row[3])
        self.var_qty.set('1')

    def get_data_cart(self, ev):
        f=self.CartTable.focus()
        content=(self.CartTable.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])  
        self.var_qty.set(row[3])              
        self.lbl_inStock.config(text=f"In stock [{str(row[4])}]")
        self.var_stock.set(row[4])



    def add_update_cart(self):
        if self.var_pid.get()=="":
            messagebox.showerror("Error", "Please select product from the list", parent=self.root)

        elif self.var_qty.get()=="":
            messagebox.showerror("Error", "Quantity is required", parent=self.root)
        elif int(self.var_qty.get())>int(self.var_stock.get()):
            messagebox.showerror("Error", "Invalid Quantity", parent=self.root)

        else:
            #price_cal= int(self.var_qty.get())*float(self.var_price.get())
            #price_cal=float(price_cal)
            price_cal=self.var_price.get()

            cart_data=[self.var_pid.get(), self.var_pname.get(), price_cal, self.var_qty.get(), self.var_stock.get()]

            #-------Update cart---------
            present="no"
            index_=0
            for row in self.cart_list:
                if self.var_pid.get()==row[0]:
                    present="yes"
                    break
                index_+=1

            if present=="yes":
                op=messagebox.askyesno("Confirm", "Product already present\nDo you want to update | Remove from the cart list", parent=self.root)
                if op==True:
                    if self.var_qty.get()=="0":
                        self.cart_list.pop(index_)
                    else:
                        #self.cart_list[index_][2]=price_cal
                        self.cart_list[index_][3]=self.var_qty.get()
            else:
                self.cart_list.append(cart_data)

            self.show_cart()
            self.bill_update()


    def bill_update(self):
        self.bill_amnt=0
        self.net_pay=0
        self.discount=0
        for row in self.cart_list:
            self.bill_amnt=self.bill_amnt+(float(row[2])*int(row[3]))

        self.discount=(self.bill_amnt*5)/100
        self.net_pay=self.bill_amnt-self.discount
        self.lbl_amnt.config(text=f"Bill Amount\n{str(self.bill_amnt)}")
        self.lbl_net_pay.config(text=f"Net Pay\n{str(self.net_pay)}")
        self.cartTitle.config(text=f"Cart \t Total Product: [{str(len(self.cart_list))}]")

    def show_cart(self): 
        try:
            self.CartTable.delete(*self.CartTable.get_children())
            for row in self.cart_list:
                self.CartTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


    def generate_bill(self):
        if self.var_cname.get()=='' or self.var_contact.get()=='':
            messagebox.showerror("Error", "Customer Details are required", parent=self.root)
        elif len(self.cart_list)==0:
            messagebox.showerror("Error", "Please add product to the cart", parent=self.root)

        else:
            #---Bill top---
            self.bill_top()
            #---Bill Middle---
            self.bill_middle()
            #---Bill Bottom---
            self.bill_bottom()

    def bill_top(self):
        invoice=int(time.strftime("%H%M%S")) + int(time.strftime("%d%m%Y"))
        bill_top_temp=f'''
\t\tIMS
 Phone no.: 09899098989 , Dhaka-1200
{str("="*36)}
 Customer Name: {self.var_cname.get()}
 Phone No.:{self.var_contact.get()}
 Bill No.:{str(invoice)}\t Date: {str(time.strftime("%d/%m/%Y"))}
{str("="*36)}
 Product Name\t\t  QTY\t Price
{str("="*36)}
        '''
        self.txt_bill_area.delete('1.0',END)
        self.txt_bill_area.insert('1.0',bill_top_temp)

    def bill_bottom(self):
        bill_bottom_temp=f'''
{str("="*36)}
 Bill Amount\t\t\t{self.bill_amnt}
 Discount\t\t\t{self.discount}
 Net Pay\t\t\t{self.net_pay}
{str("="*36)}\n
      Thanks for shopping in IMS
        '''
        self.txt_bill_area.insert(END,bill_bottom_temp)
        
    def bill_middle(self):
        for row in self.cart_list:
        # pid,name,price,qty,stock
            name=row[1]
            qty=row[3]
            price=float(row[2])*int(row[3])
            price=str(price)
            self.txt_bill_area.insert(END,"\n "+name+"\t\t  "+qty+"\t "+price)

    def clear_cart(self):
        self.var_pid.set('')
        self.var_pname.set('')
        self.var_price.set('')  
        self.var_qty.set('')              
        self.lbl_inStock.config(text=f"In stock [0]")
        self.var_stock.set('')

    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set('')
        self.var_contact.set('')
        self.txt_bill_area.delete('1.0', END)
        self.clear_cart()
        self.show()
        self.show_cart()



if __name__ =="__main__":
    #os.system('python start.py')
    print("Comment out ```#os.system('python start.py')``` in last section")
    root = Tk()
    obj = BillClass(root)
    root.mainloop()