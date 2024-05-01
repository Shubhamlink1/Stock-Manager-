create database ProjectDb
use ProjectDb

create table Customers(CustomerId int primary key identity,Name varchar(20),
Address varchar(50), Contact_No varchar(20))

create table Products(ProductId int primary key identity,Product_Name varchar(30),Description varchar(50))

create table Purchase(PurchaseId int primary key identity,PurchadeDate Date,InvoiceNo Varchar(20),
DistributerName varchar(20),Address varchar(30),ContactNo varchar(20))

create table PurchaseTransaction(TransactionId int primary key identity,
ProductId int references Products(ProductId),Quantity int,Price float,
PurchaseId int references Purchase(PurchaseId))

select*from Customers
select*from Products
select*from Purchase
select*from PurchaseTransaction

Select P.Product_Name, PT.Quantity, PT.Price, PT.Quantity*PT.Price as [Total]
From Products as [P], PurchaseTransaction as [PT] 
Where P.ProductId=PT.ProductId and PT.PurchaseID=2

create table Sales(SaleId int Primary key identity,Sale_Date Date,CustomerId int references Customers(CustomerId))

select S.SaleId,s.Sale_Date,C.Name
from Sales as [S],Customers as [C]
where s.CustomerId =c.CustomerId

create table SaleTransactions(SaleTransactionId int primary key identity,ProductId int references Products(ProductId),
Quantity int ,Price Float,SaleId int references Sales(SaleId))
select *from  Sales
select *from SaleTransactions
select P.Product_Name,ST.Quantity,ST.Price,ST.Quantity*st.Price as[Total]
from SaleTransactions as [ST],Products as [P],Sales[S]
where st.ProductId=p.ProductId and st.SaleId =s.SaleId 

select P.Product_Name,ST.Quantity,ST.Price,ST.Quantity*ST.Price as[Total] 
from SaleTransactions as [ST],Products as [P],Sales as [S]
where ST.ProductId = P.ProductId and ST.SaleId = S.SaleId and ST.SaleId=9

Select * From Sysobjects Where type='u' --for show all Tables

select P.Product_Name,PT.Quantity
from Products as [P],PurchaseTransaction as [PT]
where p.ProductId=pt.ProductId 

select p.Product_Name,ST.Quantity
from SaleTransactions as [ST],Products as [P]
where p.ProductId = st.ProductId

create table Users(UserNo int primary key identity,UserId varchar(30),Password varchar(20),User_Type varchar(20))
insert into Users values('Shubham123','SHub1234','Admin')
insert into Users values('Mohit123','MOhi1234','Admin')
insert into Users values('Rohit123','ROhi1234','Operator')
insert into Users values('Akshit123','AKsh1234','Operator')
insert into Users values('Ankit23','ANki1234','Operator')
insert into Users values('Sahil123','SAhi1234','Operator')
insert into Users values('Priyanshu','102081','Admin')

select*from Users
select*from Customers
select*from Sales
select*from SaleTransactions
select*from Products