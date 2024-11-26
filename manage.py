import time
from tkinter import *
import mysql.connector as sq
import os

class class_manage:
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

        #=== INTERNAL FRAME ===
        frame_int = Frame(self.root,width=1400,height=680,bg='white',highlightbackground='black',highlightthickness=1).place(x=60,y=130)
        #=== FRAME FOR UNDERLINE ===
        Frame(self.root,width=1400,height=2,bg="#141414").place(x=60,y=200)
        #===FRAME INSIDE INTERNAL FRAME===
        frame_int1 = Frame(self.root,width=1230,height=550,bg='#ff8b33',bd=3,relief=RAISED).place(x=180,y=220)
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
        btn_manage = Button(self.root,image=self.manage_btn,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=70,y=333)
        btn_view = Button(self.root,image=self.view_btn,command=self.view,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=70,y=435)
        btn_setting = Button(self.root,image=self.setting_btn,command=self.setting,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=70,y=537)
        btn_exit = Button(self.root,image=self.exit_btn,command=self.exit,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=70,y=640)

        #=== ADDING BUTTONS FOR DOCTOR,PATIENT & EMPLOYEES SECTIONS
        self.doc_btn = PhotoImage(file='IMG/doc_btn.png')
        self.pat_btn = PhotoImage(file='IMG/pat_btn.png')
        self.staff_btn = PhotoImage(file='IMG/staff_btn.png')

        btn_doc = Button(self.root,command=self.doct,bg='#ff8b33',cursor="hand2",image=self.doc_btn,relief=FLAT).place(x=350,y=350)
        btn_pat = Button(self.root,command=self.pat,bg='#ff8b33',cursor="hand2",image=self.pat_btn,relief=FLAT).place(x=700,y=350)
        btn_staff = Button(self.root,command=self.emp,bg='#ff8b33',cursor="hand2",image=self.staff_btn,relief=FLAT).place(x=1050,y=350)

        update_date_time()

#==============================================================================================
    
    def logout(self):
        self.root.destroy()
        os.system("python login_frame.py")
    def dashboard(self):
        self.root.destroy()
        os.system("python dashboard.py")
    def view(self):
        self.root.destroy()
        os.system("python view.py")
    def setting(self):
        self.root.destroy()
        os.system("python setting.py")
    def doct(self):
        self.root.destroy()
        os.system("python doctors.py")
    def pat(self):
        self.root.destroy()
        os.system("python patient.py")
    def emp(self):
        self.root.destroy()
        os.system("python staff.py")
    def exit(self):
        self.root.destroy()

if __name__=="__main__":
    root = Tk()
    obj = class_manage(root)
    root.mainloop()