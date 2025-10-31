def main():

    difficulty = input("Difficult or Casual? ").lower().strip()
    if not (difficulty == "difficult" or difficulty == "casual"):
        print("Enter a valid difficulty")
        return

    players = input("Multiplayer or Single-player? ").lower().strip()
    if not (players == "multiplayer" or players == "single-player"):
        print("Enter a valid number of players")
        return


    if difficulty == "difficult" and players == "multiplayer":
        recommand("Poker")

    if difficulty == "difficult" and players == "single-player":
        recommand("Klondike")

    if difficulty == "casual" and players == "multiplayer":
        recommand("Hearts")

    if difficulty == "casual" and players == "single-player":
        recommand("Clock")


def recommand(game):
    print(f"You may like {game}")


main()