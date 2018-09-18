x = 1
y = 1

while True:
    if x == 1 and y == 1:
        print("You can travel: (N)orth.")
    elif x == 1 and y == 2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
    elif x == 1 and y == 3:
        print("You can travel: (E)ast or (S)outh.")
    elif x == 2 and y == 1:
        print("You can travel: (N)orth.")
    elif x == 2 and y == 2:
        print("You can travel: (S)outh or (W)est.")
    elif x == 2 and y == 3:
        print("You can travel: (E)ast or (W)est.")
    elif x == 3 and y == 1:
        print("Victory!")
        break
    elif x == 3 and y == 2:
        print("You can travel: (N)orth or (S)outh.")
    elif x == 3 and y == 3:
        print("You can travel: (S)outh or (W)est.")


    while True:
        dir = input("Direction: ")

        if dir == 'W' or dir == 'w':
            if x == 1 or (x == 2 and y == 1) or (x == 3 and y == 1) or (x == 3 and y == 2):
                print("Not a valid direction!")
            else:
                x = x - 1
                break

        elif dir == 'E' or dir == 'e':
            if x == 3 or (x == 2 and y == 1) or (x == 2 and y == 2) or (x == 1 and y == 1):
                print("Not a valid direction!")
            else:
                x = x + 1
                break

        elif dir == 'S' or dir =='s':
            if y == 1 or (x == 2 and y == 3):
                print("Not a valid direction!")
            else:
                y = y - 1
                break

        elif dir == 'N' or dir =='n':
            if y == 3 or (x == 2 and y == 2):
                print("Not a valid direction!")
            else:
                y = y + 1
                break