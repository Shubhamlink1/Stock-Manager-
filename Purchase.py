import tkinter as tk
from tkinter.ttk import Combobox 
from DataLayer import DALProduct,DALPurchase
from Components import Purchase,PurchaseTransaction
from tkinter.ttk import Treeview

class frmPurchase():
    
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.geometry('1020x500')
        self.root.title('Purchase')
        
        self.Purchase_Date= tk.StringVar()
        self.InvoiceNo =tk.StringVar()
        self.Distributer_Name = tk.StringVar()
        self.Address = tk.StringVar()
        self.Contact_Number = tk.StringVar()
        self.Product=tk.StringVar()
        self.Quantity = tk.StringVar()
        self.Price = tk.StringVar()
        
        lbl1=tk.Label(self.root,text='Purchase Date')
        lbl1.place(x=30,y=28)
        lbl2=tk.Label(self.root,text='MM / DD/ YY')
        lbl2.place(x=150,y=50)
        
        self.ent1=tk.Entry(self.root,textvariable=self.Purchase_Date)
        self.ent1.place(x=140,y=30)
        
        lbl3=tk.Label(self.root,text='Invoice No')
        lbl3.place(x=300,y=28)
        
        self.ent2=tk.Entry(self.root,textvariable=self.InvoiceNo)
        self.ent2.place(x=390,y=30)
        
        lbl4=tk.Label(self.root,text='Distributer Name')
        lbl4.place(x=30,y=88)
        
        self.ent3=tk.Entry(self.root,textvariable=self.Distributer_Name)
        self.ent3.place(x=140,y=90)
        
        lbl5=tk.Label(self.root,text='Address')
        lbl5.place(x=300,y=90)
        
        self.ent4=tk.Entry(self.root,textvariable=self.Address)
        self.ent4.place(x=390,y=90)
        
        lbl6=tk.Label(self.root,text='Contact Number')
        lbl6.place(x=550,y=90)
        
        self.ent5=tk.Entry(self.root,textvariable=self.Contact_Number)
        self.ent5.place(x=650,y=90)
        
        lbl7=tk.Label(self.root,text='Product')
        lbl7.place(x=30,y=128)
        
        obj2 = DALProduct()
        self.AllProducts = obj2.getProduct()
        Productlist = []
        
        for product in self.AllProducts:
            Productlist.append(product.Product_Name)
        
        self.cmb1=Combobox(self.root,textvariable=self.Product)
        self.cmb1['values']=Productlist
        self.cmb1.config(state='readonly')
        self.cmb1.place(x=140,y=128)
        
        lbl1=tk.Label(self.root,text='Quantity')
        lbl1.place(x=300,y=128)
        
        self.ent6=tk.Entry(self.root,textvariable=self.Quantity)
        self.ent6.place(x=390,y=128)
        
        lbl1=tk.Label(self.root,text='Price')
        lbl1.place(x=550,y=128)
        
        self.ent7=tk.Entry(self.root,textvariable=self.Price)
        self.ent7.place(x=650,y=128)
        
        btn1=tk.Button(self.root,text='Add Details')
        btn1.place(x=850,y=125)
        
        btn1=tk.Button(self.root,text='Add Details',command=self.add_detail_click)
        btn1.place(x=850,y=125)
        
        self.tree1 = Treeview(self.root)
        self.tree1['columns']=('c1','c2','c3','c4')

        self.tree1.heading('#0',text='Product Id')
        self.tree1.heading('c1',text='Product Name')
        self.tree1.heading('c2',text='Quantity')
        self.tree1.heading('c3',text='Price')
        self.tree1.heading('c4',text='Total')


        self.tree1.place(x=10,y=200)
        
        btn1=tk.Button(self.root,text='Generate Bill',command=self.Save_click)
        btn1.place(x=500,y=450)
        
        self.objPurchase = Purchase()
        self.RowIndex = tk.IntVar()

    def Show_dialog(self):
        self.root.grab_set()
        self.root.wait_window()
    
    def Save_click(self):
        self.objPurchase.PurchaseDate=self.Purchase_Date.get()
        self.objPurchase.DistributerName = self.Distributer_Name.get()
        self.objPurchase.Address=self.Address.get()
        self.objPurchase.ContactNo = self.Contact_Number.get()
        self.objPurchase.InvoiceNo = self.InvoiceNo.get()
        
        self.ent1.delete(0, "end")
        self.ent2.delete(0, "end")
        self.ent3.delete(0, "end")
        self.ent4.delete(0, "end")
        self.ent5.delete(0, "end")
        self.ent6.delete(0, "end")
        self.ent7.delete(0, "end")
        self.cmb1.set('')
        
        
        objDAL = DALPurchase()
        if objDAL.add_purchase(self.objPurchase)==True:
            self.objPurchase.Transastions.clear()
            
       
    def add_detail_click(self):
        index= self.cmb1.current()
        
        PNM =self.AllProducts[index].Product_Name
        PID = self.AllProducts[index].ProductId
        
        Tot = int(self.Quantity.get())*float(self.Price.get())
        
        self.tree1.insert('',self.RowIndex.get(),text=PID,values=(PNM,self.Quantity.get(),self.Price.get(),Tot))
   
        tran = PurchaseTransaction()
        tran.ProductId =PID
        tran.Product_Name = PNM
        tran.Quantity = self.Quantity.get()
        tran.Price=self.Price.get()
        
        self.objPurchase.Transastions.append(tran)
        self.RowIndex.set(self.RowIndex.get()+1)




        
    