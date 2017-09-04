"""
This module has methods to do computations related to screen division and display.
"""
import pygame

# import binder
import blocks.block as block
import blocks.brick as brick
import blocks.bullet as bullet
import blocks.fire as fire
import blocks.player as player
import blocks.villain as villain
import blocks.water as water

SPLIT_IN = (15, 10)
blocks = []
# This is an array of blocks, all the blocks
# that are made in the level creator will be in this array

# row_length, col_length = binder.screen.get_width() / SPLIT_IN[0],\
                        #  binder.screen.get_height() / SPLIT_IN[1]




def make_blocks(screen, bricks):
    """
    We have to bring in all the blocks according to the levels.
    """
    row_length, col_length = screen.get_width() / SPLIT_IN[0],\
                                screen.get_height() / SPLIT_IN[1]
    for row_num, row in enumerate(INITIAL_PAGE):
        for col_num, ele in enumerate(row):
            blocks.append(create_block(col_num * row_length, row_num * col_length,\
                                       row_length, col_length, ele))
            if ele =="b":
                bricks.add(blocks[-1])


def display_blocks(screen):
    """
    This method will display all the blocks that are present in the block array.
    """
    for b in blocks:
        # pygame.draw.rect(screen, (255, 30, 80), b.rect, 2)
        screen.blit(b.image, b.rect)


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


def create_block(pos_x, pos_y, size_x, size_y, typ):
    """
    Takes in 
    """
    if typ == "":
        return block.Block(pos_x, pos_y, size_x, size_y)
    if typ == "f":
        return fire.Fire(pos_x, pos_y, size_x, size_y)
    if typ == "w":
        return water.Water(pos_x, pos_y, size_x, size_y)
    if typ == "x":
        return villain.Villain_a(pos_x, pos_y, size_x, size_y)
    if typ == "y":
        return villain.Villain_b(pos_x, pos_y, size_x, size_y)
    if typ == "z":
        return villain.Villain_c(pos_x, pos_y, size_x, size_y)
    if typ == "b":
        return brick.Brick(pos_x, pos_y, size_x, size_y)


INITIAL_PAGE = [
    ["b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"],
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", "f", "", "", "x", "", ""],
    ["", "", "", "", "b", "b", "", "", "b", "", "", "", "", "y", ""],
    ["", "", "", "", "", "", "", "b", "", "", "", "", "", "", "z"],
    ["", "", "", "", "", "", "", "", "", "", "w", "", "", "", ""],
    ["", "", "", "b", "", "b", "", "", "f", "", "", "", "", "b", ""],
    ["", "", "b", "b", "b", "", "b", "", "", "", "b", "", "", "", ""],
    ["", "b", "b", "", "", "", "", "", "b", "", "", "", "", "", ""],
    ["b", "", "", "", "", "", "", "", "", "b", "b", "b", "", "b", ""]]
