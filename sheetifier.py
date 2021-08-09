init = True

while init: 
    file_name = input("Input file name: ") or "message.txt"
    try: 
        f = open(file_name, "r")
        init = False
    except: 
        print("An error has occurred! \nPlease make sure the file exists and the name you entered is correct. ")

running = True
skill_check = True
iterator = 1
fw = open("sheet.csv", "wt")

while running: 
    if skill_check:
        skill = f.readline()
        skill_check = False
        
    line = f.readline()
    if line == "\n":
        skill_check = True
        iterator = 1
    elif line == "": 
        break
    else: 
        line = line.replace("\"", "\"\"")
        temp = line[line.find(" - ") + 3:line.rfind("[")]
        song_name = temp[0:temp.rfind("(") - 1]
        diff_name = line[line.rfind("["):line.rfind("]") + 1]
        temp = line.rfind("[")
        mapper = line[line.rfind("(", 0, temp) + 1:line.rfind(")", 0, temp)]
        
        print(skill[0:len(skill) - 1] + " " + str(iterator) + ",\"" + song_name + " " + diff_name + "\",\"" + mapper + "\"")
        fw.write(skill[0:len(skill) - 1] + " " + str(iterator) + ",\"" + song_name + " " + diff_name + "\",\"" + mapper + "\"\n")
        iterator += 1
        
f.close()
fw.close()

input("Press Enter to continue...")