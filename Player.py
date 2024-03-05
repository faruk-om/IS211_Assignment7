class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.tokens = {'skip': 0, 'steal': 0, 'shield': 0, 'double-up': 0}

    def add_token(self, token):
        self.tokens[token] += 1

    def use_token(self, token):
        if self.tokens[token] > 0:
            self.tokens[token] -= 1
            return True
        return False

    def has_token(self, token):
        return self.tokens[token] > 0

    def __str__(self):
        return f"{self.name}: {self.score} points, Tokens: {self.tokens}"

class Game:
    # Existing code...

    def use_token(self, player):
        choice = input("Roll again, hold, or use a token? (r/h/t): ")
        if choice.lower() == 't':
            token_choice = input("Which token would you like to use? (skip/steal/shield/double-up): ")
            if player.has_token(token_choice):
                if token_choice == 'skip':
                    self.switch_player()
                elif token_choice == 'steal':
                    # Implement logic to steal points from another player
                    pass
                elif token_choice == 'shield':
                    # Implement logic to protect against losing points
                    pass
                elif token_choice == 'double-up':
                    # Implement logic to double points on the next roll
                    pass
                player.use_token(token_choice)
            else:
                print("You don't have that token. Please choose another action.")
                self.use_token(player)
        else:
            return choice

    def play_turn(self, player):
        turn_total = 0
        rolling = True
        while rolling:
            roll = self.die.roll()
            print(f"{player.name} rolled a {roll}")
            if roll == 1:
                turn_total = 0
                print(f"Sorry, {player.name}, you rolled a 1. No points this turn.")
                rolling = False
            else:
                turn_total += roll
                print(f"Current turn total: {turn_total}")
                decision = self.use_token(player)
                if decision.lower() == 'h':
                    player.add_to_score(turn_total)
                    rolling = False
