import mysql.connector
import init_menu
import suppliers;
import items;
import datetime;
def insert():
     receipt_no=input("Please enter receipt no:")
     suppliers.search();
     supp_id_fk=input("Please enter supplier id:")
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")
     cursor=con.cursor()
     query=("insert into purchase(receipt_no,date_of_purchase,supp_id_fk) values('"+receipt_no+"','"+str(datetime.date.today())+"','"+supp_id_fk+"')")
     cursor.execute(query)
     purchase_id=str(cursor.lastrowid)
     con.commit()
     cursor.close()
     print ("Your Purchase ID is:",purchase_id)
     if(con.is_connected()):
          con.close()
     purchase_id_fk=purchase_id
     items.Search();
     item_id_fk=input("Please enter Item id: ")
     cost=input("Please enter the cost: ")
     units=input("Please enter the units: ")
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")
     cursor=con.cursor()
     query=("insert into  purchase_details(purchase_id_fk,item_id_fk,cost,units) values('"+purchase_id_fk+"','"+item_id_fk+"','"+cost+"','"+units+"')")
     cursor.execute(query)
     con.commit()
     print ("RECORD INSERTED SUCCESSFULLY")
     cursor.close()
     if(con.is_connected()):
          con.close()
 



def Search():
     rec_no=input("Please enter receipt Number to search: ")
     #con is object as variable
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     query="select p.purchase_id,p.receipt_no,p.date_of_purchase,s.name from purchase p inner join suppliers s on p.supp_id_fk=s.supp_id where receipt_no like'%"+rec_no+"%'";
     cursor.execute(query)
     records=cursor.fetchall()
     if(len(records)==0):
          print("No Purchase History Found. Search Again!")
          Search();
     for row in records:
          print("Purchase_id:",row[0])
          print("receipt_no",row[1])
          print("date_of_purchase:",row[2])
          print("Supplier:",row[3],"\n")
          
     
     cursor.close()
     if(con.is_connected()):
          con.close()


def delete():
     Search();
     purchase_id=input("Please enter purchase_id: ")
     #con is object as variable
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     query="delete from purchase_details where purchase_id_fk='"+purchase_id+"'"
     cursor.execute(query)
     con.commit()
 
     #GetAll()
     cursor.close()
     if(con.is_connected()):
          con.close()
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     query="delete from purchase where purchase_id='"+purchase_id+"';"
     
     cursor.execute(query)
     con.commit()
     print ("Purchase History Deleted Successfully")
     
     #GetAll()
     cursor.close()
     if(con.is_connected()):
          con.close()

 
def GetAll():
     
     #con is object as variable
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     query="select p.purchase_id,p.receipt_no,p.date_of_purchase,s.name from purchase p inner join suppliers s on p.supp_id_fk=s.supp_id"
     cursor.execute(query)
     records=cursor.fetchall()
     for row in records:
          print("Purchase_id:",row[0])
          print("receipt_no",row[1])
          print("date_of_purchase:",row[2])
          print("Supplier:",row[3],"\n")
          
     
     cursor.close()
     if(con.is_connected()):
          con.close()
 
