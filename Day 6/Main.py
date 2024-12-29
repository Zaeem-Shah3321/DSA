import Sortings as str
from Binary_Search import BinarySearchTree
import Number_Guess 
import Guess_Number
from Number_Guess import Game
import random

contacts = [

    {"Name": "Alice", "Phone": "12345627890", "Email": "alice.smith@gmail.com"},
    {"Name": "Bob", "Phone": "23456728901", "Email": "bob.johnson@gmail.com"},
    {"Name": "Charlie", "Phone": "34567829012", "Email": "charlie.brown@gmail.com"},
    {"Name": "David", "Phone": "45678920123", "Email": "david.wilson@gmail.com"},
    {"Name": "Eve", "Phone": "56718911234", "Email": "eve.davis@gmail.com"},
    {"Name": "Franky", "Phone": "67819012345", "Email": "frank.miller@gmail.com"},
    {"Name": "Grace", "Phone": "78910123456", "Email": "grace.lee@gmail.com"},
    {"Name": "Hank", "Phone": "89041234567", "Email": "hank.taylor@gmail.com"},
    {"Name": "Ivy", "Phone": "90172345678", "Email": "ivy.martinez@gmail.com"},
    {"Name": "Jack", "Phone": "01263456789", "Email": "jack.anderson@gmail.com"}
]

def data():
    flag = False
    flag2 = False
    while True:
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        flag = valid_phone(phone)
        flag2 = valid_email(email)

        if flag and flag2:
            contacts.append({"Name": name, "Phone": phone, "Email": email})
            print ("Added Sucessfully...")
            break
        elif flag and (not(flag2)):
            print("Invalid Email")
        elif (not(flag)) and flag2:
            print("Invalid Phone Number")
        elif (not(flag)) and (not(flag2)):
            print("Invalid Phone Number And Email")

def valid_phone(phone):
    flag = False
    if len(phone) == 11:
        flag = True
    return flag

def valid_email(email):
    if email.endswith("@gmail.com"):
        before = email.split("@")[0]
        if before:
            return True
    return False

def show(): 
    if not contacts:
        print("No contacts to display!")
    else:
        print("All Contacts:")
        for contact in contacts:
            print(f"Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}")

def sorting():
    while True:
        flag1= True
        flag2= True

        print("Chose Sorting Method")
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        print("4. Merge Sort")
        print("5. Quick Sort")
        inp = int(input("Enter Your Choise: "))

        print("Chose Attribute")
        print("1. Name")
        print("2. Phone Number")
        print("3. Email")
        ipt = int(input("Enter Your Choise: "))

        if inp > 5:
            print("Invalid Sorting Number...")
            flag1 = False
        if ipt > 3:
            print("Invalid Attribute Number...")
            flag2 = False

        if flag1 and flag2:
                send(inp, ipt)
                break

def send(s_i , a_i):
    arr = []
    contact_copy = contacts.copy()
    if a_i == 1:
        if s_i == 1:
            arr = str.bubble_sort(contacts,"Name")
        elif s_i == 2:
            arr = str.selection_sort(contacts,"Name")
        elif s_i == 3:
            arr = str.insertion_sort(contacts,"Name")
        elif s_i == 4:
            arr = str.merge_sort(contacts,"Name")
        elif s_i == 5:
            str.quick_sort(contact_copy,0,len(contact_copy) - 1,"Name")
    elif a_i == 2:
        if s_i == 1:
            arr = str.bubble_sort(contacts,"Phone")
        elif s_i == 2:
            arr = str.selection_sort(contacts,"Phone")
        elif s_i == 3:
            arr = str.insertion_sort(contacts,"Phone")
        elif s_i == 4:
            arr = str.merge_sort(contacts,"Phone")
        elif s_i == 5:
            str.quick_sort(contact_copy,0,len(contact_copy) - 1,"Phone")
    elif a_i == 3:
        if s_i == 1:
            arr = str.bubble_sort(contacts,"Email")
        elif s_i == 2:
            arr = str.selection_sort(contacts,"Email")
        elif s_i == 3:
            arr = str.insertion_sort(contacts,"Email")
        elif s_i == 4:
            arr = str.merge_sort(contacts,"Email")
        elif s_i == 5:
            str.quick_sort(contact_copy,0,len(contact_copy) - 1,"Email")
    
    if s_i == 5:
        display_quick(contact_copy)
    else:
        display(arr)

def display(arr):
    for contact in arr:
            print(f"Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}")

def display_quick(contact_copy):
    for contact in contact_copy:
            print(f"Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}")

