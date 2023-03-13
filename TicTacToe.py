def tictactoeboard():
    a1 = "_"
    a2 = "_"
    a3 = "_"
    b1 = "_"
    b2 = "_" 
    b3 = "_"
    c1 = "_"
    c2 = "_"
    c3 = "_"
    board = [[a1,a2,a3], [b1,b2,b3], [c1,c2,c3]]
    for row in board:
        print(" ".join(row))

tictactoeboard()
    
