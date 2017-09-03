"""
In this file we will do all the computations related to screen division.
"""
import pygame

import block

SPLIT_IN = (15, 10)
blocks = [] # This is an array of blocks, all the blocks that are made in the level creator will be in this array


def make_blocks(screen):
    """
    We have to bring in all the blocks according to the levels.
    """
    row_length, col_length = screen.get_width() / SPLIT_IN[0], screen.get_height() / SPLIT_IN[1]
    for row in range(SPLIT_IN[0]):
        for col in range(SPLIT_IN[1]):
            blocks.append(block.Block(row * row_length, col * col_length, row_length, col_length))


def display_blocks(screen):
    """
    This method will display all the blocks that are present in the block array.
    """
    for block in blocks:
        pygame.draw.rect(screen, (255, 255, 102), block.rect, 5)

"""
Keybindings

e - empty
f - fire
w - water
x - villain type 1
y - villain type 2
z - villain type 3
b - brick
p - player


A level file has to have exactly 20 rows.
"""


def create_block(pos_x, pos_y, type):
    """
    This method will take in the type of block that we have to make at (pos_x, pos_y), andcreate the block and return it.
    """
    if type == "":
        return block.Block(pos_x, pos_y)
    if type == "f":
        return fire.Fire(pos_x, pos_y)
    if type == "w":
        return water.Water(pos_x, pos_y)
    if type == "x":
        return villain.Villain_a(pos_x, pos_y)
    if type == "y":
        return villain.Villain_b(pos_x, pos_y)
    if type == "z":
        return villain.Villain_c(pos_x, pos_y)
    if type == "b":
        return brick.Brick(pos_x, pos_y)


initial_page = [
["b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"],
["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
["", "", "", "", "", "", "", "", "", "", "", "", "x", "", ""],
["", "", "", "", "", "", "", "", "b", "", "", "", "", "y", ""],
["", "", "", "", "", "", "", "", "", "", "", "", "", "", "z"],
["", "", "", "", "", "", "", "", "", "", "w", "", "", "", ""],
["", "", "", "b", "", "b", "", "", "f", "", "", "", "", "b", ""],
["", "", "b", "b", "b", "b", "b", "", "", "", "", "", "", "", ""],
["", "b", "b", "", "", "", "", "", "", "", "", "", "", "", ""],
["b", "b", "b", "", "", "", "", "", "", "b", "b", "b", "", "b", ""]]