def search():
    bst = BinarySearchTree()
    for obj in contacts:
        bst.insert(obj["Name"], obj)
        bst.insert(obj["Email"], obj)

    while True:
        ipt = input("Enter Attribute (1 for Name , 2 for Email): ")
        if ipt == "1":
            name = input("Enter Name: ")
            objt = bst.search(name)    
            if objt:
                print(f"Found: Name: {objt['Name']}, Phone: {objt['Phone']}, Email: {objt['Email']}")
            else:
                print(f"No contact found with the name '{name}'.")
            break
        elif ipt == "2":
            mail = input("Enter Email: ")
            objt = bst.search(mail)    
            if objt:
                print(f"Found: Name: {objt['Name']}, Phone: {objt['Phone']}, Email: {objt['Email']}")
            else:
                print(f"No contact found with the Email '{mail}'.")
            break
        else:
            print("Inavlid Option")

def update_contact():
    print("Update Contact")
    search_key = input("Search by (1) Name (2) Phone Number (3) Email: ")
    if search_key == "1":
        key = "Name"
    elif search_key == "2":
        key = "Phone"
    elif search_key == "3":
        key = "Email"
    else:
        print("Invalid option!")
        return

    value = input("Enter " + key + ": ")
    contact = None
    for c in contacts:
        if c[key] == value:
            contact = c
            break
 
    if contact:
        print("Current Contact: Name: " + contact['Name'] + ", Phone: " + contact['Phone'] + ", Email: " + contact['Email'])

        new_name = input("Enter new Name (press Enter to keep current): ")
        if new_name == "":
            new_name = contact['Name']

        new_phone = input("Enter new Phone Number (press Enter to keep current): ")
        if new_phone == "":
            new_phone = contact['Phone']

        new_email = input("Enter new Email (press Enter to keep current): ")
        if new_email == "":
            new_email = contact['Email']

        if valid_phone(new_phone) and valid_email(new_email):
            contact['Name'] = new_name
            contact['Phone'] = new_phone
            contact['Email'] = new_email
            print("Contact updated successfully!")
        else:
            print("Invalid phone number or email. Update failed.")
    else:
        print("No contact found with " + key + " '" + value + "'.")


def delete_contact():
    while True:
        ipt = input("Enter Attribute to Search (1 for Name, 2 for Email, 3 for Phone Number): ")
        if ipt == "1":
            name = input("Enter Name: ")
            for contact in contacts:
                if contact["Name"] == name:
                    contacts.remove(contact)
                    print(f"Contact with Name '{name}' has been deleted.")
                    return
            print(f"No contact found with the Name '{name}'.")
            break
        
        elif ipt == "2":
            email = input("Enter Email: ")
            for contact in contacts:
                if contact["Email"] == email:
                    contacts.remove(contact)
                    print(f"Contact with Email '{email}' has been deleted.")
                    return
            print(f"No contact found with the Email '{email}'.")
            break

        elif ipt == "3":
            phone = input("Enter Phone Number: ")
            for contact in contacts:
                if contact["Phone"] == phone:
                    contacts.remove(contact)
                    print(f"Contact with Phone Number '{phone}' has been deleted.")
                    return
            print(f"No contact found with the Phone Number '{phone}'.")
            break
        
        else:
            print("Invalid Option")


def game():
    print("1. Easy (6 tries)")
    print("2. Hard (4 tries)")
    print("3. Exit")


    while True:

        opt = input("Enter your choice: ")

        if opt == "1":
            print("You chose Easy mode!")
            max_attempts = 6 
            root = Number_Guess.build_tree(1, 100)
            target_number = random.randint(1, 100)    
            Game.number_game(root, target_number, max_attempts)
            break
        
        elif opt == "2":
            print("You chose Hard mode!")
            max_attempts = 4  
            root = Number_Guess.build_tree(1, 100)
            target_number = random.randint(1, 100)    
            Game.number_game(root, target_number, max_attempts)
            break

        elif opt == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

def game2():

    print("1. Play Game")
    print("2. Exit")

    while True:
        op = input("Your Choise: ")

        if op == "1":
            root = Guess_Number.build_tree(1, 100)
            Guess_Number.play_game(root)
            break
        elif op == "2":
            main()
            break
        else:
            print("Invalild Option..")

def options():
    while True:
        print("1. Add Contact")
        print("2. Show All Contacts")
        print("3. Sort Contacts")
        print("4. Search Contact")
        print("5. Update Contact Info")
        print("6. Delete Contact")
        print("7. Exit Application")

        i = input("Your Choise: ")
        if i == "1":
            data()
        elif i == "2":
            show()
        elif i == "3":
            sorting()   
        elif i == "4":
            search() 
        elif i == "5":
            update_contact()
        elif i == "6":
            delete_contact()    
        elif i == "7":
            main();    
        else:
            print("Invalid Option...")

def main():
    print("1. Contact Book Managment")
    print("2. Number Guess Game")
    print("3. Guess Number Game")

    ipt = input("Your Choise: ")
    if ipt == "1":
        options()
    elif ipt == "2":
        game()
    elif ipt == "3":
        game2()
    else:
        print("Invalid Option")

if __name__ == "__main__":
    while True:
        main()