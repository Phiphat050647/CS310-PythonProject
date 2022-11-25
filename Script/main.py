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
            print("Work : inputmenu go to Main Menu ")
            menu_check = False
        elif menu == "C" :
            print("Work : inputmenu go to Check Stock")
            menu_check = False
        elif menu == "A" :
            print("Work : inputmenu go to All orders")
            menu_check = False
        elif menu == "E" :
            print("Work : inputmenu go to Exit")
            menu_check = False


# # #First Function  runtime # # #

          
            
showmenu()
inputmenu()