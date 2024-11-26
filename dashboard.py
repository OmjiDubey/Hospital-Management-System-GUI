from tkinter import *
from tkinter import ttk,messagebox
import mysql.connector as sql
import time
import os

class HMS:
    def __init__(self,root):

        self.root = root
        self.root.geometry("1500x800+0+0")
        self.root.title("HMS-DASHBOARD")
        self.root.configure(bg='#ff8b33')
        self.root.state('zoomed')

        #==== TITLE ====
        self.icon_title = PhotoImage(file="IMG/hs_icon_s.png")
        title = Label(self.root,text="HOSPITAL MANAGMENT SYSTEM",image=self.icon_title,compound=LEFT,font=("times new roman",40),bg="#ff8b33",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

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
        frame_int = Frame(self.root,width=1400,height=680,bg='white',bd=1,relief=SOLID,highlightbackground='black',).place(x=60,y=130)
         #===FRAME FOR UNDERLINE===
        Frame(self.root,width=1400,height=2,bg="#141414").place(x=60,y=200)
        #===FRAME INSIDE INTERNAL FRAME===
        frame_int1 = Frame(self.root,width=1230,height=550,bg='#ff8b33',bd=3,relief=RAISED).place(x=180,y=220)

         #===DEFINING IMAGES FOR BUTTONS===
        self.home_btn = PhotoImage(file='IMG/home_btn.png')
        self.manage_btn = PhotoImage(file='IMG/manage_btn.png')
        self.view_btn = PhotoImage(file='IMG/view_btn.png')
        self.setting_btn = PhotoImage(file='IMG/setting_btn.png')
        self.exit_btn = PhotoImage(file='IMG/exit_btn.png')

        #=== ADDING BUTTONS ===
        btn_home = Button(self.root,image=self.home_btn,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=70,y=230)
        btn_manage = Button(self.root,image=self.manage_btn,command=self.manage,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=70,y=333)
        btn_view = Button(self.root,image=self.view_btn,command=self.view,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=70,y=435)
        btn_setting = Button(self.root,image=self.setting_btn,command=self.setting,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=70,y=537)
        btn_exit = Button(self.root,image=self.exit_btn,command=self.exit,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=70,y=640)

        #=== ADDING LABEL ABOVE LINE ===
        Label(self.root,text="ADMIN DASHBOARD",font=("times new roman",40),fg="black",bg='white',justify=CENTER,bd=1,relief=SOLID,highlightbackground='black',).place(x=60,y=130,width=1400,height=70)

        #=== HOME CONTENT ===
        self.lbl_patient = Label(self.root,text="TOTAL\n[ 0 ]\nPATIENTS",fg='#ff8b33', bg='white',bd=5,relief=RIDGE,font=('calibri',30,"bold"))
        self.lbl_patient.place(x=350,y=270,width=400,height=200)
        self.lbl_doctor = Label(self.root,text="TOTAL\n[ 0 ]\nDOCTORS",fg='#ff8b33', bg='white',bd=5,relief=RIDGE,font=('calibri',30,"bold"))
        self.lbl_doctor.place(x=900,y=270,width=400,height=200)
        self.lbl_staff = Label(self.root,text="TOTAL\n[ 0 ]\nEMPLOYEES",fg='#ff8b33', bg='white',bd=5,relief=RIDGE,font=('calibri',30,"bold"))
        self.lbl_staff.place(x=350,y=530,width=400,height=200)

        update_date_time()
        self.update_content()
        #=== INFO BUTTON ===
        from info import open_info
        self.info_btn = PhotoImage(file='IMG/info_btn.png')
        Button(self.root,image=self.info_btn,command=open_info,bg='white',highlightthickness=0,cursor="hand2",bd=5,relief=RIDGE).place(x=900,y=530,width=400,height=200)
#=======================================================================================================

    def update_content(self):
        self.con = sql.connect(host="localhost",user="root",password="access",database="GUI")
        self.cur = self.con.cursor()
        try:
            self.cur.execute('select*from patient')
            pr=self.cur.fetchall()
            self.lbl_patient.configure(text=f"TOTAL\n[ {str(len(pr))} ]\nPATIENTS")

            self.cur.execute('select*from doctor')
            nr=self.cur.fetchall()
            self.lbl_doctor.configure(text=f"TOTAL\n[ {str(len(nr))} ]\nDOCTORS")

            self.cur.execute('select*from employee')
            mr=self.cur.fetchall()
            self.lbl_staff.configure(text=f"TOTAL\n[ {str(len(mr))} ]\nEMPLOYEES")
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")




    def logout(self):
        self.root.destroy()
        os.system("python login_frame.py")
    def manage(self):
        self.root.destroy()
        os.system("python manage.py")
    def view(self):
        self.root.destroy()
        os.system("python view.py")
    def setting(self):
        self.root.destroy()
        os.system("python setting.py")
    def exit(self):
        self.root.destroy()

if __name__=="__main__":
    root = Tk()
    obj = HMS(root)
    root.mainloop()
