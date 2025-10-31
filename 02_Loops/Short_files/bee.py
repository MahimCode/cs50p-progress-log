WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

def main():
    print("Welcome to Spelling Bee")
    print("The Words should be at least 4 character long.")
    print("Your letters are A I P C R H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left")
        guess = input("Guess the Word: ")

        if guess =="GRAPHIC":
            WORDS.clear()
            print("You've Won!")

        if guess in WORDS.keys():
            points = WORDS.pop(guess)
            print(f"Good job! You scored {points} points.")

    print("That's the game!")

main()