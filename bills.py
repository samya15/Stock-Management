import mysql.connector
import init_menu
import customer;
import datetime
import items;
import bill_details;
def insert():
     customer.Search()
     customer_id_fk=input("Please enter customer id: ")
     #con is object as variable
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     query=("insert into bills(customer_id_fk,date_of_billing) values('"+customer_id_fk+"','"+str(datetime.date.today())+"')")
     cursor.execute(query)
     bill_id=str(cursor.lastrowid)
     con.commit()
     #GetAll()
     cursor.close()
     if(con.is_connected()):
          con.close()
     print("Your Bill Id is: ",bill_id);
     bill_no_fk=bill_id;

     while(True):
          items.Search()
          item_id_fk=input("Please Enter Item Id: ")
          units=int(input("Please Enter Units: "))
          mrp=items.GetMrpByItem(item_id_fk);
          total=mrp*units;
          #con is object as variable
          con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
          cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
          query=("insert into bill_details(bill_no_fk,item_id_fk,units) values('"+str(bill_no_fk)+"','"+str(item_id_fk)+"','"+str(units)+"')")
          cursor.execute(query)
          con.commit()
          print ("RECORD INSERTED SUCCESSFULLY")
          cursor.close()
          if(con.is_connected()):
               con.close()

          ch=input("Press N to Discontinue: ")
          if(ch.lower()=="n"):
               init_menu.ShowMenuOptions("bills")
    

def BillSearch():
     customer.Search()
     customer_id=input("Enter Customer Id: ")
     #con is object as variable
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     query="select b.bill_no,c.customer_id,c.customer_name,b.date_of_billing from  bills b inner join customer c on b.customer_id_fk=c.customer_id where c.customer_id="+str(customer_id)+""

     cursor.execute(query)
     records=cursor.fetchall()
     for row in records:
          print("Bill NO: ",row[0],"\tCustomer Id: ",row[1],"\tCustomer Name: ",row[2],"\n")
          bill_details.GetByBillNo(row[0])
          print("---------------------------------------------------------------------------")
     cursor.close()
     if(con.is_connected()):
          con.close()
 
def delete():
     print("1---------------------Delete Customer Bills----------------------")
     print("2-----------------------Delete By Bill No.-----------------------")
     bill_no_fk=0;
     ch=input("Enter Your Choice: ")
     if(ch=="1"):
          customer.Search()
          BillSearch();
          bill_no_fk=input("Please enter bill no: ")
          
     elif(ch=="2"):
          bill_no_fk=input("Please enter bill no: ")
     else:
          print("Invalid Choice")
          delete();

     bill_details.delete(bill_no_fk)
     #con is object as variable
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     query="delete from bill_details where bill_no_fk='"+bill_no_fk+"'"
     cursor.execute(query)
     con.commit()
     #GetAll()
     cursor.close()
     if(con.is_connected()):
          con.close()
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     query="delete from bills where bill_no='"+bill_no_fk+"'"
     
     cursor.execute(query)
     con.commit()
     print ("RECORD DELETED SUCCESSFULLY")
     
     #GetAll()
     cursor.close()
     if(con.is_connected()):
          con.close()

 



def GetAll():
     
     #con is object as variable
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     query="select b.bill_no,c.customer_id,c.customer_name,b.date_of_billing,i.item_name,bd.units from bill_details bd inner join items i on bd.item_id_fk=i.item_id inner join bills b on bd.bill_no_fk=b.bill_no inner join customer c on b.customer_id_fk=c.customer_id"
     cursor.execute(query)
     records=cursor.fetchall()
     for row in records:
          print("Bill NO: ",row[0])
          print("Customer Id: ",row[1])
          print("Customer Name: ",row[2])
          print("Date of Billing: ",row[3])
          print("Item Name: ",row[4])
          print("Units: ",row[5],"\n")
     
          
     
     cursor.close()
     if(con.is_connected()):
          con.close()



