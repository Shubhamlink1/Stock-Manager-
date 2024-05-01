import pyodbc
from Components import  Product,Customer,Purchase,PurchaseTransaction,User,Sale,SaleTransaction

class DALCustomer:
    def __init__(self):
        self.con = pyodbc.connect("driver={sql server};server=DESKTOP-LT2RR3B\SHUBHAMDATA;database=ProjectDb;uid=sa;pwd=abc123#")
    def __del__(self):
        if self.con!=None:
            self.con.close()
            self.con = None
            
    def save_Customer(self, customer):
        saved = False
        try:
            cur = self.con.cursor()
            query = "insert into Customers values(?,?,?)"
            row = (customer.Name,customer.Address,customer.Contact_No)
            
            cur.execute(query, row)
            self.con.commit()
            saved = True
        except:
            self.con.rollback()
            
        return saved
    
    def getCustomer(self):
        AllCustomers = []
        cur = self.con.cursor()
        cur.execute('select*from Customers')
        records = cur.fetchall()
        
        for record in records:
            C=Customer()
            C.CustomerId=record[0]
            C.Name=record[1]
            C.Address=record[2]
            C.Contact_No=record[3]
            
            AllCustomers.append(C)
            
        return AllCustomers

class DALProduct:
    def __init__(self):
        self.con = pyodbc.connect("driver={sql server};server=DESKTOP-LT2RR3B\SHUBHAMDATA;database=ProjectDb;uid=sa;pwd=abc123#")
    def __del__(self):
        if self.con!=None:
            self.con.close()
            self.con = None
            
    def Save_Product(self,product):
        try:
            cur = self.con.cursor()
            query = "insert into Products values(?,?)"
            row = (product.Product_Name,product.Description)
            
            cur.execute(query,row)
            self.con.commit()
            saved = True
        except:
            self.con.rollback()
            
        return saved

    def getProduct(self):
        AllProducts = []
        cur = self.con.cursor()
        cur.execute('select*from Products')
        records = cur.fetchall()
        
        for record in records:
            P=Product()
            P.ProductId=record[0]
            P.Product_Name=record[1]
            P.Description=record[2]
            
            
            AllProducts.append(P)
            
        return AllProducts
    

class DALPurchase:
    def __init__(self):
        self.con = pyodbc.connect("driver={sql server};server=DESKTOP-LT2RR3B\SHUBHAMDATA;database=ProjectDb;uid=sa;pwd=abc123#")
    def __del__(self):
        if self.con!=None:
            self.con.close()
            self.con = None
    def add_purchase(self,purchase):
        saved = False
        
        cur = self.con.cursor()
        query = "insert into Purchase values(?,?,?,?,?)"
        row = (purchase.PurchaseDate,purchase.InvoiceNo,purchase.DistributerName,purchase.Address,purchase.ContactNo)
        
        cur.execute(query,row)
        self.con.commit()
        
        cur.execute('select top 1 PurchaseId  from Purchase order by PurchaseId desc')
        
        records = cur.fetchall()
        PID = records[0][0]
        
        cur1 = self.con.cursor()
        
        for tran in purchase.Transastions:
            query = 'Insert into PurchaseTransaction values (?,?,?,?)'
            row = (tran.ProductId,tran.Quantity,tran.Price,PID)
            
            cur1.execute(query,row)
            
        self.con.commit()
        
        saved = True
            
        return saved
    
    def getPurchaseRecords(self):
        AllCustomers = []
        cur = self.con.cursor()
        cur.execute('select*from Purchase')
        records = cur.fetchall()
        for record in records:
            P=Purchase()
            P.PurchaseId=record[0]
            P.PurchaseDate=record[1]
            P.InvoiceNo=record[2]
            P.DistributerName=record[3]
            P.Address=record[4]
            P.ContactNo=record[5]
            
            AllCustomers.append(P)
            
        return AllCustomers
    
    def getPurchaseTransactions(self, PurchaseId):
        allRecords=[]
        cur = self.con.cursor()
        
        query ="Select P.Product_Name, PT.Quantity, PT.Price, PT.Quantity*PT.Price as [Total] From Products as [P], PurchaseTransaction as [PT] Where P.ProductId=PT.ProductId and PT.PurchaseID=?"
        
        row = (PurchaseId)
        
        cur.execute(query, row)
        records = cur.fetchall()
        for record in records:
            T=PurchaseTransaction()
            T.Product_Name=record[0]
            T.Quantity=record[1]
            T.Price = record[2]
            T.Total=record[3]
    
            allRecords.append(T)
            
        return allRecords
         
            
class DALSales:
    def __init__(self):
        self.con = pyodbc.connect("driver={sql server};server=DESKTOP-LT2RR3B\SHUBHAMDATA;database=ProjectDb;uid=sa;pwd=abc123#")
        
    def __del__(self):
        if self.con!=None:
            self.con.close()
            self.con = None
            
    def add_sale(self,sale):
        saved = False
        
        cur = self.con.cursor()
        query = "insert into Sales values(?,?)"
        row =(sale.Sale_Date,sale.CustomerId)
        
        cur.execute(query,row)
        self.con.commit()
        
        cur.execute('Select SaleId from Sales')
        
        records = cur.fetchall()
        SID = records[0][0]
        
        cur = self.con.cursor()
        
        for St in sale.Transastion:
            query = 'Insert into SaleTransactions values (?,?,?,?)'
            row = (St.ProductId,St.Quantity,St.Price,SID)
            
            cur.execute(query,row)
            
        self.con.commit()
        
        saved = True
            
        return saved
    def getSalesRecords(self):
        Sales = []
        cur = self.con.cursor()
        cur.execute('select S.SaleId,s.Sale_Date,C.Name from Sales as [S],Customers as [C] where c.CustomerId=s.CustomerId')
        records = cur.fetchall()
        for record in records:
            S=Sale()
            S.SaleId=record[0]
            S.Sale_Date=record[1]
            S.Name=record[2]
            Sales.append(S)
            
        return Sales
    def getSaleTransactions(self, SaleId):
        allRecords=[]
        cur = self.con.cursor()
        
        query ="select P.Product_Name,ST.Quantity,ST.Price,ST.Quantity*st.Price as[Total] from SaleTransactions as [ST],Products as [P],Sales as [S] where st.ProductId=p.ProductId and ST.SaleId =s.SaleId and st.SaleId=?"
        
        row = (SaleId)
        
        cur.execute(query, row)
        records = cur.fetchall()
        for record in records:
            ST=SaleTransaction()
            ST.Product_Name=record[0]
            ST.Quantity=record[1]
            ST.Price = record[2]
            ST.Total=record[3]
    
            allRecords.append(ST)
            
        return allRecords
class DALUsers:
    def __init__(self):
        self.con = pyodbc.connect("driver={sql server};server=DESKTOP-LT2RR3B\SHUBHAMDATA;database=ProjectDb;uid=sa;pwd=abc123#")
    def __del__(self):
        if self.con!=None:
            self.con.close()
            self.con = None
    def Authenticate(self,Uid,pwd):
       objuser =None
       cur = self.con.cursor()
       cur.execute('select*from Users where UserId=? and Password=?',(Uid,pwd))
       records = cur.fetchall()
       if len(records)>0:
           objuser=User()
           objuser.UserNo=records[0][0]
           objuser.UserId=records[0][1]
           objuser.Password=records [0][2]
           objuser.User_Type=records [0][3]
           
           
       
       return objuser      

      
        
