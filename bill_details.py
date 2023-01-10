import mysql.connector

def insert():
     
     bill_no_fk=input("Please enter Bill no: ")
     item_id_fk=input("Please enter item id: ")
     units=input("Please enter the units: ")
     #con is object as variable
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     query=("insert into bill_details(bill_no_fk,item_id_fk,units) values('"+bill_no_fk+"','"+item_id_fk+"','"+units+"')")
     
     cursor.execute(query)
     con.commit()
     print ("RECORD INSERTED SUCCESSFULLY")
     GetAll()
     cursor.close()
     if(con.is_connected()):
          con.close()

def delete(bill_no):
    
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     query="delete from bill_details where bill_no_fk='"+bill_no+"'"
     cursor.execute(query)
     con.commit()
     cursor.close()
     if(con.is_connected()):
          con.close()

def GetByBillNo(bill_no):
     
     #con is object as variable
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     query="select a.*,b.item_name from bill_details a inner join items b on b.item_id=a.item_id_fk where bill_no_fk="+str(bill_no)+""
     cursor.execute(query)
     records=cursor.fetchall()
     for row in records:
          print("\tItem Name: ",row[5],"\tCost: ",row[4],"\tUnits: ",row[3],"\n")
         
     
     cursor.close()
     if(con.is_connected()):
          con.close()
 
def Bill_Report_By_Item():

     #con is object as variable
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     query="select a.item_id,a.item_name,ifnull((select sum(units) from purchase_details fk1 where fk1.item_id_fk=a.item_id),0) as purchased,ifnull((select sum(units) from bill_details fk2 where fk2.item_id_fk=a.item_id),0) as Sold, (ifnull((select sum(units) from purchase_details fk1 where fk1.item_id_fk=a.item_id),0)-ifnull((select sum(units) from bill_details fk2 where fk2.item_id_fk=a.item_id),0)) from items a"
     cursor.execute(query)
     records=cursor.fetchall()
     for row in records:
          print("Item Id: ",row[0])
          print ("Item Name: ", row[1])
          print ("Total Purchased: ", row[2])
          print ("Total Sold: ", row[3])
          print ("Stock In Hand: ", row[4],"\n")
         
     cursor.close()
     if(con.is_connected()):
          con.close()

def search():
      #con is object as variable
     items=input("Enter the name of item: ")
     items=items+"%"
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_Stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     query="select * from items where item_name like '"+items+"'"
     cursor.execute(query)
     records=cursor.fetchall()
     if(len(records)==0):
          print("No record found. Please search again")
          search()
     for row in records:
          print("Item_id: ",row[0])
          print ("Item_name: ", row[1])
          print("cost: ",row[2])
          print ("MRP: ",row[3],"\n")
          
     cursor.close()
     if(con.is_connected()):
          con.close()
