import json 
import time

# File to store crew data
crew_file = "xogta_rikaabka.json"


# Load crew from file (if exists)
def loadcrew():
    global crew
    try:
        with open(crew_file, "r")as f:
            crew = json.load(f)
    except(FileNotFoundError, json.JSONDecodeError):
        crew = []
    

# Save crew to file
def savecrew():
    with open(crew_file, "w") as f:
        json.dump(crew, f)
        
# Initialize crew and fuel

fuel = 1000
loadcrew()
# Function to check launch status
# Function to add a crew member
# Function to remove a crew member
# Function to simulate countdown and launch
# Function to simulate launch and fuel burn
# Main menu loop
