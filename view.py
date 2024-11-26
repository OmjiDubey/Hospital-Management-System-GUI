import time
from tkinter import *
from tkinter import ttk,messagebox
import mysql.connector as sql
import os

class class_view:
    def __init__(self,root):

        self.root = root
        self.root.geometry("1500x800+0+0")
        self.root.title("HMS-MANAGE")
        self.root.configure(bg='#ff8b33')
        self.root.state('zoomed')

        #==== TITLE ====
        self.icon_title = PhotoImage(file="IMG/hs_icon_s.png")
        Label(self.root,text="HOSPITAL MANAGMENT SYSTEM",image=self.icon_title,compound=LEFT,font=("times new roman",40),bg="#ff8b33",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #=== BTN_LOGOUT ===
        btn_logout = Button(self.root,command=self.logout,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1300,y=14,height=40,width=150)
        #=== CLOCK ===
        self.clock = Label(self.root,text="Welcome to KK Hospital Management System\t\t Date: DD-MM-YYYY\t\t Time: HH-MM-SS",font=("times new roman",15),bg="#4d636d",fg="white")
        self.clock.place(x=0,y=70,relwidth=1,height=30)

        #=== FUNCTION TO SET & UPDATE DATE & TIME ===
        def update_date_time():
            time_= time.strftime("%I:%M:%S")
            date_= time.strftime("%d-%m-%y")
            self.clock.config(text=f"Welcome to KK Hospital Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)} ")
            self.clock.after(200,update_date_time)
        update_date_time()

        #=== INTERNAL WHITE FRAME ===
        frame_int = Frame(self.root,width=1400,height=680,bg='white',highlightbackground='black',highlightthickness=1).place(x=60,y=130)
        #=== FRAME FOR UNDERLINE ===
        Frame(self.root,width=1400,height=2,bg="#141414").place(x=60,y=200)
        #=== FRAME INSIDE INTERNAL FRAME(ORANGE) ===
        self.frame_int1 = Frame(self.root,width=1234,height=550,bg='#ff8b33',bd=3).place(x=180,y=220)
        #=== ADDING TITLE OF SECTION ===
        Label(self.root,text="MANAGEMENT SECTION",font=("times new roman",40),fg="black",bd=1,relief=SOLID,highlightbackground='black',bg='white',justify=CENTER).place(x=60,y=130,width=1400,height=70)

        #===DEFINING IMAGES FOR BUTTONS===
        self.home_btn = PhotoImage(file='IMG/home_btn.png')
        self.manage_btn = PhotoImage(file='IMG/manage_btn.png')
        self.view_btn = PhotoImage(file='IMG/view_btn.png')
        self.setting_btn = PhotoImage(file='IMG/setting_btn.png')
        self.exit_btn = PhotoImage(file='IMG/exit_btn.png')

        #=== ADDING BUTTONS ===
        btn_home = Button(self.root,image=self.home_btn,command=self.dashboard,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=70,y=230)
        btn_manage = Button(self.root,image=self.manage_btn,command=self.manage,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=70,y=333)
        btn_view = Button(self.root,image=self.view_btn,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=70,y=435)
        btn_setting = Button(self.root,image=self.setting_btn,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=70,y=537)
        btn_exit = Button(self.root,image=self.exit_btn,command=self.exit,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=70,y=640)

    #==== DEFINING TREE VIEWS ======
        pat_lbl = Label(self.frame_int1,text='Patient View Section',font=10,bg='white',fg='black').place(height=25,width=613.5,x=183,y=223)
        doc_lbl = Label(self.frame_int1,text='Doctor View Section',font=10,bg='white',fg='black').place(height=25,width=613.5,x=798,y=223)
        emp_lbl = Label(self.frame_int1,text='Employee View Section',font=10,bg='white',fg='black').place(height=25,width=613.5,x=183,y=493)
        adm_lbl = Label(self.frame_int1,text='Admin View Section',font=10,bg='white',fg='black').place(height=25,width=613.5,x=798,y=493)
        
        self.frame1_l = Frame(self.frame_int1,bg='white')
        self.frame1_l.place(x=183,y=248,relwidth=0.4,relheight=0.29)
        self.frame3_l = Frame(self.frame_int1,bg='white')
        self.frame3_l.place(x=183,y=518,relwidth=0.4,relheight=0.295)
        self.frame2_r = Frame(self.frame_int1,bg='white')
        self.frame2_r.place(x=798,y=248,relwidth=0.4,relheight=0.29)
        self.frame4_r = Frame(self.frame_int1,bg='white')
        self.frame4_r.place(x=798,y=518,relwidth=0.4,relheight=0.295)
    
    #====== Patient section view =======
        #=== DEFINING SCROLLBARS ===
        scrolly=Scrollbar(self.frame1_l,orient=VERTICAL)
        scrollx=Scrollbar(self.frame1_l,orient=HORIZONTAL)
        
        #=== ADDING HEADING IN TREEVIEW ===
        self.patient_table = ttk.Treeview(self.frame1_l,columns=("ID","fname","lname","dob","gender","contact","problem","addr"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        ttk.Style().configure("Treeview.Heading",font=(None,10))
        ttk.Style().configure("Treeview", background="#D3D3D3",font=(None,12))
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.patient_table.xview)
        scrolly.config(command=self.patient_table.yview)
        self.patient_table.pack(fill=BOTH,expand=1)
        self.patient_table.heading("ID",text="Patient's ID")
        self.patient_table.heading("fname",text="First Name")
        self.patient_table.heading("lname",text="Last Name")
        self.patient_table.heading("dob",text="D.O.B.")
        self.patient_table.heading("gender",text="Gender")
        self.patient_table.heading("contact",text="Contact")
        self.patient_table.heading("problem",text="Problem")
        self.patient_table.heading("addr",text="Address")
        self.patient_table["show"]="headings"

        self.patient_table.column("ID",width=120)
        self.patient_table.column("fname",width=150)
        self.patient_table.column("lname",width=150)
        self.patient_table.column("gender",width=100)
        self.patient_table.column("dob",width=100)
        self.patient_table.column("contact",width=150)
        self.patient_table.column("problem",width=150)
        self.patient_table.column("addr",width=250)
        self.show_pat()
        
    #====== Doctor section view =====
        #=== DEFINING SCROLLBARS ===
        scrolly=Scrollbar(self.frame2_r,orient=VERTICAL)
        scrollx=Scrollbar(self.frame2_r,orient=HORIZONTAL)
        
        #=== ADDING HEADING IN TREEVIEW ===
        self.doctor_table = ttk.Treeview(self.frame2_r,columns=("ID","fname","lname","dob","gender","contact","dept","addr"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        ttk.Style().configure("Treeview", background="#D3D3D3",font=(None,12))
        ttk.Style().configure("Treeview.Heading",font=(None,10))
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.doctor_table.xview)
        scrolly.config(command=self.doctor_table.yview)
        self.doctor_table.pack(fill=BOTH,expand=1)
        self.doctor_table.heading("ID",text="Doctor's ID")
        self.doctor_table.heading("fname",text="First Name")
        self.doctor_table.heading("lname",text="Last Name")
        self.doctor_table.heading("dob",text="D.O.B.")
        self.doctor_table.heading("gender",text="Gender")
        self.doctor_table.heading("contact",text="Contact")
        self.doctor_table.heading("dept",text="Department")
        self.doctor_table.heading("addr",text="Address")
        self.doctor_table["show"]="headings"

        self.doctor_table.column("ID",width=120)
        self.doctor_table.column("fname",width=150)
        self.doctor_table.column("lname",width=150)
        self.doctor_table.column("gender",width=100)
        self.doctor_table.column("dob",width=100)
        self.doctor_table.column("contact",width=150)
        self.doctor_table.column("dept",width=150)
        self.doctor_table.column("addr",width=250)
        self.show_doc()
    #====== Employee section view =====
        #=== DEFINING SCROLLBARS ===
        scrolly=Scrollbar(self.frame3_l,orient=VERTICAL)
        scrollx=Scrollbar(self.frame3_l,orient=HORIZONTAL)
        
        #=== ADDING HEADING IN TREEVIEW ===
        self.employee_table = ttk.Treeview(self.frame3_l,columns=("ID","name","gender","dob","contact","dept","addr"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        ttk.Style().configure("Treeview.Heading",font=(None,10))
        ttk.Style().configure("Treeview", background="#D3D3D3",font=(None,12))
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.employee_table.xview)
        scrolly.config(command=self.employee_table.yview)
        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.heading("ID",text="Employee's ID")
        self.employee_table.heading("name",text="Name")
        self.employee_table.heading("gender",text="Gender")
        self.employee_table.heading("dob",text="D.O.B.")
        self.employee_table.heading("contact",text="Contact")
        self.employee_table.heading("dept",text="Department")
        self.employee_table.heading("addr",text="Address")
        self.employee_table["show"]="headings"

        self.employee_table.column("ID",width=120)
        self.employee_table.column("name",width=150)
        self.employee_table.column("gender",width=100)
        self.employee_table.column("dob",width=100)
        self.employee_table.column("contact",width=150)
        self.employee_table.column("dept",width=150)
        self.employee_table.column("addr",width=150)
        self.show_emp()
    #====== Admin section view =====
        #=== DEFINING SCROLLBARS ===
        scrolly=Scrollbar(self.frame4_r,orient=VERTICAL)
        scrollx=Scrollbar(self.frame4_r,orient=HORIZONTAL)
        
        #=== ADDING HEADING IN TREEVIEW ===
        self.admin_table = ttk.Treeview(self.frame4_r,columns=("name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        ttk.Style().configure("Treeview.Heading",font=(None,10))
        ttk.Style().configure("Treeview", background="#D3D3D3",font=(None,12))
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.admin_table.xview)
        scrolly.config(command=self.admin_table.yview)
        self.admin_table.pack(fill=BOTH,expand=1)
        self.admin_table.heading("name",text="Admin's Username")
        self.admin_table["show"]="headings"
        self.admin_table.column("name",width=200)
        self.show_adm()
#===========================================================================================================================================================
    
    def show_doc(self):
        self.con = sql.connect(host="localhost",user="root",password="access",database="GUI")
        self.cur = self.con.cursor()
        try:
            self.cur.execute('select*from doctor')
            rows=self.cur.fetchall()
            self.doctor_table.delete(*self.doctor_table.get_children())
            for row in rows:
                self.doctor_table.insert('',END,values=row)

        except Exception as es:
                    messagebox.showerror(f'Error',f"Error Due to : {str(es)}",parent=self.root)
    
    def show_pat(self):
        self.con = sql.connect(host="localhost",user="root",password="access",database="GUI")
        self.cur = self.con.cursor()
        try:
            self.cur.execute('select*from patient')
            rows=self.cur.fetchall()
            self.patient_table.delete(*self.patient_table.get_children())
            for row in rows:
                self.patient_table.insert('',END,values=row)

        except Exception as es:
                    messagebox.showerror(f'Error',f"Error Due to : {str(es)}",parent=self.root)
    
    def show_emp(self):
        self.con = sql.connect(host="localhost",user="root",password="access",database="GUI")
        self.cur = self.con.cursor()
        try:
            self.cur.execute('select*from employee')
            rows=self.cur.fetchall()
            self.employee_table.delete(*self.employee_table.get_children())
            for row in rows:
                self.employee_table.insert('',END,values=row)

        except Exception as es:
                    messagebox.showerror(f'Error',f"Error Due to : {str(es)}",parent=self.root)
    
    def show_adm(self):
        self.con = sql.connect(host="localhost",user="root",password="access",database="GUI")
        self.cur = self.con.cursor()
        try:
            self.cur.execute('select*from login')
            rows=self.cur.fetchall()
            self.admin_table.delete(*self.admin_table.get_children())
            for row in rows:
                self.admin_table.insert('',END,values=row)

        except Exception as es:
                    messagebox.showerror(f'Error',f"Error Due to : {str(es)}",parent=self.root)
    
    
    
    
    def dashboard(self):
        self.root.destroy()
        os.system("python dashboard.py")
    def logout(self):
        self.root.destroy()
        os.system("python login_frame.py")
    def manage(self):
        self.root.destroy()
        os.system("python manage.py")
    def exit(self):
        self.root.destroy()


if __name__=="__main__":
    root = Tk()
    obj = class_view(root)
    root.mainloop()