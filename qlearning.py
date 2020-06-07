import numpy as np

from minesweeper import STATE_DEFAULT


class Agent:

    def pick(self):
        return (0, 0)


class Environment:

    def __init__(self, minesweeper):
        self.minesweeper = minesweeper

    def get_clickable_tiles(self):
        clickables = []
        tiles = self.minesweeper.tiles
        for x, col in tiles.items():
            for y, tile in col.items():
                if Environment.tile_is_clickable(tile):
                    clickables.append((x, y))

        return clickables

    @staticmethod
    def tile_is_clickable(tile):
        return tile['state'] == STATE_DEFAULT

    def get_map_size(self):
        tiles = self.minesweeper.tiles
        return len(tiles) * len(tiles[0])

    def has_won(self):
        return self.minesweeper.clickedCount == self.get_map_size() - self.minesweeper.mines


class QLearning:

    def __init__(self, state_num, action_num, learning_rate=0.1, discount_factor=1.0):
        self.q_matrix = np.zeros((state_num, action_num))
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor

    def update(self, state, action, reward, next_state):
        q_matrix = self.q_matrix
        learning_rate = self.learning_rate
        discount_factor = self.discount_factor
        q_matrix[state, action] = (1 - learning_rate) * q_matrix[state, action] + learning_rate * \
                                  (reward + discount_factor * np.max(q_matrix[next_state]))
