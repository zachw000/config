import json
EFLG = 0

def tokenize(command):
    tokens = command.split(' ')
    return tokens

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
def processTokens(tokens):
    return tokens
def commandLoop(mods):
    # Error flag, by default will assume error
    EFLG = 0b1111111111111111
    cmd = ""
    while cmd != "exit" or cmd != "stop" or cmd != "end":
        cmd = input("MODLIST $ ").lower()
        if cmd == "exit" or cmd == "stop" or cmd == "end" or cmd is None:
            EFLG = 0b00000
            break
        elif len(tokenize(cmd)) > 1:
            # command has multiple arguments
            EFLG = 0x0
            tkns = tokenize(cmd)
            processTokens(tkns)
        else:
            EFLG = 0b1111000010110001
            if cmd == "help" or cmd == "list" or cmd == "reload" or cmd == "refresh":
                EFLG = 0b1010   # 0xA
                if cmd == "list":
                    for i in mods:
                        # print u'\u2713' Prints check mark 'approval'
                        print('\t' + str(i['modName']) + "\n\t\tEnabled?  " + str(i['enabled']) + '\t\t' , end="")
                        if i['enabled']:
                            print(u'\u2713\n', end="")
                        else:
                            print(u'\u2717\n', end="")
                elif cmd == "reload" or cmd == "refresh":
                    EFLG = 0b1011 # 0xB
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