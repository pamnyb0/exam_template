from src.grid import Grid
from src.player import Player
from src import pickups


# TODO: flytta denna till en annan fil
class GameState:
    """Samla spelets variabler i en klass."""
    def __init__(self):
        self.score = 0
        self.inventory = []

        self.g = Grid()
        self.player = Player(self.g.width // 2, self.g.height // 2)
        self.g.set_player(self.player)
        self.g.make_walls()
        pickups.randomize(self.g)


# TODO: flytta denna till en annan fil
def print_status(game_grid, state):
    """Visa spelvärlden och antal poäng."""
    print("--------------------------------------")
    print(f"You have {state.score} points.")
    print(game_grid)


def start(state):
    command = "a"
    # Loopa tills användaren trycker Q eller X.
    while not command.casefold() in ["q", "x"]:
        print_status(state.g, state)

        command = input("Use WASD to move, Q/X to quit. ")
        command = command.casefold()[:1]

        if command == "d" and state.player.can_move(1, 0, state.g):  # move right
            # TODO: skapa funktioner, så vi inte behöver upprepa så mycket kod för riktningarna "W,A,S"
            maybe_item = state.g.get(state.player.pos_x + 1, state.player.pos_y)
            state.player.move(1, 0)

            if isinstance(maybe_item, pickups.Item):
                # we found something
                state.score += maybe_item.value
                print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
                #g.set(player.pos_x, player.pos_y, g.empty)
                state.g.clear(state.player.pos_x, state.player.pos_y)


    # Hit kommer vi när while-loopen slutar
    print("Thank you for playing!")


# __name__ skapas av Python och sätts till "__main__" om man startar game.py
# direkt. Detta är för att undvika att start-funktionen körs om man importerar
# saker från game.py i en annan fil, till exempel vid testning.
if __name__ == "__main__":
    game_state = GameState()
    start(game_state)
