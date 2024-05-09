import os, json

file = "C:/Users/scrub/OneDrive/Desktop/projects/lolnotes/src/assets/Runes/runesReforged.json"
file = os.path.realpath(file)

runeTrees = {}

index = 0

opened = open(file, encoding="utf8")
#returns data as dictionary
data = json.load(opened)

for rune in data:
    print(rune["name"])
    
    temp = {
        "id" : rune["id"],
        "name" : rune["name"],
        "icon" : rune["icon"],
        "keystones" : {},
        "perks" : {},
    }
    runeTrees.update({rune["name"]: temp})
    temp = {}
    for slot in rune['slots']:
        for thing in slot["runes"]:
            #print(thing["key"])

            temp = {
                "id" : thing["id"],
                "key" : thing["key"],
                "icon" : thing["icon"],
            }
            
            if(index == 0):
                #1st rune slot are keystones
                runeTrees[rune["name"]]["keystones"].update({thing["name"] : temp})
            else:
                runeTrees[rune["name"]]["perks"].update({thing["name"] : temp})
            temp={}

        index = index + 1 
    index = 0


total = open("finishedrunes.json","w")
total.write(json.dumps(runeTrees))
print("wrote to " , total)
    