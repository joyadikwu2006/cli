import json
import os
import uuid

file_name = "tickets.json"

def create_ticket():
    title = input("Enter ticket title: ").strip()
    if title == "":
        print("Error: title cannot be empty.")
        return

    description = input("Enter ticket description: ").strip()
    if description == "":
        print("Error: description cannot be empty.") 
        return  


    try:
        with open(file_name, "r") as file:
            tickets = json.load(file)
    except FileNotFoundError:
        tickets = []

    tickets.append(ticket)

    try:
        with open(file_name, "w") as file:
            json.dump(tickets, file, indent=4)

        print("Ticket created successfully!")
        print("Ticket ID:", ticket["id"])

    except OSError:
        print("Error: Could not save the ticket.")


def main():
    while True:
        print("\n==Welcome to CLI Ticket Creator.==")
        print("1. create ticket.")
        print("2. Exit")

        choice = input("Enter option: ").strip()

        if choice == "1":
            create_ticket()

        elif choice == "2":
            print("Exiting. Ticket Creator closed.")
            break    

        else:
            print("Invalid choice. choose 1 or 2, try again.")     

if __name__ == "__main__":
    main()  
    
    
    
