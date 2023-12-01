import csv
import hashlib
import getpass#Importing useful functions... 


def h_p(passwd):#Function to hash the password
    h_pass = hashlib.sha256(passwd.encode()).hexdigest()#Uses hashlib to hash the password using sha256 encryption
    return h_pass

def register():#Function for registering and writing to the csv file
    print("~~~~~~ User Registration ~~~~~~")
    username = input("Enter your username: ")#Takes the username inputted from the user
    passwd=getpass.getpass("Enter your password: ")#Uses getpass to get password securely without displaying it on the screen.
    h_pass = h_p(passwd)#Gets input from the h_p function written above 


    with open("userdata.csv","a",newline="") as fo:#Opens a csv file in append mode
        write=csv.writer(fo)#Function in csv to write inputs and all...
        write.writerow([username,h_pass])
    
    print("Registration successfull!!\n")


def login():#Function to login using username and password... Returns false if credentials are wrong.
    print("~~~~~~ User Login ~~~~~~")
    username = input("Enter your username: ")
    passwd = getpass.getpass("Enter your password: ")
    h_pass=h_p(passwd)


    with open("userdata.csv","r") as fr:#Opens the same csv file in read mode.
        
        userdata=csv.reader(fr)
        for i in userdata:#i gets the values saved in the csv file as a list one by one.
            if i[0]==username and i[1]==h_pass:#Checks if username and password are correct as loop iterates.
                print("Login successfull!!\n")
                return
    print("Login failed... Invalid username or password!!\n")#Only prints if the loop returns false

while True:#Loop is iterated until a break statement or false statement is reached.
    print("1) Register\n2)Login\n3)Exit\n")
    ask=input("Enter your choice (1/2/3): ")#Takes input from the user

    if ask=="1":#checks if the user inputted 1
        register()
    elif ask=="2":#checks if the user inputted 2
        login()
    elif ask=="3":#checks if the user inputted 3
        print("Program exited!!")
        break#Breaks out of the loop.
    else:#if none of the above statements return true then this statement is executed.
        print("Invalid choice. Please enter 1 , 2 or 3.\n")
