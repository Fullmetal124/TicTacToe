element = None
Xturn = True
#board
a1B = "_"
a2B = "_"
a3B = "_"
b1B = "_"
b2B = "_" 
b3B = "_"
c1B = "_"
c2B = "_"
c3B = "_"
board = [[a1B,a2B,a3B], [b1B,b2B,b3B], [c1B,c2B,c3B]]

#board checking
A1 = "A1"
A2 = "A2"
A3 = "A3"
B1 = "B1"
B2 = "B2"
B3 = "B3"
C1 = "C1"
C2 = "C2"
C3 = "C3"
listx=[]
listo=[]
listpossible=[A1,A2,A3,B1,B2,B3,C1,C2,C3]
def printboard():
    global board
    board = [[a1B,a2B,a3B], [b1B,b2B,b3B], [c1B,c2B,c3B]]
    for row in board:
        print(" ".join(row))

def tictaccombatX():
    global A1,A2,A3,B1,B2,B3,C1,C2,C3,a1B,a2B,a3B,b1B,b2B,b3B,c1B,c2B,c3B,listx,listo,listpossible,board,Xturn
    printboard()
    Plr = input("X select a space:")
    if Plr.upper() ==  "A1":
        if A1 in listx:
            print("That space is already taken STUPID")
            tictaccombatX()
        elif A1 in listo:
            print("That space is already taken STUPID")
            tictaccombatX()
        else:    
            a1B= "X"
            element = A1
            index = listpossible.index(element)
            listx = listx[:index] + [element] + listx[index:]
            listpossible.remove(element)
            Xturn = not Xturn
            winningestcheck()
    if Plr.upper() ==  "A2":
        if A2 in listx:
            print("That space is already taken STUPID")
            tictaccombatX()
        elif A2 in listo:
            print("That space is already taken STUPID")
            tictaccombatX()
        else:    
            a2B= "X"
            element = A2
            index = listpossible.index(element)
            listx = listx[:index] + [element] + listx[index:]
            listpossible.remove(element)
            Xturn = not Xturn
            winningestcheck()
    if Plr.upper() ==  "A3":
        if A3 in listx:
            print("That space is already taken STUPID")
            tictaccombatX()
        elif A3 in listo:
            print("That space is already taken STUPID")
            tictaccombatX()
        else:    
            a3B= "X"
            element = A3
            index = listpossible.index(element)
            listx = listx[:index] + [element] + listx[index:]
            listpossible.remove(element)
            Xturn = not Xturn
            winningestcheck()
    if Plr.upper() ==  "B1":
        if B1 in listx:
            print("That space is already taken STUPID")
            tictaccombatX()
        elif B1 in listo:
            print("That space is already taken STUPID")
            tictaccombatX()
        else:    
            b1B= "X"
            element = B1
            index = listpossible.index(element)
            listx = listx[:index] + [element] + listx[index:]
            listpossible.remove(element)
            Xturn = not Xturn
            winningestcheck()
    if Plr.upper() ==  "B2":
        if B2 in listx:
            print("That space is already taken STUPID")
            tictaccombatX()
        elif B2 in listo:
            print("That space is already taken STUPID")
            tictaccombatX()
        else:    
            b2B= "X"
            element = B2
            index = listpossible.index(element)
            listx = listx[:index] + [element] + listx[index:]
            listpossible.remove(element)
            Xturn = not Xturn
            winningestcheck()
    if Plr.upper() ==  "B3":
        if B3 in listx:
            print("That space is already taken STUPID")
            tictaccombatX()
        elif B3 in listo:
            print("That space is already taken STUPID")
            tictaccombatX()
        else:    
            b3B= "X"
            element = B3
            index = listpossible.index(element)
            listx = listx[:index] + [element] + listx[index:]
            listpossible.remove(element)
            Xturn = not Xturn
            winningestcheck()
    if Plr.upper() ==  "C1":
        if C1 in listx:
            print("That space is already taken STUPID")
            tictaccombatX()
        elif C1 in listo:
            print("That space is already taken STUPID")
            tictaccombatX()
        else:    
            c1B= "X"
            element = C1
            index = listpossible.index(element)
            listx = listx[:index] + [element] + listx[index:]
            listpossible.remove(element)
            Xturn = not Xturn
            winningestcheck()
    if Plr.upper() ==  "C2":
        if C2 in listx:
            print("That space is already taken STUPID")
            tictaccombatX()
        elif C2 in listo:
            print("That space is already taken STUPID")
            tictaccombatX()
        else:    
            c2B= "X"
            element = C2
            index = listpossible.index(element)
            listx = listx[:index] + [element] + listx[index:]
            listpossible.remove(element)
            Xturn = not Xturn
            winningestcheck()
    if Plr.upper() ==  "C3":
        if C3 in listx:
            print("That space is already taken STUPID")
            tictaccombatX()
        elif C3 in listo:
            print("That space is already taken STUPID")
            tictaccombatX()
        else:    
            c3B= "X"
            element = C3
            index = listpossible.index(element)
            listx = listx[:index] + [element] + listx[index:]
            listpossible.remove(element)
            Xturn = not Xturn
            winningestcheck()
    else:
        print("could you input a real spot please :)                      stupid....")
        tictaccombatX()

