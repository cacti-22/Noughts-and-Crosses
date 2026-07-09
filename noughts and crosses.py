from random import randint

moves = ["TL","TC","TR","ML","MC","MR","BL","BC","BR"]

bob = 0
TL = " "
TC = " "
TR = " "
ML = " "
MC = " "
MR = " "
BL = " "
BC = " "
BR = " "
game = int(input("do you whant single or two player. 1 for single, 2 for double. "))
if game == 2:
    while bob == 0:
        move1 = input("where do you whant to move ")
        if move1 == "TL":
            if move1 in moves:
                TL = "x"
                moves.remove("TL")
            else:
                print("cant move here")
                continue
        elif move1 == "TC":
            if move1 in moves:
                TC = "x"
                moves.remove("TC")
            else:
                print("cant move here")
                continue
        elif move1 == "TR":
            if move1 in moves:
                TR = "x"
                moves.remove("TR")
            else:
                print("cant move here")
                continue
        elif move1 == "ML":
            if move1 in moves:
                ML = "x"
                moves.remove("ML")
            else:
                print("cant move here")
                continue
        elif move1 == "MC":
            if move1 in moves:
                MC = "x"
                moves.remove("MC")
            else:
                print("cant move here")
                continue
        elif move1 == "MR":
            if move1 in moves:
                MR = "x"
                moves.remove("MR")
            else:
                print("cant move here")
                continue
        elif move1 == "BL":
            if move1 in moves:
                BL = "x"
                moves.remove("BL")
            else:
                print("cant move here")
                continue
        elif move1 == "BC":
            if move1 in moves:
                BC = "x"
                moves.remove("BC")
            else:
                print("cant move here")
                continue
        elif move1 == "BR":
            if move1 in moves:
                BR = "x"
                moves.remove("BR")
            else:
                print("cant move here")
                continue
        print (TL,TC,TR)
        print (ML,MC,MR)
        print (BL,BC,BR)
        if TL == "x" and TC == "x" and TR == "x":
            print ("Player one wins.")
            bob = bob + 1
        elif ML == "x" and MC == "x" and MR == "x":
            print ("Player one wins.")
            bob = bob + 1
        elif BL == "x" and BC == "x" and BR == "x":
            print ("Player one wins.")
            bob = bob + 1
        elif TL == "x" and ML == "x" and BL == "x":
            print ("Player one wins.")
            bob = bob + 1
        elif TC == "x" and MC == "x" and BC == "x":
            print ("Player one wins.")
            bob = bob + 1
        elif TR == "x" and MR == "x" and BR == "x":
            print ("Player one wins.")
            bob = bob + 1
        elif TL == "x" and MC == "x" and BR == "x":
            print ("Player one wins.")
            bob = bob + 1
        elif TR == "x" and MC == "x" and BL == "x":
            print ("Player one wins.")
            bob = bob + 1
        while bob == 0:
            move2 = input("where do you whant to move ")
            if move2 == "TL":
                if move2 in moves:
                    TL = "o"
                    moves.remove("TL")
                else:
                    print("cant move here")
                    continue
            elif move2 == "TC":
                if move2 in moves:
                    TC = "o"
                    moves.remove("TC")
                else:
                    print("cant move here")
                    continue
            elif move2 == "TR":
                if move2 in moves:
                    TR = "o"
                    moves.remove("TR")
                else:
                    print("cant move here")
                    continue
            elif move2 == "ML":
                if move2 in moves:
                    ML = "o"
                    moves.remove("ML")
                else:
                    print("cant move here")
                    continue
            elif move2 == "MC":
                if move2 in moves:
                    MC = "o"
                    moves.remove("MC")
                else:
                    print("cant move here")
                    continue
            elif move2 == "MR":
                if move2 in moves:
                    MR = "o"
                    moves.remove("MR")
                else:
                    print("cant move here")
                    continue
            elif move2 == "BL":
                if move2 in moves:
                    BL = "o"
                    moves.remove("BL")
                else:
                    print("cant move here")
                    continue
            elif move2 == "BC":
                if move2 in moves:
                    BC = "o"
                    moves.remove("BC")
                else:
                    print("cant move here")
                    continue
            elif move2 == "BR":
                if move2 in moves:
                    BR = "o"
                    moves.remove("BR")
                else:
                    print("cant move here")
                    continue
            print (TL,TC,TR)
            print (ML,MC,MR)
            print (BL,BC,BR)
            if TL == "o" and TC == "o" and TR == "o":
                print ("Player two wins.")
                bob = bob + 1
            elif ML == "o" and MC == "o" and MR == "o":
                print ("Player two wins.")
                bob = bob + 1
            elif BL == "o" and BC == "o" and BR == "o":
                print ("Player two wins.")
                bob = bob + 1
            elif TL == "o" and ML == "o" and BL == "o":
                print ("Player two wins.")
                bob = bob + 1
            elif TC == "o" and MC == "o" and BC == "o":
                print ("Player two wins.")
                bob = bob + 1
            elif TR == "o" and MR == "o" and BR == "o":
                print ("Player two wins.")
                bob = bob + 1
            elif TL == "o" and MC == "o" and BR == "o":
                print ("Player two wins.")
                bob = bob + 1
            elif TR == "o" and MC == "o" and BL == "o":
                print ("Player two wins.")
                bob = bob + 1
            break

