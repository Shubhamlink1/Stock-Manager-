import tkinter as tk 
from tkinter import messagebox
from Login import frmlogin
from Addcustomer import frmaddCustomer
from Customerlist import frmCustomerList
from products import frmaddProduct
from ProductList import frmProductList
from Purchase import frmPurchase
from Purchaselist import frmPurchaseList
from AddSale import frmAddsale
from SaleList import frmSaleList

class frmGateway:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('600x600')
        self.root.title('Gateway')
        
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)

        self.Login = tk.Menu()
        self.Login.add_command(label='SignIn',command=self.signinClick)
        self.Login.add_command(label='SignOut',state = 'disable',command=self.signOutClick)
        self.Login.add_command(label='Exit',command=self.Exitclick)
        
        self.Customer= tk.Menu()
        self.Customer.add_command(label='Add',state='disable',command=self.AddCustomer_click)
        self.Customer.add_command(label='List',state = 'disable',command=self.CustomerList_Click)
        
        self.Masters =tk.Menu()
        self.Masters.add_cascade(label='Customer',menu=self.Customer)
        
        self.Product=tk.Menu()
        self.Product.add_command(label='Add',state='disable',command=self.AddProduct_Click)
        self.Product.add_command(label='List',state = 'disable',command=self.ProductList_Click)
        
        self.Masters.add_cascade(label='Product',menu=self.Product)
        
        self.Purchase = tk.Menu()
        self.Purchase.add_command(label='Add Purchase',state='disable',command=self.AddPurchase_Click)
        self.Purchase.add_command(label='View Purchase',state='disable',command=self.Purchaselist_click)
        
        self.Sale= tk.Menu()
        self.Sale.add_command(label='Add Sale',state = 'disable',command=self.AddSale_click)
        self.Sale.add_command(label='View Sale',state = 'disable',command=self.SalelistClick)
        
        self.Transactions=tk.Menu()
        self.Transactions.add_cascade(label='Purchase',menu=self.Purchase)
        self.Transactions.add_cascade(label='Sale',menu=self.Sale)
        self.Transactions.add_cascade(label='Stock Summary')
        
        self.menubar.add_cascade(label='Login',menu=self.Login)
        self.menubar.add_cascade(label='Masters',menu=self.Masters)
        self.menubar.add_cascade(label='Transaction',menu=self.Transactions)
        
        
        
    def Show_dialog(self):
        self.root.mainloop()
        
    def signinClick(self):
        frm=frmlogin()
        objuser=frm.Show_dialog()
        
        if objuser!=None:
            self.Login.entryconfig('SignOut',state = 'normal')
            self.Login.entryconfig('SignIn',state = 'disable')
            if objuser.User_Type == 'Admin':
                
                self.Product.entryconfig('Add',state = 'normal')
                self.Product.entryconfig('List',state = 'normal')
                
                self.Customer.entryconfig('Add',state = 'normal')
                self.Customer.entryconfig('List',state = 'normal')
                
                self.Purchase.entryconfig('Add Purchase',state = 'normal')
                self.Purchase.entryconfig('View Purchase',state = 'normal')
                
                self.Sale.entryconfig('Add Sale',state = 'normal')
                self.Sale.entryconfig('Add Sale',state = 'normal')
            else:
  
                self.Product.entryconfig('List',state = 'normal')
            
                self.Customer.entryconfig('List',state = 'normal')
                
                self.Purchase.entryconfig('Add Purchase',state = 'normal')
                self.Purchase.entryconfig('View Purchase',state = 'normal')
                
                self.Sale.entryconfig('Add Sale',state = 'normal')
                self.Sale.entryconfig('View Sale',state = 'normal')
            
               
            
    def signOutClick(self):
        self.signout = messagebox.askyesno('Gateway','Do you want to Signout the Account')
        if self.signout==True:
            
            self.Login.entryconfig('SignOut',state = 'disable')
            
            self.Product.entryconfig('Add',state = 'disable')
            self.Product.entryconfig('List',state = 'disable')
            
            self.Customer.entryconfig('Add',state = 'disable')
            self.Customer.entryconfig('List',state = 'disable')
            
            self.Purchase.entryconfig('Add Purchase',state = 'disable')
            self.Purchase.entryconfig('View Purchase',state = 'disable')
            
            self.Sale.entryconfig('Add Sale',state = 'disable')
            self.Sale.entryconfig('Add Sale',state = 'disable')
        
            self.Login.entryconfig('SignIn',state = 'normal')
            
    def AddCustomer_click(self):
        frm=frmaddCustomer()
        frm.Show_dialog()
        
        
    def CustomerList_Click(self):
         frm1=frmCustomerList()
         frm1.Show_dialog()
    def AddProduct_Click(self):
        frm2=frmaddProduct()
        frm2.Show_dialog()
    def ProductList_Click(self):
        frm3=frmProductList()
        frm3.Show_dialog()
    def AddPurchase_Click(self):
        frm4= frmPurchase()
        frm4.Show_dialog()
    def Purchaselist_click(self):
        frm5=frmPurchaseList()
        frm5.Show_dialog()
    def AddSale_click(self):
        frm6=frmAddsale()
        frm6.show_dialog()
    def SalelistClick(self):
        frm=frmSaleList()
        frm.Show_dialog()
    def Exitclick(self):
        self.cancel = messagebox.askyesno('Gateway','Do you want to close the application')
        if self.cancel==True:
            self.root.destroy()
        
obj1= frmGateway()
obj1.Show_dialog()