from tkinter import *
from tkinter import ttk,messagebox
import mysql.connector as sql
import os

class class_staff:
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

        #=== EMPLOYEE'S SECTION'S BUTTONS ===
        self.btn_add_emp = PhotoImage(file='IMG/add_emp.png')
        self.btn_upd_emp = PhotoImage(file='IMG/upd_emp.png')
        self.btn_del_emp = PhotoImage(file='IMG/del_emp.png')

        self.btn_back = PhotoImage(file='IMG/back_btn.png')

        #=== ADDING BUTTONS ===
        Button(self.left_frame,image=self.btn_add_emp,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=103,y=280)
        Button(self.left_frame,image=self.btn_upd_emp,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=105,y=350)
        Button(self.left_frame,image=self.btn_del_emp,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=105,y=420)
        Button(self.left_frame,image=self.btn_back,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=105,y=550)

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
        self.employee_table = ttk.Treeview(emp_frame,columns=("ID","name","gender","dob","contact","dept","addr"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        ttk.Style().configure("Treeview", background="#D3D3D3")
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.employee_table.xview)
        scrolly.config(command=self.employee_table.yview)
        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.heading("ID",text="Doctor's ID")
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




if __name__=="__main__":
    root = Tk()
    obj = class_staff(root)
    root.mainloop()
