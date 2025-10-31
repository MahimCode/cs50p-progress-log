def main():
    i = int(input("How many rows you want your box to contain? "))
    j = int(input("How many bricks you want to have in each rows? "))
    print_box(i,j)

def print_box(x,y):
    # For each row in box
    for i in range(x):
        # For each brick in box
        for j in range(y):
            print("#", end="")
        print()

main()
