import time
import json

# File to store crew data
CREW_FILE = "crew_data.json"

# Load crew from file (if exists)
def load_crew():
    """Load crew list from a file."""
    global crew
    try:
        with open(CREW_FILE, "r") as f:
            crew = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        crew = []  # Default to an empty crew list

# Save crew to file
def save_crew():
    """Save crew list to a file."""
    with open(CREW_FILE, "w") as f:
        json.dump(crew, f)

# Initialize crew and fuel
fuel = 1000
load_crew()  # Load crew when the program starts

# Function to check launch status
def launch_check():
    print(f"\n🚀 Fuel: {fuel} kg | 👩‍🚀 Crew: {len(crew)} members")
    print("👨‍🚀 Crew members:", ", ".join(crew) if crew else "None")

# Function to add a crew member
def add_crew():
    name = input("Enter crew member name to add: ").strip()
    
    if not name:
        print("❌ Error: Crew member name cannot be empty!")
        return

    if name in crew:
        print(f"❌ Error: {name} is already in the crew!")
    else:
        crew.append(name)
        save_crew()  # Save after modification
        print(f"✅ {name} has been added to the crew.")

# Function to remove a crew member
def remove_crew():
    name = input("Enter crew member name to remove: ").strip()
    
    if not name:
        print("❌ Error: Crew member name cannot be empty!")
        return

    if name in crew:
        crew.remove(name)
        save_crew()  # Save after modification
        print(f"✅ {name} has been removed from the crew.")
    else:
        print(f"❌ Error: {name} is not part of the crew!")

# Function to simulate countdown and launch
def countdown():
    """Perform a countdown before launch."""
    print("\n🕒 Initiating countdown...")
    for i in range(10, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    print("🚀 Liftoff! The rocket has launched!\n")

# Function to simulate launch and fuel burn
def launch():
    global fuel
    if len(crew) == 0:
        print("\n🚨 Launch aborted! No crew members onboard.")
        return

    if fuel <= 0:
        print("\n🚨 Launch failed! Not enough fuel.")
        return

    countdown()  # Start countdown before launch

    print("\n🚀 Launch initiated! Burning fuel...")
    while fuel > 0:
        time.sleep(5)  # Wait 5 seconds
        fuel -= 100  # Reduce fuel by 100 kg
        print(f"🔥 Fuel remaining: {fuel} kg")

        if fuel <= 0:
            print("\n🛑 Out of fuel! Mission complete.")
            break

# Main menu loop
while True:
    print("\n1. Check Launch Status\n2. Add Crew\n3. Remove Crew\n4. Start Launch\n5. Exit")
    choice = input("Choose an option: ")

    try:
        choice = int(choice)
        if choice == 1:
            launch_check()
        elif choice == 2:
            add_crew()
        elif choice == 3:
            remove_crew()
        elif choice == 4:
            launch()
        elif choice == 5:
            print("Exiting Mission Control Dashboard. 🛑")
            break
        else:
            print("❌ Invalid option. Please choose a number between 1 and 5.")
    except ValueError:
        print("❌ Error: Please enter a valid number.")
