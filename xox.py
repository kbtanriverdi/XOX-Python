from random import *
import sys
grid = [[" "],[" "],[" "]],[[" "],[" "],[" "]],[[" "],[" "],[" "]]
turn = 0
playing = True
win = "-2"
pable = [[" "],[" "],[" "]],[[" "],[" "],[" "]],[[" "],[" "],[" "]]

def reset():
    global grid
    grid = [[" "],[" "],[" "]],[[" "],[" "],[" "]],[[" "],[" "],[" "]]
    global turn
    turn = 0
    global playing
    playing = True
    global win
    win = "-2"
    global pable
    pable = [[" "],[" "],[" "]],[[" "],[" "],[" "]],[[" "],[" "],[" "]]
    
def tcheck():
    while True:
        try:
            a=str(input("Try Again? (Y/N): "))
            if a == "Y":
                reset()
            elif a == "N":
                sys.exit()
                print("a")
            else:
                sys.exit()
                raise Exception
            break
        except:
            print(f"Invalid input: {a}")

def end():
    global playing
    if win=="1":
        print("Player Wins")
        playing=False
        tcheck()
    elif win=="0":
        print("Draw")
        playing=False
        tcheck()
    elif win == "-1":
        print("Computer Wins")
        playing=False
        tcheck()

def checkboard():
    rw = [0,0,0]
    col = [0,0,0]
    dio = [0,0]
    wp = "-2"
    p=False
    global win
    global playing
    for i in range(3):
        for a in range(3):
            if grid[i][a][0] == "X":
                rw[i] = rw[i]+1
            elif grid[i][a][0] == "O":
                rw[i] = rw[i]-1
            if grid[a][i][0] == "X":
                col[i] = col[i]+1
            elif grid[a][i][0] == "O":
                col[i] = col[i]-1
    for i in range(3):
        if grid[i][i][0] == 'X':
            dio[0] = dio[0]+1
        elif grid[i][i][0] == 'O':
            dio[0] = dio[0]-1
        elif grid[2-i][2-i][0] == 'X':
            dio[1] = dio[1]+1
        elif grid[2-i][2-i][0] == 'O':
            dio[1] = dio[1]-1
    if (3 in rw) or (3 in col):
        wp = "1"
        playing = p
    elif (-3 in rw) or (-3 in col):
        wp = "-1"
        playing = p
    elif (3 in dio):
        wp = "1"
        playing = p
    elif (-3 in dio):
        wp = "-1"
        playing = p
    else:
        if pable != []:
            pass
        else:
            wp = "0"
            playing = p
    win = wp

def update():
    case = "  "
    for i in range(len(grid)):
        for a in range(len(grid[i])):
            if a==(len(grid[i])-1):
                if i == (len(grid)-1):
                    case = case+str(grid[i][a][0])
                else:
                    case = case+str(grid[i][a][0])+"\n—————————————————\n  "
            else:
                case = case+str(grid[i][a][0])+"  |  "
    print(f"Turn : {turn}")
    print(case)
    checkboard()
    end()
update()

def play():
    playable = []
    for i in range(len(grid)):
        for a in range(len(grid[i])):
            if grid[i][a][0]!="X" and grid[i][a][0]!="O":
                playable.append([i,a])
    a=randint(0,len(playable)-1);
    grid[int(playable[a][0])][int(playable[a][1])] = "O"
    pable = playable
    
def playerP():
    while True:
        try:
            a = int(input("Select row: "))
            b = int(input("Select column: "))
            if a >=4 or b >=4:
                raise Exception
            cp = grid[a-1][b-1][0]
            if cp != "X":
                grid[a-1][b-1][0] = "X"
            else:
                print("This tile is unplayable")
                raise ValueError
            break
        except ValueError:
            pass
        except:
            print("Invalid argument")

while playing:
    turn=turn+1
    if turn >=10:
        print("draw")
        end()
        break
    else:
        checkboard()
        end()
        playerP()
        update()
        play()
        update()
        end()
    
