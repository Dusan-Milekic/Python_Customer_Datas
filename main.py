from contextlib import nullcontext
import Customer
import DataBase


#Opeingin connection to mySql
database = DataBase.OpenConnection()

#Get all datas
cursor = database.cursor()
cursor.execute("SELECT * FROM Korisnik")
result_datas = cursor.fetchall()

#Add datas to list customers
customers = []
for x in result_datas:
  customers.append(x)


#view all datas about customer
Customer.PaintRowsCustomers(customers)


