emptyspace = "      |      "
disk1 = "     ***     "
disk2 = "   *******   "
disk3 = " *********** "
disk = ""
pos = ""
movenum = 0
lod1 = []
lod2 = []
lod3 = []
lod1.append(disk1)
lod1.append(emptyspace)
lod1.append(emptyspace)
lod2.append(disk2)
lod2.append(emptyspace)
lod2.append(emptyspace)
lod3.append(disk3)
lod3.append(emptyspace)
lod3.append(emptyspace)
def List():
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
    LIST = ""
    for item in lod1:
        LIST = LIST + item
    print(LIST)
    LIST = ""
    for item in lod2:
        LIST = LIST + item
    print(LIST)
    LIST = ""
    for item in lod3:
        LIST = LIST + item
    print(LIST)
def move():
    wpeg = input("Which peg would you like to change? (1/2/3)")
    wpos = input("Which peg would you like to move that disk to? (1/2/3)")
    if wpeg == "1":
        peg1 = lod1[0],lod2[0],lod3[0]
        peg2 = lod1[1],lod2[1],lod3[1]
        peg3 = lod1[2],lod2[2],lod3[2]
        if peg1[0] == emptyspace:
            if peg1[1] == emptyspace:
                if peg1[2] == emptyspace:
                    print("There are no disks on this peg.")
                else:
                    disk = peg1[2]
                    pos = 3
                    if peg1[2] == disk1:
                        dv1 = 1
                    if peg1[2] == disk2:
                        dv1 = 2
                    if peg1[2] == disk3:
                        dv1 = 3
            else:
                disk = peg1[1]
                pos = 2
                if peg1[1] == disk1:
                    dv1 = 1
                if peg1[1] == disk2:
                    dv1 = 2
                if peg1[1] == disk3:
                    dv1 = 3
        else:
            disk = peg1[0]
            pos = 1
            if peg1[0] == disk1:
                dv1 = 1
            if peg1[0] == disk2:
                dv1 = 2
            if peg1[0] == disk3:
                dv1 = 3
        if wpos == "1":
            print("You can't move it to the same peg")
        if wpos == "2":
            if peg2[0] == emptyspace:
                if peg2[1] == emptyspace:
                    if peg2[2] == emptyspace:
                      try:
                        lod3[1] = disk
                        if pos == 1:
                            lod1[0] = emptyspace
                        if pos == 2:
                            lod2[0] = emptyspace
                        if pos == 3:
                            lod3[0] = emptyspace
                      except:
                        pass
                    else:
                        if peg2[2] == disk1:
                            dv2 = 1
                        elif peg2[2] == disk2:
                            dv2 = 2
                        elif peg2[2] == disk3:
                            dv2 = 3
                        if dv1 > dv2:
                            print("You cannot make that move.")
                        else:
                          try:
                            lod2[1] = disk
                            if pos == 1:
                                lod1[0] = emptyspace
                            if pos == 2:
                                lod2[0] = emptyspace
                            if pos == 3:
                                lod3[0] = emptyspace
                          except:
                            pass
                else:
                    if peg2[1] == disk1:
                        dv2 = 1
                    elif peg2[1] == disk2:
                        dv2 = 2
                    elif peg2[1] == disk3:
                        dv2 = 3
                    if dv1 > dv2:
                        print("You cannot make that move.")
                    else:
                      try:
                        lod1[1] = disk
                        if pos == 1:
                            lod1[0] = emptyspace
                        if pos == 2:
                            lod2[0] = emptyspace
                        if pos == 3:
                            lod3[0] = emptyspace
                      except:
                        pass
            else:
                if peg2[0] == disk1:
                    dv2 = 1
                if peg2[0] == disk2:
                    dv2 = 2
                if peg2[0] == disk3:
                    dv2 = 3
                if dv1 > dv2:
                    print("You cannot make that move")
                else:
                  try:
                    lod1[1] = disk
                    if pos == 1:
                        lod1[0] = emptyspace
                    if pos == 2:
                        lod1[0] = emptyspace
                    if pos == 3:
                        lod1[0] = emptyspace
                  except:
                    pass

        if wpos == "3":
            if peg3[0] == emptyspace:
                if peg3[1] == emptyspace:
                    if peg3[2] == emptyspace:
                      try:
                        lod3[2] = disk
                        if pos == 1:
                            lod1[0] = emptyspace
                        if pos == 2:
                            lod2[0] = emptyspace
                        if pos == 3:
                            lod3[0] = emptyspace
                      except:
                        pass
                    else:
                        if peg3[2] == disk1:
                            dv3 = 1
                        if peg3[2] == disk2:
                            dv3 = 2
                        if peg3[2] == disk3:
                            dv3 = 3
                        if dv1 > dv3:
                            print("You cannot make that move.")
                        else:
                          try:
                            lod2[2] = disk
                            if pos == 1:
                                lod1[0] = emptyspace
                            if pos == 2:
                                lod2[0] = emptyspace
                            if pos == 3:
                                lod3[0] = emptyspace
                          except:
                            pass
                else:
                    if peg3[1] == disk1:
                        dv3 = 1
                    if peg3[1] == disk2:
                        dv3 = 2
                    if peg3[1] == disk3:
                        dv3 = 3
                    if dv1 > dv3:
                        print("You cannot make that move.")
                    else:
                      try:
                        lod1[2] = disk
                        if pos == 1:
                            lod1[0] = emptyspace
                        if pos == 2:
                            lod2[0] = emptyspace
                        if pos == 3:
                            lod3[0] = emptyspace
                      except:
                        pass
    if wpeg == "2":
        peg1 = lod1[0],lod2[0],lod3[0]
        peg2 = lod1[1],lod2[1],lod3[1]
        peg3 = lod1[2],lod2[2],lod3[2]
        if peg2[0] == emptyspace:
            if peg2[1] == emptyspace:
                if peg2[2] == emptyspace:
                    print("There are no disks on this peg.")
                else:
                    disk = peg2[2]
                    pos = 3
                    if peg2[2] == disk1:
                        dv1 = 1
                    if peg2[2] == disk2:
                        dv1 = 2
                    if peg2[2] == disk3:
                        dv1 = 3
            else:
                disk = peg2[1]
                pos = 2
                if peg2[1] == disk1:
                    dv1 = 1
                if peg2[1] == disk2:
                    dv1 = 2
                if peg2[1] == disk3:
                    dv1 = 3
        else:
            disk = peg2[0]
            pos = 1
            if peg2[0] == disk1:
                dv1 = 1
            if peg2[0] == disk2:
                dv1 = 2
            if peg2[0] == disk3:
                dv1 = 3
        if wpos == "1":
            if peg1[0] == emptyspace:
                if peg1[1] == emptyspace:
                    if peg1[2] == emptyspace:
                      try:
                        lod3[0] = disk
                        if pos == 1:
                            lod1[1] = emptyspace
                        if pos == 2:
                            lod2[1] = emptyspace
                        if pos == 3:
                            lod3[1] = emptyspace
                      except:
                        pass
                    else:
                        if peg1[2] == disk1:
                            dv2 = 1
                        if peg1[2] == disk2:
                            dv2 = 2
                        if peg1[2] == disk3:
                            dv2 = 3
                        if dv1 > dv2:
                            print("You cannot make that move.")
                        else:
                          try:
                            lod2[0] = disk
                            if pos == 1:
                                lod1[1] = emptyspace
                            if pos == 2:
                                lod2[1] = emptyspace
                            if pos == 3:
                                lod3[1] = emptyspace
                          except:
                            pass
                else:
                    if peg1[1] == disk1:
                        dv2 = 1
                    if peg1[1] == disk2:
                        dv2 = 2
                    if peg1[1] == disk3:
                        dv2 = 3
                    if dv1 > dv2:
                        print("You cannot make that move.")
                    else:
                      try:
                        lod3[0] = disk
                        if pos == 1:
                            lod2[1] = emptyspace
                        if pos == 2:
                            lod2[1] = emptyspace
                        if pos == 3:
                            lod2[1] = emptyspace
                      except:
                        pass

        if wpos == "2":
            print("You cannot put the disk on the same peg.")
        if wpos == "3":
            if peg3[0] == emptyspace:
                if peg3[1] == emptyspace:
                    if peg3[2] == emptyspace:
                      try:
                        lod3[2] = disk
                        if pos == 1:
                            lod1[1] = emptyspace
                        if pos == 2:
                            lod2[1] = emptyspace
                        if pos == 3:
                            lod3[1] = emptyspace
                      except:
                        pass
                    else:
                        if peg3[2] == disk1:
                            dv3 = 1
                        if peg3[2] == disk2:
                            dv3 = 2
                        if peg3[2] == disk3:
                            dv3 = 3
                        if dv1 > dv3:
                            print("You cannot make that move.")
                        else:
                          try:
                            lod2[2] = disk
                            if pos == 1:
                                lod1[1] = emptyspace
                            if pos == 2:
                                lod2[1] = emptyspace
                            if pos == 3:
                                lod3[1] = emptyspace
                          except:
                            pass
                else:
                    if peg3[1] == disk1:
                        dv3 = 1
                    if peg3[1] == disk2:
                        dv3 = 2
                    if peg3[1] == disk3:
                        dv3 = 3
                    if dv1 > dv3:
                        print("You cannot make that move.")
                    else:
                      try:
                        lod1[2] = disk
                        if pos == 1:
                            lod2[1] = emptyspace
                        if pos == 2:
                            lod3[1] = emptyspace
                        if pos == 3:
                            lod3[1] = emptyspace
                      except:
                        pass
    if wpeg == "3":
        peg1 = lod1[0],lod2[0],lod3[0]
        peg2 = lod1[1],lod2[1],lod3[1]
        peg3 = lod1[2],lod2[2],lod3[2]
        if peg3[0] == emptyspace:
            if peg3[1] == emptyspace:
                if peg3[2] == emptyspace:
                    print("There are no disks on this peg.")
                else:
                  try:
                    disk = peg3[2]
                    pos = 3
                    if peg3[2] == disk1:
                        dv1 = 1
                    if peg2[2] == disk2:
                        dv1 = 2
                    if peg2[2] == disk3:
                        dv1 = 3
                  except:
                    pass
            else:
                disk = peg3[1]
                pos = 2
                if peg3[2] == disk1:
                    dv1 = 1
                if peg2[2] == disk2:
                    dv1 = 2
                if peg2[2] == disk3:
                    dv1 = 3
        else:
            disk = peg3[0]
            pos = 1
            if peg3[2] == disk1:
                dv1 = 1
            if peg2[2] == disk2:
                dv1 = 2
            if peg2[2] == disk3:
                dv1 = 3
        if wpos == "1":
            if peg1[0] == emptyspace:
                if peg1[1] == emptyspace:
                    if peg1[2] == emptyspace:
                      try:
                        lod3[0] = disk
                        if pos == 1:
                            lod1[2] = emptyspace
                        if pos == 2:
                            lod2[2] = emptyspace
                        if pos == 3:
                            lod3[2] = emptyspace
                      except:
                        pass
                    else:
                        if peg1[2] == disk1:
                            dv2 = 1
                        if peg1[2] == disk2:
                            dv2 = 2
                        if peg1[2] == disk3:
                            dv2 = 3
                        if dv1 > dv2:
                            print("You cannot make that move.")
                        else:
                          try:
                            lod2[0] = disk
                            if pos == 1:
                                lod1[2] = emptyspace
                            if pos == 2:
                                lod2[2] = emptyspace
                            if pos == 3:
                                lod3[2] = emptyspace
                          except:
                            pass
                else:
                    if peg1[1] == disk1:
                        dv2 = 1
                    if peg1[1] == disk2:
                        dv2 = 2
                    if peg1[1] == disk3:
                        dv2 = 3
                    if dv1 > dv2:
                        print("You cannot make that move.")
                    else:
                      try:
                        lod1[0] = disk
                        if pos == 1:
                            lod1[2] = emptyspace
                        if pos == 2:
                            lod2[2] = emptyspace
                        if pos == 3:
                            lod3[2] = emptyspace
                      except:
                        pass
        if wpos == "2":
            if peg2[0] == emptyspace:
                if peg2[1] == emptyspace:
                    if peg2[2] == emptyspace:
                      try:
                        lod3[1] = disk
                        if pos == 1:
                            lod1[2] = emptyspace
                        if pos == 2:
                            lod2[2] = emptyspace
                        if pos == 3:
                            lod3[2] = emptyspace
                      except:
                        pass
                    else:
                        if peg2[2] == disk1:
                            dv3 = 1
                        if peg2[2] == disk2:
                            dv3 = 2
                        if peg2[2] == disk3:
                            dv3 = 3
                        if dv1 > dv3:
                            print("You cannot make that move.")
                        else:
                          try:
                            lod2[1] = disk
                            if pos == 1:
                                lod1[2] = emptyspace
                            if pos == 2:
                                lod2[2] = emptyspace
                            if pos == 3:
                                lod3[2] = emptyspace
                          except:
                            pass
                else:
                    if peg2[1] == disk1:
                        dv3 = 1
                    if peg2[1] == disk2:
                        dv3 = 2
                    if peg2[1] == disk3:
                        dv3 = 3
                    if dv1 > dv3:
                        print("You cannot make that move")
                    else:
                      try:
                        lod2[1] = disk
                        if pos == 1:
                            lod1[2] = emptyspace
                        if pos == 2:
                            lod2[2] = emptyspace
                        if pos == 3:
                            lod3[2] = emptyspace
                      except:
                        pass
        if wpos == "3":
            print("You cannot place a disk in this spot.")
while True:

    peg3 = lod1[2],lod2[2],lod3[2]
    if peg3[0] == disk1 and peg3[1] == disk2 and peg3[2] == disk3:
        print(chr(27)+'[2j')
        print('\033c')
        print('\x1bc')
        List()
        print("You Win!                      Moves:",movenum)
        break
    else:
        List()
        print("                           Moves:",movenum)
        movenum = movenum + 1
        move()
        continue
