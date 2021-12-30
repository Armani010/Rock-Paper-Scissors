import random
moves = ['rock', 'paper', 'scissors']

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

"""The Player class is the parent class for all of the Players
in this game"""


class PlayerRock:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class PlayerPaper:
    def move(self):
        return 'paper'

    def learn(self, my_move, their_move):
        pass


class PlayerScissors:
    def move(self):
        return 'scissors'

    def learn(self, my_move, their_move):
        pass


class PlayerRandom:
    def move(self):
        return random.choice(moves)

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
            self.move()

    def learn(self, my_move, their_move):
        pass


class PlayerCycle:
    cycle = 0

    def move(self):
        if PlayerCycle.cycle % 3 == 0 or PlayerCycle.cycle % 3 == 3:
            return "rock"
        elif PlayerCycle.cycle % 3 == 1:
            return "paper"
        elif PlayerCycle.cycle % 3 == 2:
            return "scissors"
        PlayerCycle.cycle += 1

    def learn(self, my_move, their_move):
        pass


class PlayerLearn:
    def learn(self, my_move, their_move):
        self.next_move = their_move

    def move(self):
        try:
            self.learn(my_move, their_move)
            if self.next_move == "paper":
                return "scissors"
            elif self.next_move== "scissors":
                return "rock"
            elif self.next_move == "rock":
                return "paper"
        except NameError:
            return random.choice(moves)


def beats(self, one, two):
    if ((one == 'rock' and two == 'scissors') or (one == 'scissors' and two == 'paper') or (one == 'paper' and two == 'rock')):
        print("** PLAYER ONE WINS**")
        self.score1 += 1
        print(f"Player 1's score is {self.score1}. Player 2's score is {self.score2}.")
    elif((two == 'rock' and one == 'scissors') or (two == 'scissors' and one == 'paper') or (two == 'paper' and one == 'rock')):
        print("** PLAYER TWO WINS **")
        self.score2 += 1
        print(f"Player 1's score is {self.score1}. Player 2's score is {self.score2}.")
    elif ((one == 'rock' and two == 'rock') or (one == 'scissors' and two == 'scissors') or (one == 'paper' and two == 'paper')):
        print("** TIE **")
        print(f"Player 1's score is {self.score1}. Player 2's score is {self.score2}.")


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        beats(self, move1, move2)
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
