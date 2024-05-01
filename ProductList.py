import tkinter  as tk 
from tkinter.ttk import Treeview
from DataLayer import DALProduct

class frmProductList:
    def __init__(self):
        self.root =tk.Toplevel()
        self.root.geometry('1240x600')
        self.root.title('Customer List')
            
        self.tree1 = Treeview(self.root)
        self.tree1['columns']=('c1','c2')
            
        self.tree1.heading('#0',text='Customer Id')
        self.tree1.heading('c1',text='Product Name')
        self.tree1.heading('c2',text='Description')

        objDal = DALProduct()
        
        AllProducts = objDal.getProduct()
        
        i=0 
        
        for Product in AllProducts:
            self.tree1.insert('',i,text=Product.ProductId,values=(Product.Product_Name,Product.Description))
            
            i+=1 
            
        self.tree1.place(y=20)
        
    def Show_dialog(self):
        self.root.grab_set()
        self.root.wait_window()
     