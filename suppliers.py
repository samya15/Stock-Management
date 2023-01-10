import mysql.connector
import init_menu
def insert():
     name=input("Please enter supplier's name:")
     address=input("Please enter the address:")
     phone_no=input("Please enter phone no.:")
     #con is object as variable
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     query=("insert into suppliers(name,address,phone_no) values('"+name+"','"+address+"','"+phone_no+"')")
     
     cursor.execute(query)
     con.commit()
     print ("RECORD INSERTED SUCCESSFULLY")
     GetAll()
     cursor.close()
     if(con.is_connected()):
          con.close()

def delete():
     search();
     supplier_id=input("Please enter supplier id:")
     #con is object as variable
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     query="delete from suppliers where supp_id='"+supplier_id+"'"
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
     query="select * from suppliers"
     cursor.execute(query)
     records=cursor.fetchall()
     for row in records:
          print("Supp ID:",row[0])
          print("name:",row[1])
          print("Address:",row[2])
          print("phone no:",row[3],"\n")
     cursor.close()
     if(con.is_connected()):
          con.close()
def search():
     print("1-------------Search By Supplier Name-----------")
     print("2-------------Get All Suppliers----------------")
     query="";
     ch=input("Enter Your Choice: ")
     if(ch=="1"):
          name=input("Search Supplier By Name: ")
          query="select * from suppliers where name like '%"+name+"%'"
     elif(ch=="2"):
          query="select * from suppliers"
     else:
          print("Invalid Choice")
          Search();     
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     
     cursor.execute(query)
     records=cursor.fetchall()
     if(len(records)==0):
          print("No Supplier Found. Search Again!")
          search();
     for row in records:
          print("Supp ID:",row[0])
          print("name:",row[1])
          print("Address:",row[2])
          print("phone no:",row[3],"\n")
     cursor.close()
     if(con.is_connected()):
          con.close()

def update():
     search()
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     supp_id=input("Enter the supplier id to update it: ")
     ch=int(input("Press 1 to update supplier name\nPress 2 to update supplier address\nPress 3 to update supplier phone number\nPress 4 to update all the fields\nEnter your choice: "))
     if(ch==1):
          supp_name=input("Enter the new name of the supplier: ")
          query="update suppliers set name='"+supp_name+"' where supp_id='"+supp_id+"'"
          cursor.execute(query)
          con.commit()
          cursor.close()
          print("-------Record updated successfully-------")
          
     elif(ch==2):
          supp_add=input("Enter the new address of the supplier: ")
          query="update suppliers set address='"+supp_add+"' where supp_id='"+supp_id+"'"
          cursor.execute(query)
          con.commit()
          cursor.close()
          print("-------Record updated successfully-------")
          
     elif(ch==3):
          supp_p_no=input("Enter the new phone no. of the supplier: ")
          query="update suppliers set phone_no='"+supp_p_no+"' where supp_id='"+supp_id+"'"
          cursor.execute(query)
          con.commit()
          cursor.close()
          print("-------Record updated successfully-------")
     elif(ch==4):
          supp_name=input("Enter the new name of the supplier: ")
          supp_add=input("Enter the new address of the supplier: ")
          supp_p_no=input("Enter the new phone no. of the supplier: ")
          query="update suppliers set name='"+supp_name+"',address='"+supp_add+"',phone_no='"+supp_p_no+"' where supp_id='"+supp_id+"'"
          cursor.execute(query)
          con.commit()
          cursor.close()
          print("-------Record updated successfully-------")


