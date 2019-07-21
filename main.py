import Puzzle


class Main:

    def __init__(self):
        self.game_type = None
        self.state = [None] * 3
        self.puzzle = None

    def start(self):
        # self.game_type = input("plz enter whether (M)anual or using (A)i > ")
        # f_state = input("plz enter first state's directory > ")
        # self.game_type = 'M'
        f_state = 'input.txt'

        self.state = self.state_builder(f_state)

        self.puzzle = Puzzle.Puzzle(self.state)
        self.puzzle.start_manual()

    def state_builder(self, f_state):
        f = open(f_state, "r")
        state = [None] * 3
        if f.mode == "r":
            for i in range(3):
                state[i] = f.readline().split()
        return state


game = Main()
game.start()
