#importing datetime module for recording the time of borrow and return
import datetime
#importing os for the removal of borrower file after successful return
import os


#def display() displays all the detail of the books present in the library.

def display():
    file1= open("LibraryBooks.txt","r")
    print("\n \t\t|| Detail of Books available in our store ||")
    print("_______________________________________________________________________________")
    print ("\nBOOK NAME\t\tAUTHOR NAME\t\tQUANTITY\tPRICE")

    #reading lines from file1
    lines=file1.readlines()

    #stripping new lines with strip
    lines=[x.strip('\n') for x in lines]
    for i in range(len(lines)):
        print ("\n-------------------------------------------------------------------------------")
        for a in lines[i].split(','):
            print(a,end="\t\t")
    print("\n_______________________________________________________________________________")

"""def borrow() initialises the borrow process; creates new text file with
    borrower’s name and holds onto all the details relating to the borrower.
    After the successful borrow of books, the stock file is updated."""

def borrow():
    while True:
        Name= input("\nEnter your Name: ")

        #validating name 
        if Name.isalpha():
            break
        else:
            print("Please input alphabet from: A-Z")
            
    #Creation of new file at each borrow with borrower's name
    Name=Name.upper()
    file_name= "Borrower-"+Name+".txt"
    with open(file_name,"w+")as file2:

        #Accessing date and time
        Date= datetime.datetime.now()

        #For return date
        date= datetime.datetime.now
        new_date= date().date()
        new= datetime.timedelta(10)
        return_date= new_date+new
        
        #Writing Borrower Name and Date-Time of issue to the file
        file2.write("Borrowed By: "+Name+"\n\n Date and Time of Issue: "+str(Date)+"\n Last Date of Return: "+ str(return_date)+"\n")
        
        print("\n----- Books available in our store -----\n")

        #Initialising empty lists for appending book name and cost from the file into a list
        #initialising total with float datatype to store the total cost of books
        total=0.0
        cost=[]
        bookname=[]
        with open("LibraryBooks.txt","r") as file1:
            lines=file1.readlines()
            lines=[x.strip('\n') for x in lines]
            for i in range(len(lines)):
                ind=0
                for a in lines[i].split(','):
                    if (ind==0):
                        bookname.append(a)
                    if(ind==3):
                        cost.append(a.strip("$"))
                         #Strips "$" sign and only appends the number to the list
                    ind+=1

            #PRINTS NAMES OF THE AVAILABLE BOOKS
            for i in bookname:
                print("\t"+i)
    
        while True:
            try:
                Book_quantity= int(input("\n Enter number of books you want to borrow: "))

                #Checking if correct value has been entered
                if Book_quantity>0:
                    break
                else:
                    print(" Please input positive integer")
            except:
                print(" Please input correctly")
        bname = []
        count = 0
        #loop runs as many times as the number specified in Book_quantity        
        for i in range(Book_quantity):
            ct = 0
            Book_Name= input("\n Enter name of the book you would like to borrow: ")
            for b in bname:
                if (b == Book_Name):
                    print(" You can't borrow same book twice.")
                    ct = 1
                    break
            if(ct == 0):
                #Accessing the file's content as elements of a list
                file1= open("LibraryBooks.txt","r")
                li=[(line.strip()).split(",") for line in file1]
                #For stock update
                for i in range(len(li)):
                    if Book_Name not in bookname:
                        print(" The Book "+Book_Name+" is not available in our library. Please type in properly")
                        ct = 1
                        break
                    if Book_Name==li[i][0]:
                        if int(li[i][2])==0:
                            print("\n '"+Book_Name+"' is not available at the moment.\nPlease place an order for some other book :)")
                            ct = 1
                            break
                    if(ct == 0):
                        bname.append(Book_Name)
                        if Book_Name==li[i][0]:
                            if int(li[i][2])>0:
                                #typecasting string values of file into int
                                li[i][2]= int(li[i][2])
                                li[i][2]=(li[i][2])-1

                       #Writing the Stock-file with updated value of books     
                        with open("LibraryBooks.txt","w")as file1:
                            file1.write(str(li[0][0])+","+ str(li[0][1])+","+str(li[0][2])+","+str(li[0][3]+"\n"))
                            file1.write(str(li[1][0])+","+ str(li[1][1])+","+str(li[1][2])+","+str(li[1][3]+"\n"))
                            file1.write(str(li[2][0])+","+ str(li[2][1])+","+str(li[2][2])+","+str(li[2][3]+"\n"))
                            file1.write(str(li[3][0])+","+ str(li[3][1])+","+str(li[3][2])+","+str(li[3][3]+"\n"))
                            file1.write(str(li[4][0])+","+ str(li[4][1])+","+str(li[4][2])+","+str(li[4][3]+"\n"))
                            file1.write(str(li[5][0])+","+ str(li[5][1])+","+str(li[5][2])+","+str(li[5][3]+"\n"))
                            file1.write(str(li[6][0])+","+ str(li[6][1])+","+str(li[6][2])+","+str(li[6][3]+"\n"))
                            file1.write(str(li[7][0])+","+ str(li[7][1])+","+str(li[7][2])+","+str(li[7][3]+"\n"))
                            file1.write(str(li[8][0])+","+ str(li[8][1])+","+str(li[8][2])+","+str(li[8][3]+"\n"))
                            file1.write(str(li[9][0])+","+ str(li[9][1])+","+str(li[9][2])+","+str(li[9][3]+"\n"))

                
                #For calculating cost
                if(ct == 0):
                    #Writing to the Borrower's file the Borrowed Book'Name
                    file2.write("\n Name of the Book: "+Book_Name)
                    for i in range(len(cost)):
                        if Book_Name==bookname[i]:
                            total+= float(cost[i])
                    if(total != 0 and count == (Book_quantity-1)):
                        print("\n Your total is $",total)
                        #Writing the cost of the book to the file
                        file2.write("\n Your total is: $"+str(total)+"\n")
            count += 1
        print("\n ----- Thankyou for borrowing from us ! -----")

