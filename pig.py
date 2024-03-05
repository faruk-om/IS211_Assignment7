def main():
    num_players = 2  # Default number of players
    if len(sys.argv) > 1 and sys.argv[1].startswith('--numPlayers='):
        num_players = int(sys.argv[1].split('=')[1])

    while True:
        game = Game(num_players)
        game.play_game()

        play_again = input("Play another game? (y/n): ").lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    main()
