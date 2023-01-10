import users
import customer
import suppliers
import items
import purchase
import purchase_details
import bills
import bill_details
import datetime
def ShowMenuOptions(choice):
     if(choice=="MainMenu"):
          print("---------------------------------MAIN MENU---------------------------")
          print("1.-----------------------------MANAGE USERS--------------------------")
          print("2.-----------------------------MANAGE CUSTOMERS----------------------")
          print("3.-----------------------------MANAGE SUPPLIER-----------------------")
          print("4.-----------------------------MANAGE ITEMS--------------------------")
          print("5.-----------------------------MANAGE PURCHASE-----------------------")
          print("6.-----------------------------MANAGE BILLS--------------------------")
          print("7.-----------------------------MANAGE REPORTS------------------------")
          ch=int(input("Enter your choice: "))
          if(ch==1):
               try:
                    ShowMenuOptions("Users")
               except Exception as e:
                    print("Something went wrong. We are working on it.");
                    obj=open("errorLog.txt","a")
                    d=str(str(e)+"_"+str(datetime.datetime.now()))
                    obj.write(d)
                    obj.close()
          elif(ch==2):
               try:
                    ShowMenuOptions("customers")
               except Exception as e:
                    print("Something went wrong. We are working on it.");
                    obj=open("errorLog.txt","a")
                    d=str(str(e)+"_"+str(datetime.datetime.now()))
                    obj.write(d)
                    obj.close()          
          elif(ch==3):
               try:
                    ShowMenuOptions("suppliers")
               except Exception as e:
                    print("Something went wrong. We are working on it.");
                    obj=open("errorLog.txt","a")
                    d=str(str(e)+"_"+str(datetime.datetime.now()))
                    obj.write(d)
                    obj.close()
          elif(ch==4):
               try:
                    ShowMenuOptions("items")
               except Exception as e:
                    print("Something went wrong. We are working on it.");
                    obj=open("errorLog.txt","a")
                    obj.write(str(str(e)+"_"+str(datetime.datetime.now())))
                    obj.close()
          elif(ch==5):
               try:
                    ShowMenuOptions("purchase")
               except Exception as e:
                    print("Something went wrong. We are working on it.");
                    obj=open("errorLog.txt","a")
                    d=str(str(e)+"_"+str(datetime.datetime.now()))
                    obj.write(d)
                    obj.close()
                    
          elif(ch==6):
               try:
                    ShowMenuOptions("bills")
               except Exception as e:
                    print("Something went wrong. We are working on it.");
                    obj=open("errorLog.txt","a")
                    d=str(str(e)+"_"+str(datetime.datetime.now()))
                    obj.write(d)
                    obj.close()
                    
          elif(ch==7):
               try:
                    ShowMenuOptions("report")
               except Exception as e:
                    print("Something went wrong. We are working on it.");
                    obj=open("errorLog.txt","a")
                    d=str(str(e)+"_"+str(datetime.date.now()))
                    obj.write(d)
                    obj.close()
                    
     elif(choice=="Users"):
          print("1.---------------------------ADD USERS------------------------")
          print("2.-------------------------DELETE USERS-----------------------")
          print("3.------------------------SHOW ALL USERS----------------------")
          print("4.------------------------UPDATE PASSWORD---------------------")
          print("5.---------------------------MAIN MENU------------------------")
          ch=int(input("Enter your choice: "))
          if(ch==1):
               try:
                    users.insert()
                    ShowMenuOptions("Users")
               except Exception as e:
                    print("Something went wrong. We are working on it.");
                    obj=open("errorLog.txt","a")
                    obj.write(e+"_"+str(datetime.date.now()))
                    obj.close()
                    
          elif(ch==2):               
               users.delete()
               ShowMenuOptions("Users")
          elif(ch==3):
               users.GetAll()
               ShowMenuOptions("Users")
          elif(ch==4):
               users.update()
               ShowMenuOptions("Users")  
          elif(ch==5):
               ShowMenuOptions("MainMenu")
               
     elif(choice=="customers"):
          print("1-----------------------------Add customer---------------------------")
          print("2.--------------------------Delete customers-------------------------")
          print("3.--------------------------Search Customers-------------------------")
          print ("4.-------------------------Update customers-------------------------")
          print("5.-----------------------------Main Menu-----------------------------")
          ch=int(input("Enter your choice: "))
          if(ch==1):
               customer.insert()
               ShowMenuOptions("customers")
          elif(ch==2):
               customer.delete()
               ShowMenuOptions("customers")
          elif(ch==3):
               customer.Search()
               ShowMenuOptions("customers")
          elif(ch==4):
               customer.update()
               ShowMenuOptions("customers")
          elif(ch==5):
               ShowMenuOptions("MainMenu")
               
     elif(choice=="suppliers"):
          print("1-----------------------------Add Supplier---------------------------")
          print("2.-------------------------Delete Suppliers--------------------------")
          print("3.--------------------------Search Suppliers-------------------------")
          print("4.------------------------------Update-------------------------------")
          print("5.-----------------------------Main Menu-----------------------------")
          ch=int(input("Enter your choice: "))
          if(ch==1):
               suppliers.insert()
               ShowMenuOptions("suppliers")
          elif(ch==2):
               suppliers.delete()
               ShowMenuOptions("suppliers")
          elif(ch==3):
               suppliers.search()
               ShowMenuOptions("suppliers")
          elif(ch==4):
               suppliers.update()
               ShowMenuOptions("suppliers")
          elif(ch==5):
               ShowMenuOptions("MainMenu")
          
     elif(choice=="items"):
          print("1-----------------------------Insert items---------------------------")
          print("2.----------------------------Delete items---------------------------")
          print("3.----------------------------Update items---------------------------")
          print("4.----------------------------Search items---------------------------")
          print("5.------------------------------Main Menu----------------------------")
          
          ch=int(input("Enter your choice: "))
          if(ch==1):
               items.insert()
               ShowMenuOptions("items")
          elif(ch==2):
               items.delete()
               ShowMenuOptions("items")
          elif(ch==3):
               items.update()
               ShowMenuOptions("items")
                    
          elif(ch==4):
               items.Search()
               ShowMenuOptions("items")
          elif(ch==5):
               ShowMenuOptions("MainMenu")
     elif(choice=="purchase"):
          print("1-----------------------------Insert Purchase---------------------------")
          print("2.----------------------------Delete Purchase---------------------------")
          print("3.---------------------------Show all Purchase--------------------------")
          print("4.-------------------------------Main Menu------------------------------")
          
          ch=int(input("Enter your choice: "))
          if(ch==1):
               purchase.insert()
               ShowMenuOptions("purchase")
          elif(ch==2):
               purchase.delete()
               ShowMenuOptions("purchase")
          elif(ch==3):
               purchase.GetAll()
               ShowMenuOptions("purchase")
          elif(ch==4):
               ShowMenuOptions("MainMenu")
     elif(choice=="purchase_details"):
          print("1-----------------------------Insert Purchase_details---------------------------")
          print("2.----------------------------Delete Purchase_details---------------------------")
          print("3.---------------------------Show all Purchase_details--------------------------")
          print("4.----------------------------------Main Menu-----------------------------------")
          
          ch=int(input("Enter your choice: "))
          if(ch==1):
               purchase_details.insert()
               ShowMenuOptions("purchase_details")
          elif(ch==2):
               purchase_details.delete()
               ShowMenuOptions("purchase_details")
          elif(ch==3):
               purchase_details.GetAll()
               ShowMenuOptions("purchase_details")
          elif(ch==4):
               ShowMenuOptions("MainMenu")
     elif(choice=="bills"):
          print("1-----------------------------Insert bills---------------------------")
          print("2.----------------------------Delete bills---------------------------")
          print("3.---------------------------Show all bills--------------------------")
          print("4.-----------------------------Main Menu-----------------------------")
          
          ch=int(input("Enter your choice: "))
          if(ch==1):
               bills.insert()
               ShowMenuOptions("bills")
          elif(ch==2):
               bills.delete()
               ShowMenuOptions("bills")
          elif(ch==3):
               bills.BillSearch()
               ShowMenuOptions("bills")
          elif(ch==4):
               ShowMenuOptions("MainMenu")
     elif(choice=="bill_details"):
          print("1-----------------------------Insert bill_details---------------------------")
          print("2.----------------------------Delete bill_details---------------------------")
          print("3.-------------------------------Search Bills-------------------------------")
          print("4.---------------------------------Main Menu--------------------------------")
          
          ch=int(input("Enter your choice: "))
          if(ch==1):
               bill_details.insert()
               ShowMenuOptions("bill_details")
          elif(ch==2):
               bill_details.delete()
               ShowMenuOptions("bill_details")
          elif(ch==3):
               bill_details.GetAll()
               ShowMenuOptions("bill_details")
          elif(ch==4):
               ShowMenuOptions("MainMenu")
     elif(choice=="report"):
          bill_details.Bill_Report_By_Item()     
          ShowMenuOptions("MainMenu")
          

