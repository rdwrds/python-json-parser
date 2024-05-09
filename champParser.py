import os, json

path = "C:/Users/scrub/OneDrive/Desktop/projects/lolnotes/src/assets/ChampJsons"
path = os.path.realpath(path)
os.chdir(path)

champs = {}
abilities = {}
binds = ['Q','W','E','R']
index = 0
for root, dirs, files in os.walk(path):
    for file in files:
        opened = open(file, encoding="utf8")
        #returns data as dictionary
        data = json.load(opened)
        name = opened.name.removesuffix(".json")

        print("opened: ", file)
        spells = data["data"][name]["spells"]
        
        for item in spells:
            abilities.update({binds[index]: item["image"]["full"]})
            index = index + 1

        champs.update({name : abilities})
        champs[name].update({"id": data["data"][name]["key"]})
        champs[name].update({"icon": data["data"][name]["image"]["full"]})

        abilities = {}
        index = 0

print(champs)