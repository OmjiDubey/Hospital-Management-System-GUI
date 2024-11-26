from tkinter import *
from tkinter import messagebox
import mysql.connector as sql
import os
##010c48

class login:
    def __init__(self,root):
        #CREATING ROOT WINDOWS
        self.root = root
        self.root.geometry('1500x800+0+0')
        self.root.configure(bg='#ff8b33')
        self.root.title('HOSPITAL MANAGMENT SYSTEM-LOGIN')
        self.root.state('zoomed')

        #CREATING LOGIN FRAME
        myframe = Frame(self.root,width=500,height=600,bg='white').place(x=500,y=150)

        #ADDING LABELS IN FRAME
        l1 = Label(myframe,text='Username',font=("Arial",20), bg='white')
        l1.place(x=540,y=395)
        l2 = Label(myframe,text='Password',font=('Arial',20),bg='white')
        l2.place(x=540,y=500)

        #ADDING ENTRY WIDGETS
        self.e1=StringVar()
        self.e2=StringVar()
        e1_ = Entry(self.root,textvariable=self.e1,width=25,border=0,font=('Arial',18)).place(x=542,y=440)
        e2_ = Entry(self.root,textvariable=self.e2,show='*',width=25,border=0,font=('Arial',18)).place(x=542,y=545)

        #CREATING A FRAME WHICH SHOWS AS UNDERLINE FOR ENTRY-BOX
        Frame(self.root,width=350,height=2,bg="#141414").place(x=542,y=468)
        Frame(self.root,width=350,height=2,bg="#141414").place(x=542,y=573)

        #ADDING IMAGE
        from PIL import ImageTk
        self.imageb= ImageTk.PhotoImage(file="IMG/main_logo.png")

        label1 = Label(image=self.imageb,border=0,justify=CENTER)
        label1.place(x=600, y=160)

        def cmd():
            if self.e1.get()=='' or self.e2.get()=='':
                messagebox.showerror("Error","! ! All fields are required ! !",parent=self.root)
            else:
                try:
                    #CONNECTING MYSQL DATABASE FOR USERNAME AND PASSWORD
                    self.con = sql.connect(host="localhost",user="root",password="access",database="GUI")
                    self.cur = self.con.cursor()
                    self.cur.execute("select * from login where usrname=%s AND passwd=%s",(self.e1.get(),self.e2.get()))
                    raw = self.cur.fetchone()
                    if raw==None:
                        messagebox.showerror("Error",'Invalid USERNAME/PASSWORD',parent=self.root)
                    else:
                        self.root.destroy()
                        os.system("python dashboard.py")
                except Exception as es:
                    messagebox.showerror(f'Error',f"Error Due to : {str(es)}",parent=self.root)


        #Button_with hover effect
        def bttn(x,y,text,ecolor,lcolor):
            def on_entera(e):
                myButton1['background'] = ecolor #ffcc66
                myButton1['foreground']= lcolor  #000d33

            def on_leavea(e):
                myButton1['background'] = lcolor
                myButton1['foreground']= ecolor

            myButton1 = Button(self.root,text=text,
                           width=20,
                           height=2,
                           fg=ecolor,
                           border=0,
                           bg=lcolor,
                           activeforeground=lcolor,
                           activebackground=ecolor,
                               command=cmd)

            myButton1.bind("<Enter>", on_entera)
            myButton1.bind("<Leave>", on_leavea)

            myButton1.place(x=x,y=y)


        bttn(670,600,'L O G I N','white','#994422')


        
root=Tk()
obj=login(root)
root.mainloop()
