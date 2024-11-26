from tkinter import *
from tkinter import ttk,messagebox
import mysql.connector as sql
import os

class class_pat:
    def __init__(self,root):

        self.root = root
        self.root.geometry("1500x800+0+0")
        self.root.title("Patient's Section")
        self.root.configure(bg='#ff8b33')
        self.root.state('zoomed')

        #=== MAIN FRAME ===
        self.main_frame = Frame(self.root,bg='white').place(x=55,y=45,relwidth=0.92,relheight=0.92)
        #=== LEFT FRAME ===
        self.left_frame = Frame(self.root,highlightthickness=2,relief=SOLID,highlightbackground = "red", highlightcolor= "red",bg='white').place(x=75,y=130,relwidth=0.25,relheight=0.79)
        #=== LABEL FRAME FOR LEFT MENU ===
        LabelFrame(self.left_frame,text='Patient Management Options',font=5,bg='white').place(x=85,y=180,relwidth=0.238,relheight=0.6)
        #=== RIGHT FRAME ===
        self.right_frame = Frame(self.root,highlightthickness=2,relief=SOLID,highlightbackground = "red", highlightcolor= "red",bg='white').place(x=460,y=130,relwidth=0.64,relheight=0.79)
        #=== ADDING TITLE TO THE PAGE ===
        Label(self.root,text="Patient Management Section",font=("calibri",40),bg='white',fg='#ff8b33').place(x=60,y=45,relwidth=0.9,height=70)

        #=== PATIENT'S SECTION'S BUTTONS ===
        self.btn_add_pat = PhotoImage(file='IMG/add_pat.png')
        self.btn_upd_pat = PhotoImage(file='IMG/upd_pat.png')
        self.btn_del_pat = PhotoImage(file='IMG/del_pat.png')

        self.btn_back = PhotoImage(file='IMG/back_btn.png')

        #=== ADDING BUTTONS ===
        Button(self.left_frame,image=self.btn_add_pat,command=self.add_pat,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=103,y=280)
        Button(self.left_frame,image=self.btn_upd_pat,command=self.update,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=105,y=350)
        Button(self.left_frame,image=self.btn_del_pat,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=105,y=420)
        Button(self.left_frame,image=self.btn_back,command=self.back,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=105,y=550)

        cmb_search = ttk.Combobox(self.right_frame,values=("Search","Sort"),state='readonly',justify=CENTER,width=20,height=10)
        cmb_search.place(x=500,y=150)
        cmb_search.current(0)
        cmb_searchby = ttk.Combobox(self.right_frame,width=20,height=10,values=("Search by","ID","Name","Contact"),state='readonly',justify=CENTER)
        cmb_searchby.place(x=650,y=150)
        cmb_searchby.current(0)

        #=== ADDING SEARCH BAR ===
        search_entry = Entry(self.right_frame,width=45,bd=0,font=('calibri',12))
        search_entry.place(x=800,y=149)
        Frame(self.right_frame,height=1,bg='grey',width=350).place(x=800,y=170)

        def on_entry_click(event):
            """function that gets called whenever entry is clicked"""
            if search_entry.get() == 'Search Here...':
               search_entry.delete(0, "end") # delete all the text in the entry
               search_entry.insert(0, '') #Insert blank for user input
               search_entry.config(fg = 'black')

        def on_focusout(event):
            if search_entry.get() == '':
                search_entry.insert(0, 'Search Here...')
                search_entry.config(fg = 'grey')

        search_entry.insert(0, 'Search Here...')
        search_entry.bind('<FocusIn>', on_entry_click)
        search_entry.bind('<FocusOut>', on_focusout)
        search_entry.config(fg = 'grey')

        #=== ADDING SEARCH BUTTONS ===
        self.btn_search = PhotoImage(file='IMG/search.png')
        Button(self.right_frame,image=self.btn_search,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(y=137,x=1150)
        self.btn_view_all = PhotoImage(file='IMG/view_all.png')
        Button(self.right_frame,image=self.btn_view_all,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(y=137,x=1270)

        emp_frame = Frame(self.right_frame,relief=RIDGE)
        emp_frame.place(x=470,y=185,relwidth=0.63,relheight=0.7)

        #=== DEFINING SCROLLBARS ===
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        #=== ADDING HEADING IN TREEVIEW ===
        self.employee_table = ttk.Treeview(emp_frame,columns=("ID","fname","lname","dob","gender","contact","problem","addr"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        ttk.Style().configure("Treeview",font=(None,12),background="#D3D3D3")
        ttk.Style().configure("Treeview.Heading",font=(None,10))
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.employee_table.xview)
        scrolly.config(command=self.employee_table.yview)
        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.heading("ID",text="Employee's ID")
        self.employee_table.heading("fname",text="First Name")
        self.employee_table.heading("lname",text="Last Name")
        self.employee_table.heading("dob",text="D.O.B.")
        self.employee_table.heading("gender",text="Gender")
        self.employee_table.heading("contact",text="Contact")
        self.employee_table.heading("problem",text="Problem")
        self.employee_table.heading("addr",text="Address")
        self.employee_table["show"]="headings"

        self.employee_table.column("ID",width=120)
        self.employee_table.column("fname",width=110)
        self.employee_table.column("lname",width=110)
        self.employee_table.column("dob",width=130)
        self.employee_table.column("gender",width=110)
        self.employee_table.column("contact",width=100)
        self.employee_table.column("problem",width=150)
        self.employee_table.column("addr",width=150)

        self.show()
    
    #============================================================================================================================
    #===== UPDATE PATIENT ===
    def upd(self):
        global top
        top = Toplevel()
        top.geometry("1500x800+0+0")
        top.title("Patient's Section")
        top.configure(bg='#ff8b33')
        top.state('zoomed')

        #===== ALL VARIABLES ===
        self.var_pat_id=StringVar()
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_dob=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_problem=StringVar()
        self.var_addr=StringVar()

        #=== INTERNAL FRAME ===
        frame_int = Frame(top,width=1430,height=750,bg='white',bd=0,relief=SOLID,highlightbackground='black',).place(x=60,y=50)
        #=== TITLE ===
        title = Label(top,text="PATIENT REGISTRATION SECTION",font=("times new roman",40),bg="white",fg="#ff8b33",anchor="w",padx=20).place(x=300,y=70,relwidth=0.7,height=70)

        #=== ADDING LABEL FRAMES ===
        LabelFrame(top,text="Patient's Details",font=5,bg='white').place(x=130,y=170,relwidth=0.6,relheight=0.6)
        #LabelFrame(top,text="KK Hospital",font=5,bg="white").place(x=1100,y=170,relheight=0.6,relwidth=0.23)

        #=== ADDING HOSPITAL LOGO TO SECOND FRAME ===
        self.logo_main = PhotoImage(file="IMG/main_logo.png")
        Label(top,image=self.logo_main,bd=0,justify=CENTER).place(x=1150,y=300)

        #=== ADDING OPTIONS TO PAGE ===
        lbl_pat_id = Label(top,text="Patient ID",font=('calibri',20),bg='white').place(x=160,y=230)
        en_pat_id = Entry(top,textvariable=self.var_pat_id,width=25,border=0,font=('Arial',16)).place(x=295,y=232)
        Frame(top,width=330,height=2,bg="#141414").place(x=295,y=258)

        lbl_fname = Label(top,text="First Name",font=('calibri',20),bg='white').place(x=160,y=300)
        en_fname = Entry(top,textvariable=self.var_fname,width=21,border=0,font=('Arial',16)).place(x=295,y=302)
        Frame(top,width=250,height=2,bg="#141414").place(x=295,y=329)

        lbl_lname = Label(top,text="Last Name",font=('calibri',20),bg='white').place(x=600,y=300)
        en_lname = Entry(top,textvariable=self.var_lname,width=20,border=0,font=('Arial',16)).place(x=735,y=302)
        Frame(top,width=250,height=2,bg="#141414").place(x=735,y=329)

        lbl_dob = Label(top,text="D.O.B.",font=('calibri',20),bg='white').place(x=160,y=370)
        en_dob = Entry(top,textvariable=self.var_dob,width=20,border=0,font=('Arial',16)).place(x=295,y=370)
        Frame(top,width=250,height=2,bg="#141414").place(x=295,y=397)

        #=== ADDING COMBOBOX ===
        lbl_gender = Label(top,text="Gender",font=('calibri',20),bg='white').place(x=600,y=370)
        en_gender = ttk.Combobox(top,textvariable=self.var_gender,values=("-- Select --","Male","Female","Other"),font=20,state='readonly',justify=CENTER,width=20)
        en_gender.place(x=735,y=370)
        en_gender.current(0)

        lbl_contact = Label(top,text="Contact",font=('calibri',20),bg='white').place(x=160,y=440)
        en_contact = Entry(top,textvariable=self.var_contact,width=20,border=0,font=('Arial',16)).place(x=295,y=440)
        Frame(top,width=250,height=2,bg="#141414").place(x=295,y=467)

        lbl_spec = Label(top,text='Speciality',font=('calibri',20),bg='white').place(x=600,y=430)
        en_specs = ttk.Combobox(top,textvariable=self.var_dept,values=("-- Select --","Cardiology","Neurology","Urology","Dermatology","Orthopaedics","Pediatrics"),font=20,state='readonly',justify=CENTER,width=20)
        en_specs.place(x=735,y=430)
        en_specs.current(0)

        lbl_addr = Label(top,text="Address",font=('calibri',20),bg='white').place(x=160,y=510)
        en_addr = Entry(top,textvariable=self.var_addr,width=20,border=0,font=('Arial',16)).place(x=295,y=510)
        Frame(top,width=250,height=2,bg="#141414").place(x=295,y=537)

        #=== ADDING BUTTONS ===
        self.sub_btn = PhotoImage(file='IMG/sub_btn.png')
        self.cancel_btn = PhotoImage(file='IMG/cancel_btn.png')
        btn_sub = Button(top,command=self.update,image=self.sub_btn,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=295,y=700)
        cancel_sub = Button(top,command=self.cancel,image=self.cancel_btn,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=600,y=700)

        f=self.employee_table.focus()
        content=(self.employee_table.item(f))
        row=content['values']
        self.var_pat_id.set(row[0]),
        self.var_fname.set(row[1]),
        self.var_lname.set(row[2]),
        self.var_dob.set(row[3]),
        self.var_gender.set(row[4]),
        self.var_contact.set(row[5]),
        self.var_problem.set(row[6]),
        self.var_addr.set(row[7]),
       
        top.mainloop()
    #================================================================================================================================

    def submit(self):
        self.con = sql.connect(host="localhost",user="root",password="access",database="GUI")
        self.cur = self.con.cursor()
        try:
            if self.var_pat_id.get()=="":
                pass

            else:
                self.cur.execute("Select * from patient where pat_id=%s",(self.var_pat_id.get(),))
                row=self.cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Patient ID alreaady exists, try another")
                else:
                    self.cur.execute("insert into patient(pat_id,f_name,l_name,dob,gender,contact,problem,addr) values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                        self.var_pat_id.get(),
                                        self.var_fname.get(),
                                        self.var_lname.get(),
                                        self.var_dob.get(),
                                        self.var_gender.get(),
                                        self.var_contact.get(),
                                        self.var_problem.get(),
                                        self.var_addr.get(),
                    ))
                    self.con.commit()
                    messagebox.showinfo("Success","Patient registered seccuessfully")

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def cancel(self):
        self.root.destroy()
        os.system("python patient.py")

    def show(self):
        self.con = sql.connect(host="localhost",user="root",password="access",database="GUI")
        self.cur = self.con.cursor()
        try:
            self.cur.execute('select*from patient')
            rows=self.cur.fetchall()
            self.employee_table.delete(*self.employee_table.get_children())
            for row in rows:
                self.employee_table.insert('',END,values=row)

        except Exception as es:
                    messagebox.showerror(f'Error',f"Error Due to : {str(es)}",parent=self.root)
    
    def update(self):
            self.con = sql.connect(host="localhost",user="root",password="access",database="GUI")
            self.cur = self.con.cursor()
            self.cur.execute("Select * from patient where pat_id=%s",(self.var_pat_id.get(),))
            row=self.cur.fetchone()
            try:
                if row==None:
                    messagebox.showerror("Error","This Patient ID alreaady exists, try another")
                else:
                    self.cur.execute("update patient set f_name=%s,l_name=%s,dob=%s,gender=%s,contact=%s,problem=%s,addr=%s where pat_id=%s",(
                                        self.var_fname.get(),
                                        self.var_lname.get(),
                                        self.var_dob.get(),
                                        self.var_gender.get(),
                                        self.var_contact.get(),
                                        self.var_problem.get(),
                                        self.var_addr.get(),
                                        self.var_pat_id.get(),

                    ))
                    self.con.commit()
                    messagebox.showinfo("Success","Patient updated seccuessfully")
            except Exception as ex:
                print(str(ex))
            self.show()

    def add_pat(self):
        self.root.destroy()
        os.system("python add_pat.py")
    
    def back(self):
        self.root.destroy()
        os.system("python dashboard.py")


if __name__=="__main__":
    root = Tk()
    obj = class_pat(root)
    root.mainloop()
