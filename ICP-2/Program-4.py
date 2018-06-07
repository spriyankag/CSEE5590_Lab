heightinp= int(input("Enter the height of the board: "))
widthinp= int(input("Enter the width of the board: "))


def board_draw(heightinp, widthinp):
    for i in range(0,heightinp):
        for j in range(0, widthinp):
            print(" ---", end=" ")
        print("\r")
        for j in range(0,widthinp+1):
            print("|   ", end= " ")
        print("\r")
    for j in range(0, widthinp ):
        print(" ---", end=" ")



board_draw(heightinp,widthinp)