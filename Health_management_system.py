# Health Management System
# 3 clients = Harry, rohan and Hammad
# def getdate():
#     import datetimereturn datetime.datetime.now()
# Total 6 files
# Write a function thatwhen executed takes as input client name
# one functon to retrive exersise or food for any client



client = input("Enter the client name \n")
print("Choose whether you want to log the file  or retrive the file")
opt1 = input("Enter 'l' to log the file or 'r' to retrive the file \n")
print("Choose from the following which file you want to open , food or Exersise")
opt2 = input("Enter 'f' for food log or 'e'for exersise log \n")
#choice = input("What do you want to ")



def getdate():
    import datetime
    return datetime.datetime.now()



def Food_log():
    if client == "Harry":
        f = open("Harry_food_log.txt","a")
        f.write(input("Enter the Meal"+"\n"))
        f.write("\n")
        f.close()

    if client == "Rohan":
        f = open("Rohan_food_log.txt","a")
        f.write(input("Enter the Meal\n"))
        f.write("\n")
        f.close()

    if client == "Hammad":
        f = open("Hammad_food_log.txt","a")
        f.write(input("Enter the Meal\n"))
        f.write("\n")
        f.close()

def Exersise_log():
    if client == "Harry":
        f = open("Harry_Exersise_log.txt", "a")
        f.write(input("Enter the Exersise\n"))
        f.write("\n")
        f.close()

    if client == "Rohan":
        f = open("Rohan_Exersise_log.txt", "a")
        f.write(input("Enter the Exersise\n"))
        f.write("\n")
        f.close()

    if client == "Hammad":
        f = open("Hammad_Exersise_log.txt", "a")
        f.write(input("Enter the exersise\n"))
        f.write("\n")
        f.close()

def Food_log_retrive():
    if client == "Harry":
        f = open("Harry_log.txt")
        print(getdate())
        for line in f:
            print(line, end="")
        f.close()

    if client == "Rohan":
        f = open("Rohan_food_log.txt")
        print(getdate())
        for line in f:
            print(line, end="")
        f.close()

    if client == "Hammad":
        f = open("Hammad_food_log.txt")
        print(getdate())
        for line in f:
            print(line, end="")
        f.close()

def Exersise_log_retrive():
    if client == "Harry":
        f = open("Harry_Exersise_log.txt")
        print(getdate())
        for line in f:
            print(line, end="")
        f.close()

    if client == "Rohan":
        f = open("Rohan_Exersise_log.txt")
        print(getdate())
        for line in f:
            print(line, end="")
        f.close()

    if client == "Hammad":
        f = open("Hammad_Exersise_log.txt")
        print(getdate())
        for line in f:
            print(line, end="")
        f.close()

def start_programme():
    if opt1 == 'l':     # log the information in file
        if opt2 == 'f':      # food log
            Food_log()
        elif opt2 == 'e':            # Exersise log
            Exersise_log()
        else:
            print("Enter the valid input")
    elif opt1 == 'r':        # Retrives the information in file
        if opt2 == 'f':         # retrives food log
            Food_log_retrive()
        elif opt2 == 'e':     #retrives exersise log
            Exersise_log_retrive()
        else:
            print("Enter the valid input")

start_programme()

print("Would you like to run the programme again?")
choice = input("Enter 'y' for yes and 'n' for no \n")
if choice == 'y':
    start_programme()
else:
    exit
