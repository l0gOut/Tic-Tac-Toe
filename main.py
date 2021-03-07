def x_and_o(x):
    print("---------")
    print(f"| {x[0][0]} {x[0][1]} {x[0][2]} |")
    print(f"| {x[1][0]} {x[1][1]} {x[1][2]} |")
    print(f"| {x[2][0]} {x[2][1]} {x[2][2]} |")
    print("---------")


cells = "         "
symbol = ["X", "O"]
if_draw = ""
flag = 0
matrix = [[x for x in cells[0:3]],
          [x for x in cells[3:6]],
          [x for x in cells[6:9]]]
x_and_o(matrix)

while True:
    try:
        draw = ""
        x, y = input("Enter the coordinates: ").split()
        x = int(x)
        y = int(y)
        if not 0 < x < 4 or not 4 > y > 0:
            print("Coordinates should be from 1 to 3!")
            continue
        else:
            if matrix[x - 1][y - 1] != " ":
                print("This cell is occupied! Choose another one!")
                continue
            else:
                matrix[x - 1][y - 1] = symbol[flag]
                x_and_o(matrix)
                for i in matrix:
                    if "".join(i) == "XXX" or "".join(i) == "OOO":
                        print(f"{symbol[flag]} wins!")
                        break
                else:
                    for i in range(3):
                        word = matrix[0][i] + matrix[1][i] + matrix[2][i]
                        if word == "XXX" or word == "OOO":
                            print(f"{symbol[flag]} wins!")
                            break
                        draw += "".join(matrix[i]).replace(" ", "")
                    else:
                        if_draw = draw
                        word1 = matrix[0][0] + matrix[1][1] + matrix[2][2]
                        word2 = matrix[0][2] + matrix[1][1] + matrix[2][0]
                        if word1 == "XXX" or word1 == "OOO":
                            print(f"{symbol[flag]} wins!")
                            break
                        elif word2 == "XXX" or word2 == "OOO":
                            print(f"{symbol[flag]} wins!")
                            break
                        elif len(if_draw) == 9:
                            print("Draw!")
                            break
                        flag = (1 if flag == 0 else 0)
                        continue
                    break
                break
    except ValueError:
        print("You should enter numbers!")
