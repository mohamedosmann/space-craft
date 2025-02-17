import time
import json 

crew_file = "crewdata.json"

def load_crew():
    global crew
    try:
        with open(crew_file, "r") as f:
            crew = json.load(f)
    except(FileNotFoundError, json.JSONDecodeError):
        crew = []

def save_crew():
    with open(crew_file, "w") as f:
        json.dump(crew, f)

fuel = 1000
load_crew()

def checkstatus():
    print(f"\n Fuel {fuel} KG| crew : {len(crew)}")
    print(f"Crew members" ,",".join(crew) if crew else "none")

def addcrew():
    name = input("enter member name to add :")
    if not name:
        print("Error cannot be empty")
        return
    if name in crew:
        print(f"Error {name} is already in crew ")
    else:
        crew.append(name)
        save_crew()
        print(f"{name} has been added to the crew ")

def removecrew():
    name = input("remove crew Enter their name :")
    if name in crew:
        crew.remove(name)
        save_crew()
        print(f"{name} has been removed ")
    else:
        print(f"error {name} is not in the crew ")

def countdown():
    for i in range(10, 0, -1):
        print(f"{i}......")
        time.sleep(1)
        print("🚀 Liftoff! The rocket has launched!\n")
def launch():
    global fuel 
    if len(crew) ==0:
        print("\n🚨 Launch aborted! No crew members onboard.")
        return
    
    if fuel<=0:
        print("\n🚨 Launch failed! Not enough fuel.")
        return
    
    countdown()

print("\n🚀 Launch initiated! Burning fuel...")
while fuel >0:
    time.sleep(5)
    fuel -= 100
    print(f"🔥 Fuel remaining: {fuel} kg")
    if fuel <=0:
        print("Out of fuel Mission complete")
        break
while True:
    print("\n1. Check Launch Status\n2. Add Crew\n3. Remove Crew\n4. Start Launch\n5. Exit")
    choice = input("Choose an option: ")

    try:
        choice = int(choice)
        if choice ==1:
            checkstatus()
        elif choice == 2:
            addcrew()
        elif choice == 3:
            removecrew()
        elif choice ==4:
            launch()
        elif choice == 5:
            print("Exiting Mission control dashboard.........")
            break
        else:
            print("❌ Invalid option. Please choose a number between 1 and 5.")
    except ValueError:
        print("Please enter valid number ")
