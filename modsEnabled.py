import json
EFLG = 0

def tokenize(command):
    tokens = command.split(' ')

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
def commandLoop(mods):
    # Error flag, by default will assume error
    EFLG = 0b1111111111111111
    cmd = ""
    while cmd != "exit" or cmd != "stop":
        cmd = input("MODLIST $ ").lower()
        if cmd == "exit":
            EFLG = EFLG & ~EFLG
        elif len(tokenize(cmd)) > 1:
            # command has multiple arguments
            EFLG = 0b0000000000000000
            tokenize(cmd)
        else:
            EFLG = 0b1111000010110001
            if cmd == "help" or cmd == "list" or cmd == "reload" or cmd == "refresh":
                EFLG = 0xA
                if cmd == "list":
                    for i in mods:
                        # print u'\u2713' Prints check mark 'approval'
                        if i['enabled']:
                            print(str(i['modName']) + "\nEnabled?  " + str(i['enabled']) + '\t\t\t' + u'\u2713')
                        else:
                            print(str(i['modName']) + "\nEnabled?  " + str(i['enabled']) + '\t\t\t' + u'\u2717')
                elif cmd == "reload" or cmd == "refresh":
                    EFLG = 0xB
                    mods = readMods()
                elif cmd == "help":
                    print("Usage MODLIST $ <help|list|refresh|enable|disable|add|remove>")
    if EFLG != 0:
        if EFLG == 0xB:
            return True
        return False
    else:
        return True
def mainFunc():
    # Initializes modlist in read mode
    mods = readMods()
    if not commandLoop(mods):
        print("An error has occured.\n")
    else:
        print("Exiting...\n")
if __name__ == '__main__':
    mainFunc()