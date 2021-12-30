"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""
import random
choices = ["rock", "paper", "scissors"]

class PlayerRock:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class PlayerRandom:
    def move(self):
        return random.choice(choices)

    def learn(self, my_move, their_move):
        pass


class PlayerHuman:
    def move(self):
        decision = input("Please choose rock, paper, or scissors.")
        if "rock" in decision.lower():
            return "rock"
        elif "paper" in decision.lower():
            return "paper"
        elif "scissors" in decision.lower():
            return "scissors"
        else:
            move()

    def learn(self, my_move, their_move):
        pass

class PlayerCycle:
    def move(self):
        try:
            if my_move == "paper":
                return "rock"
            elif my_move == "scissors":
                return "paper"
            elif my_move == "rock":
                return "scissors"
        except NameError:
            return random.choice(choices)


    def learn(self, my_move, their_move):
        newchoice = my_move


class PlayerLearn:
    def move(self):
        try:
            if PlayerLearn.learn.newchoice == "paper":
                return "scissors"
            elif PlayerLearn.learn.newchoice == "scissors":
                return "rock"
            elif PlayerLearn.learn.newchoice == "rock":
                return "paper"
        except NameError:
            return random.choice(choices)

    def learn(self, my_move, their_move):
        newchoice = their_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

def ties(one, two):
    return ((one == 'rock' and two == 'rock') or
            (one == 'scissors' and two == 'scissors') or
            (one == 'paper' and two == 'paper'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        try:
            gamecount = int(input("Enter the number of games to play."))
        except ValueError:
            Game(p1, p2).play_game()
        for round in range(gamecount):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    p1 = PlayerLearn()
    p2 = PlayerRock()
    game = Game(p1, p2)
    game.play_game()
