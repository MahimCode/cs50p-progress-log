def main():
    difficulty = input("Difficult or Casual? ").lower().strip()
    players = input("Multiplayer or Single-player? ").lower().strip()

    if difficulty == "difficult":
        if players == "multiplayer":
            recommand("Poker")
        elif players == "single-player":
            recommand("Klondike")
        else:
            print("Enter a Valid number of players")
    elif difficulty == "casual":
        if players == "multiplayer":
            recommand("Hearts")
        elif players == "single-player":
            recommand("Clock")
        else:
            print("Enter a Valid number of players")
    else:
        print("Enter a valid difficulty")
        
def recommand(game):
    print(f"You may like {game}")


main()