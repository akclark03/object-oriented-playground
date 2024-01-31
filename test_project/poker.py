from texas import Texas


class Poker:
    def run():
        players = -1
        while players < 2 or players > 10:
            try:
                players = int(input("\nHow many players? (2 - 10)\n"))
            finally:
                continue

        game = None
        ans = ""
        while ans != "T":
            ans = input("\nWhich game? (T)exas Hold 'Em\n")
            if ans == "T":
                game = Texas(players)

        count = 1
        while True:
            print("\n*** HAND", count, "***\n")
            game.play()
            count += 1


if __name__ == "__main__":
    Poker.run()
