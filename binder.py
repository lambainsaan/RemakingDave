import sys, pygame
import os
import blocks.brick as brick
import blocks.player as player
import blocks.helper
import numpy

import fire
import villain
import display_methods


"""
Taken from https://gamedev.stackexchange.com/questions/105750/pygame-fullsreen-display-issue, without this hack the window is streched out.
"""
import ctypes
ctypes.windll.user32.SetProcessDPIAware()
true_res = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))
pygame.display.set_mode(true_res,pygame.FULLSCREEN)

SIZE = WIDTH, HEIGHT = 1920, 1080

player1 = player.Player(50, 140) # Temporarily declare it as a global variable

pygame.display.init()
infoObject = pygame.display.Info()
# screen = pygame.display.set_mode(SIZE) # , pygame.FULLSCREEN  Temporarily declare it as a global variable
screen = pygame.display.set_mode((0, 0), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE | pygame.FULLSCREEN)

test = brick.Brick(300, 400)
test1 = brick.Brick(100, 350)
test3 = fire.Fire(200, 300)
test4 = villain.Villain(150, 34)
display_methods.make_blocks(screen)

bricks = pygame.sprite.Group(test, test1)
clock = pygame.time.Clock()

def extra_work():
    """
    Move it to another file
    """
    if player1.bullet != None:
        screen.blit(player1.bullet.image, player1.bullet.rect)
        player1.bullet.next_cord()
        if player1.bullet.rect.right >= WIDTH + 30 or player1.bullet.rect.left <= -40:
            player1.shoot = False
            if pygame.sprite.spritecollide(player1.bullet, bricks, False):
                player1.bullet = None
                player1.shoot = False

def game():

    pygame.init()

    background = pygame.image.load(os.path.abspath('assets/game-background-images-10.jpg'))
    # Added clock to limit the frequecy of execution to some fps
    while True:
        # FPS (Frames per second)
        fps = 20

        # Returns a dicitonary with True value for all the keys that are pressed,
        # helps with multiple key presses
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if keys[pygame.K_q]: sys.exit()    # q closes down the window
        player1.player_key_handler(pygame, pygame.event.get(), keys)
        player1.next_cord()

        white = 255, 255, 255
        black = 0, 0, 0
        player1.rect = player1.calc_rect()
        # Draws the current temporary background on to the screen
        screen.blit(background, (0, 0))
        extra_work()


        # Draws the player onto the screen
        display_methods.display_blocks(screen)
        screen.blit(player1.get_player_image(), player1.draw_rect)
        screen.blit(test.image, test.rect)
        screen.blit(test1.image, test1.rect)
        screen.blit(test3.image, test3.rect)

        pygame.draw.rect(screen, (255, 255, 102), test3.rect, 5)
        pygame.draw.circle(screen, (232, 55, 102), (test4.x_cord, test4.y_cord), 50)

        pygame.display.flip()

        clock.tick(fps)

if __name__ == '__main__':
    game()