def tictaccombatO():
    global A1,A2,A3,B1,B2,B3,C1,C2,C3,a1B,a2B,a3B,b1B,b2B,b3B,c1B,c2B,c3B,listx,listo,listpossible,board,Xturn
    printboard()
    Plr = input("O select a space:")
    if Plr.upper() ==  "A1":
        if A1 in listo:
            print("That space is already taken STUPID")
            tictaccombatO()
        elif A1 in listx:
            print("That space is already taken STUPID")
            tictaccombatO()
        else:    
            a1B= "O"
            element = A1
            index = listpossible.index(element)
            listo = listo[:index] + [element] + listo[index:]
            listpossible.remove(element)
            Xturn = not Xturn
            winningestcheck()
    if Plr.upper() ==  "A2":
        if A2 in listo:
            print("That space is already taken STUPID")
            tictaccombatO()
        elif A2 in listx:
            print("That space is already taken STUPID")
            tictaccombatO()
        else:    
            a2B= "O"
            element = A2
            index = listpossible.index(element)
            listo = listo[:index] + [element] + listo[index:]
            listpossible.remove(element)
            Xturn = not Xturn
            winningestcheck()
    if Plr.upper() ==  "A3":
        if A3 in listo:
            print("That space is already taken STUPID")
            tictaccombatO()
        elif A3 in listx:
            print("That space is already taken STUPID")
            tictaccombatO()
        else:    
            a3B= "O"
            element = A3
            index = listpossible.index(element)
            listo = listo[:index] + [element] + listo[index:]
            listpossible.remove(element)
            Xturn = not Xturn
            winningestcheck()
    if Plr.upper() ==  "B1":
        if B1 in listo:
            print("That space is already taken STUPID")
            tictaccombatO()
        elif B1 in listx:
            print("That space is already taken STUPID")
            tictaccombatO()
        else:    
            b1B= "O"
            element = B1
            index = listpossible.index(element)
            listo = listo[:index] + [element] + listo[index:]
            listpossible.remove(element)
            Xturn = not Xturn
            winningestcheck()
    if Plr.upper() ==  "B2":
        if B2 in listo:
            print("That space is already taken STUPID")
            tictaccombatO()
        elif B2 in listx:
            print("That space is already taken STUPID")
            tictaccombatO()
        else:    
            b2B= "O"
            element = B2
            index = listpossible.index(element)
            listo = listo[:index] + [element] + listo[index:]
            listpossible.remove(element)
            Xturn = not Xturn
            winningestcheck()
    if Plr.upper() ==  "B3":
        if B3 in listo:
            print("That space is already taken STUPID")
            tictaccombatO()
        elif B3 in listx:
            print("That space is already taken STUPID")
            tictaccombatO()
        else:    
            b3B= "O"
            element = B3
            index = listpossible.index(element)
            listo = listo[:index] + [element] + listo[index:]
            listpossible.remove(element)
            Xturn = not Xturn
            winningestcheck()
    if Plr.upper() ==  "C1":
        if C1 in listo:
            print("That space is already taken STUPID")
            tictaccombatO()
        elif C1 in listx:
            print("That space is already taken STUPID")
            tictaccombatO()
        else:    
            c1B= "O"
            element = C1
            index = listpossible.index(element)
            listo = listo[:index] + [element] + listo[index:]
            listpossible.remove(element)
            Xturn = not Xturn
            winningestcheck()
    if Plr.upper() ==  "C2":
        if C2 in listo:
            print("That space is already taken STUPID")
            tictaccombatO()
        elif C2 in listx:
            print("That space is already taken STUPID")
            tictaccombatO()
        else:    
            c2B= "O"
            element = C2
            index = listpossible.index(element)
            listo = listo[:index] + [element] + listo[index:]
            listpossible.remove(element)
            Xturn = not Xturn
            winningestcheck()
    if Plr.upper() ==  "C3":
        if C3 in listo:
            print("That space is already taken STUPID")
            tictaccombatO()
        elif C3 in listx:
            print("That space is already taken STUPID")
            tictaccombatO()
        else:    
            c3B= "O"
            element = C3
            index = listpossible.index(element)
            listo = listo[:index] + [element] + listo[index:]
            listpossible.remove(element)
            Xturn = not Xturn
            winningestcheck()
    else:
        print("could you input a real spot please :)                      stupid....")
        tictaccombatO()

def wincheck(tocheck):
    global a1B,a2B,a3B,b1B,b2B,b3B,c1B,c2B,c3B,listx,listo,listpossible
    if a1B == tocheck and a2B == tocheck and a3B == tocheck:
        return True
        
    elif b1B == tocheck and b2B == tocheck and b3B == tocheck:
        return True
    
    elif c1B == tocheck and c2B == tocheck and c3B == tocheck:
        return True
    
    elif a1B == tocheck and b1B == tocheck and c1B == tocheck:
        return True
    
    elif a2B == tocheck and b2B == tocheck and c2B == tocheck:
        return True
    
    elif a3B == tocheck and b3B == tocheck and c3B == tocheck:
        return True
    
    elif a1B == tocheck and b2B == tocheck and c3B == tocheck:
        return True
    
    elif a3B == tocheck and b2B == tocheck and c1B == tocheck:
        return True
        

        


def turncheck():
    if Xturn == True:
        tictaccombatX()
    elif Xturn == False:
        tictaccombatO()
        
    
tictaccombatX()

    #See if X is winner:
def winningestcheck():    
    if (wincheck("X")) == True:
        print ("X is the winner")
    if (wincheck("O")) == True:
        print("O is the winner")
    else:
        turncheck()
        
def plyagnchk():
    var3=input("Do you want to play again, quit to menu,? Y for yes, N for no, H for highscore")
    if var3.lower() == 'y':
        multiplayer()
    if var3.lower() == "n":
        rockmenu()