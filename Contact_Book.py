import os
contacts={}
filename="contacts.txt"
def load_contacts():
    if os.path.exists(filename):
        with open(filename,"r") as file:
            for line in file:
                parts=line.strip().split(",")
                if len(parts)==4:
                    name,phone,email,address=parts
                    add_contact(name,phone,email,address,loaded=True)
def save_contacts():
    with open(filename,"w") as file:
        for name,details in contacts.items():
            file.write(f"{name},{details['Phone']},{details['Email']},{details['Address']}\n")
  
def add_contact(name,phone,email,address,loaded=False):
    if name in contacts.keys():
        print("Contact with same name already present!\n")
    else:
        contacts[name]={'Phone':phone,
                        'Email':email,
                        'Address':address
                        }
        if (not loaded):
            print("Contact Added Successfully!")
def display_contacts():
    if not contacts:
        print("No Contact Found")
    else:
        print("\n------------Contact List------------")
        for name,details in contacts.items():
            print(f"Name:{name}")
            print(f"Phone Number:{details['Phone']}")
            print(f"Email ID:{details['Email']}")
            print(f"Address:{details['Address']}") 
            print("------------------------") 
def search_contact(searchname=None,searchphone=None):
    found =False
    if searchphone:
        for name ,details in contacts.items():
            if str(details["Phone"]).lower()==searchphone:
                print(f"Name: {name}") 
                print(f"Phone Number : {details["Phone"]}") 
                print(f"Email ID : {details["Email"]}") 
                print(f"Address : {details["Address"]}")
                found=True
                break
    if not found and searchname:
        for name ,details in contacts.items():
            if(name.lower()==searchname.lower()):
                print(f"Name: {name}") 
                print(f"Phone Number : {details["Phone"]}") 
                print(f"Email ID : {details["Email"]}") 
                print(f"Address : {details["Address"]}")
                found=True
                break
    if not found:
            print("Contact Not Found")
def update(name):
    if name in contacts:
        print(f"Updating contact for {name}")
        phone=input("Enter Phone number to update(leave blank for to keep same): ")
        email=input("Enter Email ID to update(leave blank for to keep same): ")
        address=input("Enter Address to update(leave blank for to keep same): ")
        
        if phone:
            contacts[name]['Phone']=phone
        if email:
            contacts[name]['Email']=email
        if address:
            contacts[name]['Address']=address
        print("Contact Updated Successfully")
    else:
        print("Contact Not Found!")
def delete(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully")     
    else:
        print("Contact Not found!")
def menu():
    print("-----------------------------------")
    print("1. Add Contact")        
    print("2. View Contact List")        
    print("3. Search Contact")        
    print("4. Update Contact")        
    print("5. Delete Contact")  
    print("6. Exit")  
          
def main():
    load_contacts()
    while(True):
        menu()
        choice=input("Choose an operation: ")
        if(choice=="1"):
            name=input("Enter Name: ")
            phone=input("Enter Phone Number: ")
            email=input("Enter Email ID: ")
            address=input("Enter Address: ")
            add_contact(name=name,phone=phone,address=address,email=email)
        elif(choice=="2"):
            display_contacts()
        elif(choice=="3"):
            searchind=print("Enter Name or Phone Number to search: ")
            search_contact(searchname=searchind,searchphone=searchind)
        elif(choice=="4"):
            name=input("Enter name of Contact to be updated: ")
            update(name=name)
        elif(choice=="5"):
            name=input("Enter name of Contact to be deleted: ")
            delete(name=name)
        elif (choice=="6"):
            save_contacts()
            break
        
        else:
            print("Enter a Correct Opeartion")

main()