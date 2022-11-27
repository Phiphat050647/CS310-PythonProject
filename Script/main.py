def showmenu() : #Display Interface Menu (Funtction)
  print("="*50)
  print("%-13s %s %12s %8s %4s"% ("|","Main Menu","|","Code","|"))
  print("="*50)
  print("%-13s %s %13s %8s %4s"% ("|","Shopping","|","-S01-","|"))
  print("%-12s %s %11s %8s %4s"% ("|","Check Stock","|","-C01-","|"))
  print("%-12s %s %12s %8s %4s"% ("|","All orders","|","-A01-","|"))
  print("%-15s %s %15s %7s %5s"% ("|","Exit","|","-E-","|"))
  print("="*50)

  
def inputmenu() : # Enter word hook showmenu

    menu_check = True # check menu list
    while menu_check : # if true is work loop whiles

        menu = input(str("showmenu : ")).upper()

        if menu == "S" :
            shopping()
            menu_check = False
        elif menu == "C" : #Check Stock
            showmenu()
            menu_check = False
        elif menu == "A" :
            print("Work : inputmenu go to All orders")
            menu_check = False
        elif menu == "E" : #Exit
            print("Work : inputmenu go to Exit")
            menu_check = False



# # #First Function  runtime # # #
               
def shopping() : 
    with open(r"Datapacks\datalist.txt") as file:
        resource = file.read().splitlines()
    
    print("-"*55)
    print("%-2s %s %-15s %-19s %-2s %s %2s"% ("|","Code","|","Food Menu","|","Price","|"))
    print("-"*55)

    for i in range(len(resource)) : # ดึงเอา txt resource splitlines() 
        
        resource_conlist = resource[i] # แปลง text เป็น List 
        resource_conlist = list(resource_conlist.split(",")) # แปลง text เป็น List 

        print("%-3s %-3s %-7s %-27s %-3s %-4s %2s"% ("|",resource_conlist[0],"|",resource_conlist[1],"|",resource_conlist[2],"|"))
        print("-"*55)
    
    order()
    
def order() : #ฟังชันก์สั่งออเดอร์ พร้อมบอกจำนวน
    with open(r"Datapacks\datalist.txt") as file:
        resource = file.read().splitlines()
        
    oder_check = True 
    while oder_check :
        
        oder = int(input("Please enter your order : "))
        amt = int(input("Please enter the required quantity : "))
        
    for i in range(len(resource)) : # ดึงเอา txt resource splitlines() 
        
        resource_conlist = resource[i] # แปลง text เป็น List 
        resource_conlist = list(resource_conlist.split(",")) # แปลง text เป็น List 
        
        if oder == resource_conlist[0] :
            total = resource_conlist[3] - amt
            resource
            #inplace_change("Datapacks\datalist.txt", resource_conlist[3] , total) เขียนแทนทีไฟล์
            #เดี๋ยวมาเขียนต่อ
            

def stock_change(filename, old_int, new_int):
    with open(filename) as f:
        s = f.read()
        if old_int not in s:
            
        
           
            
        


        
#def stock() :





############################################################
showmenu() # First Run times! 1
inputmenu() # First Run times!  2