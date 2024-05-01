import tkinter as tk 
from tkinter import messagebox
from DataLayer import DALUsers


class frmlogin:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.geometry('300x200')
        self.root.title('Login')
        self.root.config(bg='#A5A5A2')
        
        self.v1=tk.StringVar()
        self.v2=tk.StringVar()
        
        self.lbl1=tk.Label(self.root,text='User Id')
        self.lbl1.place(x=30,y=30)
        
        self.ent1=tk.Entry(self.root,textvariable=self.v1)
        self.ent1.place(x=100,y=32)
        
        self.lbl2=tk.Label(self.root,text='Password')
        self.lbl2.place(x=30,y=60)
        
        self.ent2=tk.Entry(self.root,textvariable=self.v2)
        self.ent2.place(x=100,y=62)
        
        self.btn1=tk.Button(self.root,text='Sign In',command=self.SignIn_Click)
        self.btn1.place(x=100,y=90)
        
        self.btn2=tk.Button(self.root,text='Cancel',command=self.Cancel_click)
        self.btn2.place(x=160,y=90)
        
        self.objuser= None

    def Show_dialog(self):
        self.root.grab_set()
        self.root.wait_window()
        return self.objuser
        
    def SignIn_Click(self):
        
        objDal = DALUsers()
        
        self.objuser=objDal.Authenticate(self.v1.get(),self.v2.get())
        
        if self.objuser!=None:
            self.root.destroy()
        else:
            messagebox.showwarning('CAS','User Id or  Password incorrect')
    def Cancel_click(self):
        self.cancel = messagebox.askyesno('User Login','Do you want to close the application')
        if self.cancel==True:
            self.root.destroy()
        