#def display_borrow() asks for the name of the borrower and displays their borrowing details.
    
def display_borrow():
    
    #Checking the file of Borrower
    Name= input("Enter your Name: ")
    Name=Name.upper()
    file_name= "Borrower-"+Name+".txt"
    try:
        with open(file_name,"r")as file2:
            lines=file2.read()
            print("\n"+lines)
    except:
        print("The borrower's name is incorrect")
        display_borrow()

"""def returns() initialises the return process; creates new text file with
    returner’s name and holds onto all the details relating to the returner.
    After the successful return of books, the stock file is updated and
    the file with borrower’s detail is removed """        

def returns():
            
    #Checking the file of Borrower
    Name= input("Enter your Name: ")
    Name=Name.upper()
    file_name= "Borrower-"+Name+".txt"
    try:
        with open(file_name,"r")as file2:
            lines=file2.read()
            print("\n"+lines)
    except:
        print("The borrower's name is incorrect")
        returns()

    try:

        #Creating new file with Returner's name
        file="Returner-"+Name+".txt"
        with open(file,"w+")as file3:
                #Accessing date and time
                Date= str(datetime.datetime.now())
                #Writing Borrower Name and Date-Time of issue to the file
                file3.write("Borrowed By: "+Name+"\nDate and Time of Return: "+Date+"\n")

                #initialising total and totalcost with float datatype to store the total cost of books
                total=0.0
                totalcost=0.0
                while True:
                    Book_quantity= int(input("Enter number of books you want to return: "))
                    #Checking if correct value has been entered
                    if Book_quantity>0:
                        break
                    else:
                        print(" Please input positive integer")

                #loop runs as many times as the number specified in Book_quantity  
                for i in range(Book_quantity):
                    Book_Name= input("\nEnter name of the book you would like to return: ")

                    #Accessing the file's content as elements of a list
                    file1= open("LibraryBooks.txt","r")
                    li=[(line.strip()).split(",") for line in file1]

                    #For stock update
                    for i in range(len(li)):
                        if Book_Name.upper()==li[i][0].upper():
                            #typecasting string values of file into int
                            li[i][2]= int(li[i][2])
                            li[i][2]=(li[i][2])+1

                        #Writing the Stock-file with updated value of books     
                        with open("LibraryBooks.txt","w")as file1:
                            file1.write(str(li[0][0])+","+ str(li[0][1])+","+str(li[0][2])+","+str(li[0][3]+"\n"))
                            file1.write(str(li[1][0])+","+ str(li[1][1])+","+str(li[1][2])+","+str(li[1][3]+"\n"))
                            file1.write(str(li[2][0])+","+ str(li[2][1])+","+str(li[2][2])+","+str(li[2][3]+"\n"))
                            file1.write(str(li[3][0])+","+ str(li[3][1])+","+str(li[3][2])+","+str(li[3][3]+"\n"))
                            file1.write(str(li[4][0])+","+ str(li[4][1])+","+str(li[4][2])+","+str(li[4][3]+"\n"))
                            file1.write(str(li[5][0])+","+ str(li[5][1])+","+str(li[5][2])+","+str(li[5][3]+"\n"))
                            file1.write(str(li[6][0])+","+ str(li[6][1])+","+str(li[6][2])+","+str(li[6][3]+"\n"))
                            file1.write(str(li[7][0])+","+ str(li[7][1])+","+str(li[7][2])+","+str(li[7][3]+"\n"))
                            file1.write(str(li[8][0])+","+ str(li[8][1])+","+str(li[8][2])+","+str(li[8][3]+"\n"))
                            file1.write(str(li[9][0])+","+ str(li[9][1])+","+str(li[9][2])+","+str(li[9][3]+"\n"))

                    #Writing to the Returner's file
                    file3.write("\nName of the Book: "+Book_Name+"\n")

                    #Initialising empty list for appending book name and cost from the file into a list
                    cost=[]
                    bookname=[]
                    with open("LibraryBooks.txt","r") as file1:
                        lines=file1.readlines()
                        lines=[x.strip('\n') for x in lines]
                        for i in range(len(lines)):
                            ind=0
                            for a in lines[i].split(','):
                                if (ind==0):
                                    bookname.append(a)
                                if(ind==3):
                                    cost.append(a.strip("$"))
                                    #Strips "$" sign and only appends the number to the list
                                ind+=1
                                
                        #For calculating cost       
                        for i in range(len(cost)):
                            if Book_Name.upper()==bookname[i].upper():
                                total+= float(cost[i])
                    print(" Your total cost is: $",total)
                

                #For removal of borrow record after successful return
                file2.close()
                os.remove("Borrower-"+Name+".txt")
                print(" Borrower Record removed")

                #For calculating fine
                print("\nIs the book return date expired?")
                print("Press Y for Yes and N for No")
                expired=input()
                if(expired.upper()=="Y"):
                    print("By how many days was the book returned late?")
                    day=int(input())
                    #Initialising fine with $0.5 per day
                    fine= 0.5*day
                    print("\n Your fine is: $",fine)
                    #Adding fine to the total
                    totalcost= float(total+fine)
                    print(" Your total amount due is: $",totalcost)

                    #Writing the fine and total amount to the file
                    file3.write("\nFine is: $"+str(fine)+"\n")
                    file3.write(" Your total amount due is: $"+ str(totalcost)+"\n")
                    
                else:
                    print("\nYour total amount due is: $",total)
                    file3.write("\nYour total amount due is: $"+ str(total)+"\n")
                print("\n ----- Thankyou for returning the book ----- \n ---------- Do visit us again ! ---------")
                return
    except:
        print("Please input correct values")
