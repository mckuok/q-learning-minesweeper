from time import sleep

from minesweeper import MinesweeperWrapper
from qlearning import Agent, Environment, QLearning


def main():
    wrapper = MinesweeperWrapper()

    sleep(1)
    environment = Environment(wrapper.minesweeper)

    q = QLearning(environment.get_map_size(), 2)

    agent = Agent()
    picked = agent.pick()
    wrapper.minesweeper.onClick(wrapper.minesweeper.tiles[1][1])
    print('clicked')
    print(environment.get_clickable_tiles())



if __name__ == "__main__":
    main()
