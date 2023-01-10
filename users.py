import mysql.connector
import init_menu
def insert():
     user_name=input("Please enter Username: ")
     password=input("Please enter Password: ")
     #con is object as variable
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     query=("insert into users(user_name,password) values('"+user_name+"','"+password+"')")
     cursor.execute(query)
     con.commit()
     print ("RECORD INSERTED SUCCESSFULLY")
     GetAll()
     cursor.close()
     if(con.is_connected()):
          con.close()
def delete():
     search()
     user_name=input("Please enter the name of the user: ")
     #con is object as variable
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     query="delete from users where user_name='"+user_name+"'"
     cursor.execute(query)
     con.commit()
     print ("--------RECORD DELETED SUCCESSFULLY--------")
     GetAll()
     cursor.close()
     if(con.is_connected()):
          con.close()
def update():
     search()
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     user_id=(input("Enter the user id to change the password: "))
     password=input("Enter New Password: ")
     query="update users set password='"+password+"' where user_id='"+user_id+"'"     
     cursor.execute(query)
     con.commit()
     cursor.close()
     print ("----------Password updated successfully-----------")

def search():
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     name=input("Enter username search: ")
     query="select * from users where user_name like '%"+name+"%'"   
     cursor.execute(query)
     records=cursor.fetchall()
     cursor.close()
     if(len(records)==0):
          print("No Record Found. Search Again!")
          search();
     for row in records:
          
          print("User Id= ",row[0],"\n", "User name",row[1],"\n", "PASSWORD",row[2])
          print("-------------------------------------------------------")    

def GetAll():
     
     #con is object as variable
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     query="select * from users"
     cursor.execute(query)
     records=cursor.fetchall()
     
       
     for row in records:
          print("User Id: ",row[0])
          print("Username: ",row[1])
          print ("Password: ", row[2],"\n")
       
     cursor.close()
     if(con.is_connected()):
          con.close()


def Login():
     user_name=input("Please enter the Username:")
     password=input("Please enter the Password:")
     #con is object as variable
     con=mysql.connector.connect(host="localhost",user="root",password="students",database="main_stock")#for connection
     cursor=con.cursor()#cursor is used to exectue query con-detail cusror-execute, here command will be executed
     query="select * from users where user_name='"+user_name+"' and password='"+password+"'"
     cursor.execute(query)
     records=cursor.fetchall()
     if(len(records)>0):
          print("YOU ARE LOGGED IN")
          init_menu.ShowMenuOptions("MainMenu")
     else:
          print("Invalid username/password")
          Login()
     if(con.is_connected()):
          con.close()