while bob == 0:
    move1 = input("where do you whant to move ")
    if move1 == "TL":
        if move1 in moves:
            TL = "x"
            moves.remove("TL")
        else:
            print("cant move here")
            continue
    elif move1 == "TC":
        if move1 in moves:
            TC = "x"
            moves.remove("TC")
        else:
            print("cant move here")
            continue
    elif move1 == "TR":
        if move1 in moves:
            TR = "x"
            moves.remove("TR")
        else:
            print("cant move here")
            continue
    elif move1 == "ML":
        if move1 in moves:
            ML = "x"
            moves.remove("ML")
        else:
            print("cant move here")
            continue
    elif move1 == "MC":
        if move1 in moves:
            MC = "x"
            moves.remove("MC")
        else:
            print("cant move here")
            continue
    elif move1 == "MR":
        if move1 in moves:
            MR = "x"
            moves.remove("MR")
        else:
            print("cant move here")
            continue
    elif move1 == "BL":
        if move1 in moves:
            BL = "x"
            moves.remove("BL")
        else:
            print("cant move here")
            continue
    elif move1 == "BC":
        if move1 in moves:
            BC = "x"
            moves.remove("BC")
        else:
            print("cant move here")
            continue
    elif move1 == "BR":
        if move1 in moves:
            BR = "x"
            moves.remove("BR")
        else:
            print("cant move here")
            continue
    print (f"{TL}|{TC}|{TR}")
    print ("-|-|-")
    print (f"{ML}|{MC}|{MR}")
    print ("-|-|-")
    print (f"{BL}|{BC}|{BR}")

    if TL == "x" and TC == "x" and TR == "x":
        print ("Player one wins.")
        bob = bob + 1
    elif ML == "x" and MC == "x" and MR == "x":
        print ("Player one wins.")
        bob = bob + 1
    elif BL == "x" and BC == "x" and BR == "x":
        print ("Player one wins.")
        bob = bob + 1
    elif TL == "x" and ML == "x" and BL == "x":
        print ("Player one wins.")
        bob = bob + 1
    elif TC == "x" and MC == "x" and BC == "x":
        print ("Player one wins.")
        bob = bob + 1
    elif TR == "x" and MR == "x" and BR == "x":
        print ("Player one wins.")
        bob = bob + 1
    elif TL == "x" and MC == "x" and BR == "x":
        print ("Player one wins.")
        bob = bob + 1
    elif TR == "x" and MC == "x" and BL == "x":
        print ("Player one wins.")
        bob = bob + 1
        
    while bob == 0:
        move2 = randint(0,8)
        if move2 == 0:
            if "TL" in moves:
                TL = "o"
                moves.remove("TL")
                break
            
        elif move2 == 1:
            if "TC" in moves:
                TC = "o"
                moves.remove("TC")
                break
            
        elif move2 == 2:
            if "TR" in moves:
                TR = "o"
                moves.remove("TR")
                break
            
        elif move2 == 3:
            if "ML" in moves:
                ML = "o"
                moves.remove("ML")
                break
            
        elif move2 == 4:
            if "MC" in moves:
                MC = "o"
                moves.remove("MC")
                break
            
        elif move2 == 5:
            if "MR" in moves:
                MR = "o"
                moves.remove("MR")
                break
            
        elif move2 == 6:
            if "BL" in moves:
                BL = "o"
                moves.remove("BL")
                break
            
        elif move2 == 7:
            if "BC" in moves:
                BC = "o"
                moves.remove("BC")
                break

        elif move2 == 8:
            if "BR" in moves:
                BR = "o"
                moves.remove("BR")
                break

    print (f"{TL}|{TC}|{TR}")
    print ("-|-|-")
    print (f"{ML}|{MC}|{MR}")
    print ("-|-|-")
    print (f"{BL}|{BC}|{BR}")
    if TL == "o" and TC == "o" and TR == "o":
        print ("Player two wins.")
        bob = bob + 1
    elif ML == "o" and MC == "o" and MR == "o":
        print ("Player two wins.")
        bob = bob + 1
    elif BL == "o" and BC == "o" and BR == "o":
        print ("Player two wins.")
        bob = bob + 1
    elif TL == "o" and ML == "o" and BL == "o":
        print ("Player two wins.")
        bob = bob + 1
    elif TC == "o" and MC == "o" and BC == "o":
        print ("Player two wins.")
        bob = bob + 1
    elif TR == "o" and MR == "o" and BR == "o":
        print ("Player two wins.")
        bob = bob + 1
    elif TL == "o" and MC == "o" and BR == "o":
        print ("Player two wins.")
        bob = bob + 1
    elif TR == "o" and MC == "o" and BL == "o":
        print ("Player two wins.")
        bob = bob + 1





