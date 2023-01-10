import mysql.connector
import init_menu
def insert():
     item_name=input("Please enter item name: ")
     mrp=input("Please enter MRP: ")
     #con is object as variable
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     query=("insert into items(item_name,mrp) values('"+item_name+"','"+mrp+"')")
        
     cursor.execute(query)
     con.commit()
     print ("RECORD INSERTED SUCCESSFULLY")
     GetAll()
     cursor.close()
     if(con.is_connected()):
          con.close()
def update():
     Search();
     item_id=input("Please enter Item Id: ")
     item_name=input("Please enter Item Name: ")
     mrp=input("Please enter MRP: ")
     #con is object as variable
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     query=("update items set item_name='"+item_name+"',mrp='"+mrp+"'  where item_id='"+item_id+"'")
        
     cursor.execute(query)
     con.commit()
     print ("RECORD UPDATED SUCCESSFULLY")
     GetAll()
     cursor.close()
     if(con.is_connected()):
          con.close()
def Search():
     print("1-----------------Search By Item Name-----------")
     print("2------------------Get All Items----------------")
     query="";
     ch=input("Enter Your Choice: ")
     if(ch=="1"):
          item_name=input("Search Item By Name: ")
          query="select * from items where item_name like '%"+item_name+"%'"
     elif(ch=="2"):
          query="select * from items"
     else:
          print("Invalid Choice")
          Search();   
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     cursor.execute(query)
     records=cursor.fetchall()
     if(len(records)==0):
          print("No Item Found. Search Again!")
          Search();

     for row in records:
          print("Item_id: ",row[0])
          print("Item Name: ",row[1])      
          print ("MRP: ",row[3],"\n")
          
     cursor.close()
     if(con.is_connected()):
          con.close()


def GetMrpByItem(item_id):
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     query="select * from items where item_id='"+str(item_id)+"'"
     cursor.execute(query)
     records=cursor.fetchall()
     mrp=0;
     for row in records:
          mrp=float(row[3])
     
     cursor.close()
     if(con.is_connected()):
          con.close()
     return mrp

def delete():
     Search();
     item_id=input("Please enter item id: ")
     #con is object as variable
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     query="delete from items where Item_id='"+item_id+"'"
     
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
     query="select * from items"
     cursor.execute(query)
     records=cursor.fetchall()
     for row in records:
          print("Item_id: ",row[0])
          print("Item Name: ",row[1])      
          print ("MRP: ",row[3],"\n")
     
     cursor.close()
     if(con.is_connected()):
          con.close()


