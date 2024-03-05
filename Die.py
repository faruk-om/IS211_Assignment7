import random

class Die:
    def __init__(self):
        random.seed(0)  # Ensure reproducible rolls if needed

    def roll(self):
        return random.randint(1, 6)
