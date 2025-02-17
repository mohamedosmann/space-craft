import json

crew_list = ["ahmed", "mohamed"]

def save_crew():
    with open("randomname.json", "w") as f:
        json.dump(crew_list, f)

save_crew()