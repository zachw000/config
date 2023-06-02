import json
EFLG = 0
def readMods():
    # Opening JSON file
    f = open('EntityMods.json',)
    modlist = []
    
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    
    # Iterating through the json
    # list
    for i in data['entityMods']:
        # print u'\u2713' Prints check mark 'approval'
        #print(str(i['modName']) + "\nEnabled?  " + str(i['enabled']) + '\t\t\t' + u'\u2713')
        modlist.append(i)
  
    # Closing file
    f.close()
    return modlist
def commandLoop():
    # Error flag, by default will assume error
    EFLG = 0xFFFF
    if EFLG != 0:
        return False
    else:
        return True
if __name__ == '__main__':
    # Initializes modlist in read mode
    mods = readMods()
    if not commandLoop():
        print("An error has occured.\n")
    else:
        print("Exiting...\n")