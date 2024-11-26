from tkinter import *
from tkinter import ttk,messagebox
import mysql.connector as sql
import os

class class_add_emp:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1500x800+0+0")
        self.root.title("Employee's Section")
        self.root.configure(bg='#ff8b33')
        self.root.state('zoomed')

        #===== ALL VARIABLES ===
        self.var_emp_id=StringVar()
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_dob=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_dept=StringVar()
        self.var_addr=StringVar()

        #=== INTERNAL FRAME ===
        frame_int = Frame(self.root,width=1430,height=750,bg='white',bd=0,relief=SOLID,highlightbackground='black',).place(x=60,y=50)
        #=== TITLE ===
        title = Label(self.root,text="EMPLOYEE REGISTRATION SECTION",font=("times new roman",40),bg="white",fg="#ff8b33",anchor="w",padx=20).place(x=300,y=70,relwidth=0.7,height=70)

        #=== ADDING LABEL FRAMES ===
        LabelFrame(self.root,text="Employee's Details",font=5,bg='white').place(x=130,y=170,relwidth=0.6,relheight=0.6)

        #=== ADDING HOSPITAL LOGO TO SECOND FRAME ===
        self.logo_main = PhotoImage(file="IMG/main_logo.png")
        Label(self.root,image=self.logo_main,bd=0,justify=CENTER).place(x=1150,y=300)

        #=== ADDING OPTIONS TO PAGE ===
        lbl_emp_id = Label(self.root,text="Employee ID",font=('calibri',20),bg='white').place(x=160,y=230)
        en_emp_id = Entry(self.root,textvariable=self.var_emp_id,width=25,border=0,font=('Arial',16)).place(x=310,y=232)
        Frame(root,width=330,height=2,bg="#141414").place(x=310,y=258)

        lbl_fname = Label(self.root,text="First Name",font=('calibri',20),bg='white').place(x=160,y=300)
        en_fname = Entry(self.root,textvariable=self.var_fname,width=21,border=0,font=('Arial',16)).place(x=295,y=302)
        Frame(root,width=250,height=2,bg="#141414").place(x=295,y=329)

        lbl_lname = Label(self.root,text="Last Name",font=('calibri',20),bg='white').place(x=600,y=300)
        en_lname = Entry(self.root,textvariable=self.var_lname,width=20,border=0,font=('Arial',16)).place(x=735,y=302)
        Frame(root,width=250,height=2,bg="#141414").place(x=735,y=329)

        lbl_dob = Label(self.root,text="D.O.B.",font=('calibri',20),bg='white').place(x=160,y=370)
        en_dob = Entry(self.root,textvariable=self.var_dob,width=20,border=0,font=('Arial',16)).place(x=295,y=370)
        Frame(root,width=250,height=2,bg="#141414").place(x=295,y=397)

        #=== ADDING COMBOBOX ===
        lbl_gender = Label(self.root,text="Gender",font=('calibri',20),bg='white').place(x=600,y=370)
        en_gender = ttk.Combobox(self.root,textvariable=self.var_gender,values=("-- Select --","Male","Female","Other"),font=20,state='readonly',justify=CENTER,width=20)
        en_gender.place(x=735,y=370)
        en_gender.current(0)

        lbl_contact = Label(self.root,text="Contact",font=('calibri',20),bg='white').place(x=160,y=440)
        en_contact = Entry(self.root,textvariable=self.var_contact,width=20,border=0,font=('Arial',16)).place(x=295,y=440)
        Frame(root,width=250,height=2,bg="#141414").place(x=295,y=467)

        lbl_dept = Label(self.root,text='Department',font=('calibri',20),bg='white').place(x=600,y=430)
        en_dept = Entry(self.root,textvariable=self.var_dept,width=20,border=0,font=('Arial',16),bg='white').place(x=745,y=430)
        Frame(self.root,width=250,height=2,bg="#141414").place(x=745,y=457)

        lbl_addr = Label(self.root,text="Address",font=('calibri',20),bg='white').place(x=160,y=510)
        en_addr = Entry(self.root,textvariable=self.var_addr,width=30,border=0,font=('Arial',16)).place(x=295,y=510)
        Frame(root,width=375,height=2,bg="#141414").place(x=295,y=537)

        #=== ADDING BUTTONS ===
        self.sub_btn = PhotoImage(file='IMG/sub_btn.png')
        self.cancel_btn = PhotoImage(file='IMG/cancel_btn.png')
        btn_sub = Button(self.root,command=self.submit,image=self.sub_btn,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=295,y=700)
        cancel_sub = Button(self.root,command=self.cancel,image=self.cancel_btn,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=600,y=700)
#====================================================================================================================================

    def submit(self):
        self.con = sql.connect(host="localhost",user="root",password="access",database="GUI")
        self.cur = self.con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID is must required",parent=self.root)

            else:
                self.cur.execute("Select * from employee where emp_id=%s",(self.var_emp_id.get(),))
                row=self.cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Employee ID alreaady exists, try another")
                else:
                    self.cur.execute("insert into employee(emp_id,f_name,l_name,dob,gender,contact,dept,addr) values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                        self.var_emp_id.get(),
                                        self.var_fname.get(),
                                        self.var_lname.get(),
                                        self.var_dob.get(),
                                        self.var_gender.get(),
                                        self.var_contact.get(),
                                        self.var_dept.get(),
                                        self.var_addr.get(),
                    ))
                    self.con.commit()
                    messagebox.showinfo("Success","Employee registered seccuessfully")

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def cancel(self):
        self.root.destroy()
        os.system("python staff.py")

if __name__=="__main__":
    root = Tk()
    obj = class_add_emp(root)
    root.mainloop()
