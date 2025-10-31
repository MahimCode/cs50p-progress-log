def area(length, width):
    print(length * width,'square feet')
    return length * width


def main():
    #take input from user
    home_length = int(input("Enter home length: "))
    home_width = int(input("Enter home width: "))
    home = area (home_length, home_width)

    yard_length = int(input("Enter yard length: "))
    yard_width = int(input("Enter yard width: "))
    yard = area (yard_length, yard_width)
    
    total = home + yard
    print("total is", total, "square feet")
main()