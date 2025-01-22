from RPS import player
from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player
from unittest import main


def run_simulation():
    # Playing 1000 rounds against all bots
    play(player, quincy, 1000, verbose=False)
    play(player, abbey, 1000, verbose=False)
    play(player, kris, 1000, verbose=False)
    play(player, mrugesh, 1000, verbose=False)

    # Uncomment line below to play interactively against a bot
    # play(human, abbey, 20, verbose=True)

    # Uncomment line below to play against a random player
    # play(human, random_player, 1000)

# Uncomment line below to run unit tests automatically
#main(module='test_module', exit=False)

# Running the simulation
if __name__ == "__main__":
    run_simulation()
