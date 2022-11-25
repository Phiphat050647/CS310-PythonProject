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
    while menu_check : # if true is work loop while

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
    with open(r"C:\Users\NATE\Desktop\CS310-PythonProject\Datapacks\datalist.txt") as file:
        resource = file.read().splitlines()
    
    print("-"*50)
    print("%-2s %s %-10s %-19s %-2s %s %2s"% ("|","Code","|","Food Menu","|","Price","|"))

    '''for i in range(len(resource)) :
        resource_context = resource[i]
        print(resource_context.replace(' ',' '*20))
        #print(resource[i])
        print("-"*50)'''

    for i in range(len(resource)) : # ดึงเอา txt resource splitlines() 
        #print(resource[i]) #debug log to text
        
        resource_conlist = resource[i] # แปลง text เป็น List 
        resource_conlist = list(resource_conlist.split(" ")) # แปลง text เป็น List 

        print("%-2s %s %-10s %-19s %-2s %s %2s"% ("",resource_conlist[0],"",resource_conlist[1],"",resource_conlist[2],""))

        #print(resource[i])
        #print("%-2s %s %-10s %-19s %-2s %s %2s"% ("|","Code","|","Food Menu","|","Price","|"))
        print("-"*50)



#def order() :
        
#def stock() :





############################################################
showmenu() # First Run times! 1
inputmenu() # First Run times!  2