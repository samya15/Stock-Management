import mysql.connector
import init_menu
def insert():
     purchase_id_fk=input("Please enter purchase id:")
     item_id_fk=input("Please enter Item id")
     cost=input("Please enter the cost")
     units=input("Please enter the units")
     #con is object as variable
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     query=("insert into  purchase_details(purchase_id_fk,item_id_fk,cost,units) values('"+purchase_id_fk+"','"+item_id_fk+"','"+cost+"','"+units+"')")
        
     cursor.execute(query)
     con.commit()
     print ("RECORD INSERTED SUCCESSFULLY")
     GetAll()
     cursor.close()
     if(con.is_connected()):
          con.close()

def delete():
     purchase_detail_id=input("Please enter purchase detail id:")
     #con is object as variable
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     query="delete from purchase_details where purchase_detail_id='"+purchase_detail_id+"'"
     cursor.execute(query)
     con.commit()
     print ("RECORD DELETED SUCCESSFULLY")
     GetAll()
     cursor.close()
     if(con.is_connected()):
          con.close()

def GetAll():
     
     #con is object as variable
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     query="select * from purchase_details"
     cursor.execute(query)
     records=cursor.fetchall()
     for row in records:
          print("purchase_detail_id:",row[0])
          print("purchase_id_fk",row[1])
          print("item_id_fk:",row[2])
          print("cost:",row[3])
          print("units:",row[4],"\n")
          
     
     cursor.close()
     if(con.is_connected()):
          con.close()


