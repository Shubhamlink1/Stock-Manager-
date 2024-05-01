import tkinter as tk 
from tkinter import messagebox
from Components import Product
from DataLayer import DALProduct

class frmaddProduct:
    def __init__(self):
        self.root=tk.Toplevel()
        
        self.root.geometry('500x500')
        self.root.title('Add Product')
        
        self.Pn =tk.StringVar()
        
        lbl1 = tk.Label(self.root,text='Product Name')
        lbl1.place(x=30,y=27)
        self.Ent1=tk.Entry(self.root,textvariable=self.Pn)
        self.Ent1.place(x=140,y=30)
        
        lbl1 = tk.Label(self.root,text='Description :')
        lbl1.place(x=30,y=58)
        
        self.txt1 = tk.Text(self.root,width=40,height=10)
        self.txt1.place(x=100,y=90)
        
        
        
        
        self.btn1 = tk.Button(self.root, text='Save',command=self.Save_Click)
        self.btn1.place(x=200,y=280)
        
        self.btn2 = tk.Button(self.root, text='Close',command=self.close_Click)
        self.btn2.place(x=300,y=280)
    
        
    def Show_dialog(self):
        self.root.grab_set()
        self.root.wait_window()
        
    def Save_Click(self):
       P=Product()
       P.Product_Name = self.Pn.get()
       P.Description= self.txt1.get("1.0", tk.END)
       
       self.Ent1.delete(0, "end")
       self.txt1.delete("1.0", tk.END)
       objDAL = DALProduct()
       if objDAL.Save_Product(P)==True:
           print('saved')
          
           
       objDAL = None
        
    def close_Click(self):
        self.a = messagebox.askyesno('Add Product','Do you want to close the application')
        if self.a == True:
            self.root.destroy()
        
