#importing all the functions from the module Functions
import Functions
def Library():
    while True:
        print("\n\nWELCOME TO LIBRARY MANAGEMENT SYSTEM")
        print("\n1. Display Book Record")
        print("2. Borrow Book")
        print("3. Display Borrower Record")
        print("4. Return Book")
        print("5. Exit")
        while True:
            try:
                choice=int(input("\nEnter your choice: "))
                break
            except:
                print("Please input an appropriate value")    
        #Calling the functions from imported module.
        if choice==1:
            Functions.display() 
        elif choice==2:
            Functions.borrow()
        elif choice==3:
            Functions.display_borrow()
        elif choice==4:
            Functions.returns()
        elif choice==5:
            print("Thank you for your presence in our library")
            return
        else:
            print("Please enter a valid choice from 1-5")           
Library()
