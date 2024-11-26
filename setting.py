from tkinter import *
from tkinter import messagebox
import mysql.connector as sql
import time
import os

class cd_pwd:
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
        btn_home = Button(self.root,image=self.home_btn,command=self.dashboard,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=70,y=230)
        btn_manage = Button(self.root,image=self.manage_btn,command=self.manage,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=70,y=333)
        btn_view = Button(self.root,image=self.view_btn,command=self.view,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=70,y=435)
        btn_setting = Button(self.root,image=self.setting_btn,command=self.setting,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=70,y=537)
        btn_exit = Button(self.root,image=self.exit_btn,command=self.exit,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=70,y=640)

        #=== ADDING LABEL ABOVE LINE ===
        Label(self.root,text="CHANGE ADMIN USER PASSWORD",font=("times new roman",40),fg="black",bg='white',justify=CENTER,bd=1,relief=SOLID,highlightbackground='black',).place(x=60,y=130,width=1400,height=70)

        #=== FUNCTION TO SET & UPDATE DATE & TIME ===
        def update_date_time():
            time_= time.strftime("%I:%M:%S")
            date_= time.strftime("%d-%m-%y")
            self.clock.config(text=f"Welcome to KK Hospital Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)} ")
            self.clock.after(200,update_date_time)
        update_date_time()

        #==== CREATING CHANGE PASSWORD FRAME ====
        myframe = Frame(self.root,width=500,height=500,bg='white').place(x=500,y=250)

        Label(self.root,text='Username',bg='white',font=('Arial',20)).place(x=530,y=270)
        Label(self.root,text='Old Password',bg='white',font=('Arial',20)).place(x=530,y=375)
        Label(self.root,text='New Password',bg='white',font=('Arial',20)).place(x=530,y=480)
        
        Frame(self.root,width=350,height=2,bg="#141414").place(x=532,y=350)
        Frame(self.root,width=350,height=2,bg="#141414").place(x=532,y=455)
        Frame(self.root,width=350,height=2,bg="#141414").place(x=532,y=560)

        self.e1=StringVar()
        self.e2=StringVar()
        self.e3=StringVar()
        e1_ = Entry(self.root,textvariable=self.e1,width=25,border=0,font=('Arial',18)).place(x=532,y=320)
        e2_ = Entry(self.root,textvariable=self.e2,width=25,border=0,font=('Arial',18)).place(x=532,y=425)
        e3_ = Entry(self.root,textvariable=self.e3,width=25,border=0,font=('Arial',18)).place(x=532,y=530)

        self.btn_submit = PhotoImage(file='IMG/sub_btn1.png')
        self.btn_cancel = PhotoImage(file='IMG/cancel_btn1.png')

        Button(self.root,image=self.btn_submit,command=self.submit,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=550,y=650)
        Button(self.root,image=self.btn_cancel,command=self.cancel,bd=0,highlightthickness=0,cursor="hand2",relief=RAISED).place(x=780,y=650)

    def submit(self):
        try:
            if self.e1.get()=="" or self.e2.get=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)

            else:
                #CONNECTING MYSQL DATABASE FOR USERNAME AND PASSWORD
                self.con = sql.connect(host="localhost",user="root",password="access",database="GUI")
                self.cur = self.con.cursor()
                self.cur.execute("Select * from login where usrname=%s AND passwd=%s",(self.e1.get(),self.e2.get(),))
                raw=self.cur.fetchone()
                if raw==None:
                    messagebox.showerror("Error!",'Invalid USERNAME/PASSWORD',parent=self.root)
                else:
                    self.cur.execute("update login set passwd=%s where usrname=%s",(self.e3.get(),self.e1.get(),))
                    self.con.commit()
                    messagebox.showinfo("Done","Password updated successfully")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
    
    def cancel(self):
        self.root.destroy()
        os.system("python setting.py")
#=========================================================================================================================================================

    def logout(self):
        self.root.destroy()
        os.system("python login_frame.py")
    def dashboard(self):
        self.root.destroy()
        os.system("python dashboard.py")
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
    obj = cd_pwd(root)
    root.mainloop()