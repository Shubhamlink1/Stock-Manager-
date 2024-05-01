import tkinter  as tk 
from tkinter.ttk import Treeview
from DataLayer import DALCustomer

class frmCustomerList:
    def __init__(self):
        self.root =tk.Toplevel()
        self.root.geometry('1240x600')
        self.root.title('Customer List')
            
        self.tree1 = Treeview(self.root)
        self.tree1['columns']=('c1','c2','c3')
            
        self.tree1.heading('#0',text='Customer Id')
        self.tree1.heading('c1',text='Customer Name')
        self.tree1.heading('c2',text='Address')
        self.tree1.heading('c3',text='ContactNo')
        
        objDal = DALCustomer()
        
        AllCustomers = objDal.getCustomer()
        
        i=0 
        
        for Customer in AllCustomers:
            self.tree1.insert('',i,text=Customer.CustomerId,values=(Customer.Name,Customer.Address,Customer.Contact_No))
            
            i+=1 
            
        self.tree1.place(y=20)
        
    def Show_dialog(self):
        self.root.grab_set()
        self.root.wait_window()
        
