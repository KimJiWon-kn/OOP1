
# print one horizontal line
def print_line():
    print("+ - - - - + - - - - +")

# print one vertical line
def print_column():
    print("|         |         |")

# draw grid
def draw_grid():
    print_line()
    for i in range(4):
        print_column()
    print_line()
    for i in range(4):
        print_column()
    print_line()

# run
draw_grid()