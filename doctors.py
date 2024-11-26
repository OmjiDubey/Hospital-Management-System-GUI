from tkinter import *
from tkinter import ttk,messagebox
import mysql.connector as sql
import os

class class_doc:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1500x800+0+0")
        self.root.title("Doctor's Section")
        self.root.configure(bg='#ff8b33')
        self.root.state('zoomed')

        #=== MAIN FRAME ===
        self.main_frame = Frame(self.root,bg='white').place(x=55,y=45,relwidth=0.92,relheight=0.92)
        #=== LEFT FRAME ===
        self.left_frame = Frame(self.root,highlightthickness=2,relief=SOLID,highlightbackground = "red", highlightcolor= "red",bg='white').place(x=75,y=130,relwidth=0.25,relheight=0.79)
        #=== LABEL FRAME FOR LEFT MENU ===
        LabelFrame(self.left_frame,text='Doctor Management Options',font=5,bg='white').place(x=85,y=180,relwidth=0.238,relheight=0.6)
        #=== RIGHT FRAME ===
        self.right_frame = Frame(self.root,highlightthickness=2,relief=SOLID,highlightbackground = "red", highlightcolor= "red",bg='white').place(x=460,y=130,relwidth=0.64,relheight=0.79)
        #=== ADDING TITLE TO THE PAGE ===
        Label(self.root,text="Doctor Management Section",font=("calibri",40),bg='white',fg='#ff8b33').place(x=60,y=45,relwidth=0.9,height=70)

        #=== ADDING BUTTONS TO MANAGEMENT OPTIONS LABEL ===
            #=== DOCTOR'S SECTION'S BUTTONS ===
        self.btn_add_doc = PhotoImage(file='IMG/add_doc.png')
        self.btn_upd_doc = PhotoImage(file='IMG/upd_doc.png')
        self.btn_del_doc = PhotoImage(file='IMG/del_doc.png')

        self.btn_back = PhotoImage(file='IMG/back_btn.png')

            #=== ADDING BUTTONS ===
        Button(self.left_frame,image=self.btn_add_doc,command=self.add_doc,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=103,y=280)
        Button(self.left_frame,image=self.btn_upd_doc,command=self.upd,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=105,y=350)
        Button(self.left_frame,image=self.btn_del_doc,command=self.delete,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=105,y=420)
        Button(self.left_frame,image=self.btn_back,command=self.back,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=105,y=550)

        #=== ADDING COMBOBOXES FOR SEARCH FILTER ===
        self.cmb_search = Label(self.right_frame,text='Search Data Here',font=8,bg='white',fg='#ff8b33')
        self.cmb_search.place(x=470,y=145)
        self.cmb_searchby = ttk.Combobox(self.right_frame,width=20,height=10,values=("Search by","ID","Name"),state='readonly',justify=CENTER)
        self.cmb_searchby.place(x=650,y=150)
        self.cmb_searchby.current(0)
        #=== ADDING SEARCH BAR ===
        self.search_entry = Entry(self.right_frame,width=45,bd=0,font=('calibri',12))
        self.search_entry.place(x=800,y=149)
        Frame(self.right_frame,height=1,bg='grey',width=350).place(x=800,y=170)

        #=== FADED TEXT IN SEARCH BAR WHEN NOTHING IS INPUTTED ===
        #   {
        def on_focusout(event):
            if self.search_entry.get() == '':
                self.search_entry.insert(0, 'Search Here...')
                self.search_entry.config(fg = 'grey')

        def on_entry_click(event):
            """function that gets called whenever entry is clicked"""
            if self.search_entry.get() == 'Search Here...':
               self.search_entry.delete(0, "end") # delete all the text in the entry
               self.search_entry.insert(0, '') #Insert blank for user input
               self.search_entry.config(fg = 'black')

        self.search_entry.insert(0, 'Search Here...')
        self.search_entry.bind('<FocusIn>', on_entry_click)
        self.search_entry.bind('<FocusOut>', on_focusout)
        self.search_entry.config(fg = 'grey')
        #     }

        #=== ADDING SEARCH BUTTONS ===
        self.btn_search = PhotoImage(file='IMG/search.png')
        Button(self.right_frame,image=self.btn_search,command=self.search,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(y=137,x=1150)
        self.btn_view_all = PhotoImage(file='IMG/view_all.png')
        Button(self.right_frame,image=self.btn_view_all,command=self.show,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(y=137,x=1270)

        #=== FRAME FOR TREEVIEW ===
        doc_frame = Frame(self.right_frame,relief=RIDGE)
        doc_frame.place(x=470,y=185,relwidth=0.63,relheight=0.7)
        
        #=== DEFINING SCROLLBARS ===
        scrolly=Scrollbar(doc_frame,orient=VERTICAL)
        scrollx=Scrollbar(doc_frame,orient=HORIZONTAL)
        
        #=== ADDING HEADING IN TREEVIEW ===
        self.doctor_table = ttk.Treeview(doc_frame,columns=("ID","fname","lname","dob","gender","contact","dept","addr"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        ttk.Style().configure("Treeview",font=(None,12),background="#D3D3D3")
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
        self.doctor_table.column("fname",width=110)
        self.doctor_table.column("lname",width=110)
        self.doctor_table.column("dob",width=130)
        self.doctor_table.column("gender",width=100)
        self.doctor_table.column("contact",width=150)
        self.doctor_table.column("dept",width=150)
        self.doctor_table.column("addr",width=150)
        
        self.show()

#============================================================================================================================
    #===== UPDATE DOCTOR ===
    def upd(self):
        global top
        top = Toplevel()
        top.geometry("1500x800+0+0")
        top.title("Doctor's Section")
        top.configure(bg='#ff8b33')
        top.state('zoomed')

        #===== ALL VARIABLES ===
        self.var_doc_id=StringVar()
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_dob=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_specs=StringVar()
        self.var_addr=StringVar()

        #=== INTERNAL FRAME ===
        frame_int = Frame(top,width=1430,height=750,bg='white',bd=0,relief=SOLID,highlightbackground='black',).place(x=60,y=50)
        #=== TITLE ===
        title = Label(top,text="DOCTOR REGISTRATION SECTION",font=("times new roman",40),bg="white",fg="#ff8b33",anchor="w",padx=20).place(x=300,y=70,relwidth=0.7,height=70)

        #=== ADDING LABEL FRAMES ===
        LabelFrame(top,text="Doctor's Details",font=5,bg='white').place(x=130,y=170,relwidth=0.6,relheight=0.6)
        #LabelFrame(top,text="KK Hospital",font=5,bg="white").place(x=1100,y=170,relheight=0.6,relwidth=0.23)

        #=== ADDING HOSPITAL LOGO TO SECOND FRAME ===
        self.logo_main = PhotoImage(file="IMG/main_logo.png")
        Label(top,image=self.logo_main,bd=0,justify=CENTER).place(x=1150,y=300)

        #=== ADDING OPTIONS TO PAGE ===
        lbl_doc_id = Label(top,text="Doctor ID",font=('calibri',20),bg='white').place(x=160,y=230)
        en_doc_id = Entry(top,textvariable=self.var_doc_id,width=25,border=0,font=('Arial',16)).place(x=295,y=232)
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
        en_specs = ttk.Combobox(top,textvariable=self.var_specs,values=("-- Select --","Cardiology","Neurology","Urology","Dermatology","Orthopaedics","Pediatrics"),font=20,state='readonly',justify=CENTER,width=20)
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

        f=self.doctor_table.focus()
        content=(self.doctor_table.item(f))
        row=content['values']
        self.var_doc_id.set(row[0]),
        self.var_fname.set(row[1]),
        self.var_lname.set(row[2]),
        self.var_dob.set(row[3]),
        self.var_gender.set(row[4]),
        self.var_contact.set(row[5]),
        self.var_specs.set(row[6]),
        self.var_addr.set(row[7]),
       
        top.mainloop()
        #================================================================================================================================================
       
    def submit(self):
        self.con = sql.connect(host="localhost",user="root",password="access",database="GUI")
        self.cur = self.con.cursor()
        try:
            if self.var_doc_id.get()=="":
                messagebox.showerror("Error !",'Doctor ID is must required',parent=self.root)

            else:
                self.cur.execute("Select * from doctor where doc_id=%s",(self.var_doc_id.get(),))
                row=self.cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Doctor ID alreaady exists, try another")
                else:
                    self.cur.execute("insert into doctor(doc_id,f_name,l_name,dob,gender,contact,specs,addr) values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                        self.var_doc_id.get(),
                                        self.var_fname.get(),
                                        self.var_lname.get(),
                                        self.var_dob.get(),
                                        self.var_gender.get(),
                                        self.var_contact.get(),
                                        self.var_specs.get(),
                                        self.var_addr.get(),
                    ))
                    self.con.commit()
                    messagebox.showinfo("Success","Doctor registered seccuessfully")

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def delete(self):
        self.con = sql.connect(host="localhost",user="root",password="access",database="GUI")
        self.cur = self.con.cursor()
        cc=self.doctor_table.focus()
        content=(self.doctor_table.item(cc))
        pp=content['values'][0]
        ask=messagebox.askyesno("Confirm!","Do you want to delete the data?",parent=self.root)
        if ask==True:
            self.cur.execute('delete from doctor where doc_id=%s',(pp,))
            self.con.commit()
            messagebox.showinfo('Deleted','Data deleted successfully')
            self.show()
        
    def search(self):
        self.con = sql.connect(host="localhost",user="root",password="access",database="GUI")
        self.cur = self.con.cursor()
        if self.cmb_searchby.get()=="Search by":
            messagebox.showerror("Error!","Select any option to search data",parent=self.root)
        elif self.search_entry=="":
            messagebox.showerror("Error!","Search in input is required",parent=self.root)
        else:
            if self.cmb_searchby.get()=='ID':
                print(self.search_entry.get())
                self.cur.execute('select*from doctor where doc_id=%s',(self.search_entry.get(),))
                rows=self.cur.fetchall()
                if len(rows)!=0:
                    self.doctor_table.delete(*self.doctor_table.get_children())
                    for row in rows:
                        self.doctor_table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error!","No data found",parent=self.root)
            elif self.cmb_searchby.get()=='Name':
                self.cur.execute('select*from doctor where f_name=%s',(self.search_entry.get(),))
                rows=self.cur.fetchall()
                if len(rows)!=0:
                    self.doctor_table.delete(*self.doctor_table.get_children())
                    for row in rows:
                        self.doctor_table.insert('',END,values=row)

    def cancel(self):
        self.root.destroy()
        os.system("python doctors.py")

    def show(self):
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
    
    def update(self):
            self.con = sql.connect(host="localhost",user="root",password="access",database="GUI")
            self.cur = self.con.cursor()
            self.cur.execute("Select * from doctor where doc_id=%s",(self.var_doc_id.get(),))
            row=self.cur.fetchone()
            try:
                if row==None:
                    messagebox.showerror("Error","This Doctor ID alreaady exists, try another")
                else:
                    self.cur.execute("update doctor set f_name=%s,l_name=%s,dob=%s,gender=%s,contact=%s,specs=%s,addr=%s where doc_id=%s",(
                                        self.var_fname.get(),
                                        self.var_lname.get(),
                                        self.var_dob.get(),
                                        self.var_gender.get(),
                                        self.var_contact.get(),
                                        self.var_specs.get(),
                                        self.var_addr.get(),
                                        self.var_doc_id.get(),

                    ))
                    self.con.commit()
                    messagebox.showinfo("Success","Doctor updated seccuessfully")
            except Exception as ex:
                print(str(ex))
            self.show()

    def add_doc(self):
        self.root.destroy()
        os.system("python add_doc.py")
    def back(self):
        self.root.destroy()
        os.system("python dashboard.py")

if __name__=="__main__":
    root = Tk()
    obj = class_doc(root)
    root.mainloop()
