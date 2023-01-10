import mysql.connector
import init_menu
def insert():
     customer_name=input("Please enter name: ")
     address=input("Please enter address: ")
     phone_no=input("Please enter phone no: ")
     #con is object as variable
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     query=("insert into customer(customer_name,address,phone_no) values('"+customer_name+"','"+address+"','"+phone_no+"')")
        
     cursor.execute(query)
     con.commit()
     print ("RECORD INSERTED SUCCESSFULLY")
     GetAll()
     cursor.close()
     if(con.is_connected()):
          con.close()
def delete():
     Search()
     customer_id=input("Please enter Customer Id: ")
     #con is object as variable
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     query="delete from customer where customer_id='"+customer_id+"'"
     cursor.execute(query)
     con.commit()
     print ("RECORD DELETED SUCCESSFULLY")
     GetAll()
     cursor.close()
     if(con.is_connected()):
          con.close()

def Search():
     print("1-------------------Search By Customer Name-----------")
     print("2-------------------Get All Customers----------------")
     query="";
     ch=input("Enter Your Choice: ")
     if(ch=="1"):
          customer_name=input("Search Customer By Name: ")
          query="select * from customer where Customer_Name like '%"+customer_name+"%'"
     elif(ch=="2"):
          query="select * from customer"
     else:
          print("Invalid Choice")
          Search();
          
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     cursor.execute(query)
     records=cursor.fetchall()
     if(len(records)==0):
          print("No Record Found. Search Again!")
          Search();
     for row in records:
          print("Customer_id: ",row[0])
          print("Customer_Name: ",row[1])
          print("Address: ",row[2])
          print ("Phone_No: ",row[3],"\n")
     cursor.close()
     if(con.is_connected()):
          con.close()
 

def GetAll():
     
     #con is object as variable
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     query="select * from customer"
     cursor.execute(query)
     records=cursor.fetchall()
     for row in records:
          print("Customer_id: ",row[0])
          print("Customer_Name: ",row[1])
          print("Address: ",row[2])
          print ("Phone_No: ",row[3],"\n")
     
     cursor.close()
     if(con.is_connected()):
          con.close()

def update():
     Search()
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     cust_id=input("Enter the customer id to update it: ")
     ch=int(input("Press 1 to update customer name\nPress 2 to update customer address\nPress 3 to update customer phone number\nPress 4 to update all the fields\nEnter your choice: "))
     if(ch==1):
          cust_name=input("Enter the new name of the customer: ")
          query="update customer set customer_name='"+cust_name+"' where customer_id='"+cust_id+"'"
          cursor.execute(query)
          con.commit()
          cursor.close()
          
     elif(ch==2):
          cust_add=input("Enter the new address of the customer: ")
          query="update customer set address='"+cust_add+"' where customer_id='"+cust_id+"'"
          cursor.execute(query)
          con.commit()
          cursor.close()
          
     elif(ch==3):
          cust_p_no=input("Enter the new phone no. of the customer: ")
          query="update customer set phone_no='"+cust_p_no+"' where customer_id='"+cust_id+"'"
          cursor.execute(query)
          con.commit()
          cursor.close()
          #records=cursor.fetchall()
     elif(ch==4):
          cust_name=input("Enter the new name of the customer: ")
          cust_add=input("Enter the new address of the customer: ")
          cust_p_no=input("Enter the new phone no. of the customer: ")
          query="update customer set customer_name='"+cust_name+"',address='"+cust_add+"',phone_no='"+cust_p_no+"' where customer_id='"+cust_id+"'"
          cursor.execute(query)
          con.commit()
          cursor.close()
          #records=cursor.fetchall()
     

