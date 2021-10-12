from sqlite3.dbapi2 import Cursor, connect
from tkinter import *  
from PIL import ImageTk
import PIL.Image
from tkinter import ttk, messagebox
import sqlite3

class employeeClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1055x485+205+127")
        self.root.title("Employee | IMS | Developed by Amit")
        self.root.config(bg="white")
        photo = PhotoImage(file = "images\i1.png")
        self.root.iconphoto(False, photo)
        self.root.focus_force()
        self.root.resizable(False, False)
        #root.overrideredirect(1)

        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        #All variables

        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_emp_id = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()
        self.var_salary = StringVar()



        #-----Search-----
        SearchFrame=LabelFrame(self.root, text="Search Employee", bg="white", font=("goudy old style",12,"bold"))
        SearchFrame.place(x=250, y=20,width=600,height=70)

        #====Options====
        cms_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select", "Email", "Name", "Contact"), state='readonly', justify=CENTER, font=("goudy old style", 15))
        cms_search.place(x=10, y=10, width=180)
        cms_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("goudy old style", 15), bg="azure2")
        txt_search.place(x=200,y=10)

        btn_search = Button(SearchFrame, command=self.search, cursor="hand2", text="Search", font=("goudy old style", 15), bg="dark sea green", fg="white")
        btn_search.place(x=410,y=9,width=150, height=27)

        #---Title---
        title = Label(self.root, text="Employee Details", font=("goudy old style", 15), bg="#0f4d7d", fg="white").place(x=50,y=100,width=955)

        #---Contant----
        #---Row2---

        lbl_empid = Label(self.root, text="Employee ID", font=("goudy old style", 15), bg="white").place(x=50,y=150)
        lbl_gender = Label(self.root, text="Gender", font=("goudy old style", 15), bg="white").place(x=400,y=150)
        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 15), bg="white").place(x=750,y=150)
 
        txt_empid = Entry(self.root, textvariable=self.var_emp_id, font=("goudy old style", 15), bg ="azure2").place(x=180,y=150, width=180)
        txt_gender = ttk.Combobox(self.root, textvariable=self.var_gender, font=("goudy old style", 15), values=("Select", "Male", "Female", "Other"), state="readonly", justify=CENTER)
        txt_gender.place(x=480,y=150, width=180)
        txt_gender.current(0)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15), bg="azure2").place(x=850,y=150, width=180)

        #---Row2---

        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15), bg="white").place(x=50,y=190)
        lbl_dob = Label(self.root, text="Date of birth", font=("goudy old style", 15), bg="white").place(x=380,y=190)
        lbl_doj = Label(self.root, text="Date of joining", font=("goudy old style", 15), bg="white").place(x=720,y=190)
 
        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15), bg ="azure2").place(x=180,y=190, width=180)
        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 15), bg ="azure2").place(x=500,y=190, width=180)
        txt_doj = Entry(self.root, textvariable=self.var_doj, font=("goudy old style", 15), bg="azure2").place(x=850,y=190, width=180)

        #====Row3====

        lbl_email = Label(self.root, text="E-mail", font=("goudy old style", 15), bg="white").place(x=50,y=230)
        lbl_pass = Label(self.root, text="Password", font=("goudy old style", 15), bg="white").place(x=400,y=230)
        lbl_utype = Label(self.root, text="User type", font=("goudy old style", 15), bg="white").place(x=750,y=230)
 
        txt_email = Entry(self.root, textvariable=self.var_email, font=("goudy old style", 15), bg ="azure2").place(x=180,y=230, width=180)
        txt_pass = Entry(self.root, textvariable=self.var_pass, font=("goudy old style", 15), bg ="azure2").place(x=500,y=230, width=180)
        txt_utype = ttk.Combobox(self.root, textvariable=self.var_utype, state="readonly", font=("goudy old style", 15), values=("Select", "Admin", "Employee"))
        txt_utype.place(x=850,y=230, width=180)
        txt_utype.current(0)

        #===Row4===

        lbl_address = Label(self.root, text="Address", font=("goudy old style", 15), bg="white").place(x=50,y=270)
        lbl_salary = Label(self.root, text="Salary", font=("goudy old style", 15), bg="white").place(x=500,y=270)
 
        self.txt_address = Text(self.root, font=("goudy old style", 15), bg ="azure2")
        self.txt_address.place(x=180,y=270, width=300, height=60)
        txt_salary = Entry(self.root, textvariable=self.var_salary, font=("goudy old style", 15), bg ="azure2").place(x=600,y=270, width=180)

        #----Button---
        btn_add = Button(self.root, command=self.add, cursor="hand2", text="Save", font=("goudy old style", 15), bg="SeaGreen2", fg="white").place(x=490,y=305,width=100, height=28)

        btn_update = Button(self.root, command=self.update, cursor="hand2", text="Update", font=("goudy old style", 15), bg="cadet blue", fg="white").place(x=600,y=305,width=100, height=28)

        btn_delete = Button(self.root, command=self.delete, cursor="hand2", text="Delete", font=("goudy old style", 15), bg="goldenrod", fg="white").place(x=710,y=305,width=100, height=28)

        btn_clear = Button(self.root, command=self.clear,cursor="hand2", text="Clear", font=("goudy old style", 15), bg="SlateGray2", fg="white").place(x=820,y=305,width=100, height=28)

        btn_exit = Button(self.root, cursor="hand2", text="Exit", font=("goudy old style", 15), command=self.exit, bg="red", fg="white").place(x=930,y=305,width=100, height=28)


        #===Employee details===

        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0,y=345,relwidth=1, height=140)

        scrolly = Scrollbar(emp_frame, orient= VERTICAL)
        scrollx = Scrollbar(emp_frame, orient= HORIZONTAL)



        self.EmployeeTable = ttk.Treeview(emp_frame, columns=("eid", "name", "email", "gender", "contact", "dob", "doj", "pass", "utype", "address", "salary"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)

        self.EmployeeTable.heading("eid", text="Employee ID")
        self.EmployeeTable.heading("name", text="Name")
        self.EmployeeTable.heading("email", text="Email")
        self.EmployeeTable.heading("gender", text="Gender")
        self.EmployeeTable.heading("contact", text="Contact")
        self.EmployeeTable.heading("dob", text="Date of birth")
        self.EmployeeTable.heading("doj", text="Date of joining")
        self.EmployeeTable.heading("pass", text="Password")
        self.EmployeeTable.heading("utype", text="User type")
        self.EmployeeTable.heading("address", text="Address")
        self.EmployeeTable.heading("salary", text="Salary")

        self.EmployeeTable["show"] = "headings"

        self.EmployeeTable.column("eid", width=90)
        self.EmployeeTable.column("name", width=100)
        self.EmployeeTable.column("email", width=100)
        self.EmployeeTable.column("gender", width=100)
        self.EmployeeTable.column("contact", width=100)
        self.EmployeeTable.column("dob", width=100)
        self.EmployeeTable.column("doj", width=100)
        self.EmployeeTable.column("pass", width=100)
        self.EmployeeTable.column("utype", width=100)
        self.EmployeeTable.column("address", width=100)
        self.EmployeeTable.column("salary", width=100)
        self.EmployeeTable.pack(expand=1, fill=BOTH)
        self.EmployeeTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()


##########################################################################################################################################
##########################################################################################################################################

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error", "Employee ID must be required", parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Employee ID already assigned, try different", parent=self.root)
                else:
                    cur.execute("Insert into employee(eid, name, email, gender, contact, dob, doj, pass, utype, address, salary) values(?,?,?,?,?,?,?,?,?,?,?)", (
                                        self.var_emp_id.get(),
                                        self.var_name.get(),
                                        self.var_email.get(),
                                        self.var_gender.get(),
                                        self.var_contact.get(),

                                        self.var_dob.get(),
                                        self.var_doj.get(),

                                        self.var_pass.get(),
                                        self.var_utype.get(),
                                        self.txt_address.get('1.0', END),
                                        self.var_salary.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee Added Successfully", parent=self.root)
                    self.show()
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])

        self.var_dob.set(row[5])
        self.var_doj.set(row[6])

        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END,row[9])
        self.var_salary.set(row[10])

    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error", "Employee ID must be required", parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID", parent=self.root)
                else:
                    cur.execute("Update employee set name=?, email=?, gender=?, contact=?, dob=?, doj=?, pass=?, utype=?, address=?, salary=? where  eid=?", (
                                        self.var_name.get(),
                                        self.var_email.get(),
                                        self.var_gender.get(),
                                        self.var_contact.get(),

                                        self.var_dob.get(),
                                        self.var_doj.get(),

                                        self.var_pass.get(),
                                        self.var_utype.get(),
                                        self.txt_address.get('1.0', END),
                                        self.var_salary.get(),
                                        self.var_emp_id.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error", "Employee ID must be required", parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?", parent=self.root)
                    if op==True:
                        cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Employee Deleted Successfully", parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")

        self.var_dob.set("")
        self.var_doj.set("")

        self.var_pass.set("")
        self.var_utype.set("Select")
        self.txt_address.delete('1.0', END)
        self.var_salary.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()

    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error", "Select search by option", parent=self.root)

            elif self.var_searchtxt.get()=="":   
                messagebox.showerror("Error", "Select input should be required", parent=self.root)

            else:
                cur.execute("Select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('',END,values=row)

                else:
                    messagebox.showerror("Error", "No record found.", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)



    def exit(self):
        self.root.destroy()

if __name__ =="__main__":
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()