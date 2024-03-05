import random
import sys

class Die:
    def __init__(self):
        random.seed(0)  # Ensure reproducible rolls if needed

    def roll(self):
        return random.randint(1, 6)

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.tokens = {'skip': 0, 'steal': 0, 'shield': 0, 'double-up': 0}  # Magic Tokens

    def add_to_score(self, points):
        self.score += points

    def earn_token(self, token_type):
        if token_type in self.tokens:
            self.tokens[token_type] += 1
            print(f"{self.name} earned a {token_type} token!")

    def use_token(self, token_type):
        if self.tokens[token_type] > 0:
            self.tokens[token_type] -= 1
            print(f"{self.name} used a {token_type} token!")
            return True
        return False

    def reset_score(self):
        self.score = 0
        for token in self.tokens.keys():
            self.tokens[token] = 0

    def __str__(self):
        return f"{self.name}: {self.score} points, Tokens: {self.tokens}"

class Game:
    def __init__(self, num_players=2):
        self.players = [Player(f"Player {i + 1}") for i in range(num_players)]
        self.die = Die()
        self.current_player_index = 0

    def switch_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def play_turn(self, player):
        turn_total = 0
        rolling = True
        while rolling:
            roll = self.die.roll()
            print(f"{player.name} rolled a {roll}")

            if roll == 1:
                if player.use_token('shield'):
                    print(f"{player.name}'s shield token protected their turn!")
                    continue  # Skip the penalty and allow another roll
                turn_total = 0
                print(f"Sorry, {player.name}, you rolled a 1. No points this turn.")
                rolling = False
            else:
                turn_total += roll
                print(f"Current turn total: {turn_total}")

                # Check for earning tokens
                if turn_total >= 20:  # Example condition
                    player.earn_token('shield')

                decision = input("Roll again, hold, or use a token? (r/h/t): ")
                if decision.lower() == 'h':
                    player.add_to_score(turn_total)
                    rolling = False
                elif decision.lower() == 't':
                    token_type = input("Enter token type to use (skip/steal/shield/double-up): ")
                    if player.use_token(token_type):
                        # Implement the specific logic for each token type
                        pass  # Placeholder for token effect logic

    def play_game(self):
        print("Starting a new game...")
        while all(player.score < 100 for player in self.players):
            current_player = self.players[self.current_player_index]
            print(f"\n{current_player.name}'s turn")
            self.play_turn(current_player)
            print(current_player)
            if current_player.score >= 100:
                print(f"\n{current_player.name} wins!")
                break
            self.switch_player()

    def reset_game(self):
        for player in self.players:
            player.reset_score()
        self.current_player_index = 0

def main(num_players):
    game = Game(num_players)
    game.play_game()
    while input("Play another game? (y/n): ").lower() == 'y':
        game.reset_game()
        game.play_game()

if __name__ == "__main__":
    num_players = 2
    if len(sys.argv) > 1 and sys.argv[1].startswith('--numPlayers='):
        num_players = int(sys.argv[1].split('=')[1])
    main(num_players)
