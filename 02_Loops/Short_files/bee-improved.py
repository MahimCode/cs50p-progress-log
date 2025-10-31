WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

def main():
    print("Welcome to Spelling Bee 🐝")
    print("Rules:")
    print("- Words must be at least 4 letters long.")
    print("- Your letters are: A I P C R H G")
    print("- Type 'quit' anytime to stop.\n")

    total_score = 0
    remaining_words = WORDS.copy()

    while remaining_words:
        print(f"{len(remaining_words)} words left.")
        guess = input("Guess a word: ").strip().upper()

        if guess == "QUIT":
            print("You quit the game.")
            break

        if guess == "GRAPHIC":
            print("You've found the longest word and won the game!")
            total_score += remaining_words.pop(guess, 0)
            remaining_words.clear()
            break

        if guess in remaining_words:
            points = remaining_words.pop(guess)
            total_score += points
            print(f"✅ Good job! You earned {points} points.")
        else:
            if guess in WORDS:
                print("⚠️ You already guessed that word!")
            else:
                print("❌ Invalid word. Try again!")

        print(f"Current score: {total_score}\n")

    print("\n🎉 Game over!")
    print(f"Your final score: {total_score}")

main()
