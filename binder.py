import sys, pygame, time
import os
import player

SIZE = WIDTH, HEIGHT = 500, 500

def game():
    pygame.init()
    player1 = player.Player(0, 140, 'gun-stand')

    white = 255, 255, 255 # TODO: Remove white background and add some background

    screen = pygame.display.set_mode(SIZE)
    background = pygame.image.load(os.path.abspath('assets/game-background-images-10.jpg'))
    # Added clock to limit the frequecy of execution to some fps
    clock = pygame.time.Clock()
    # Width of each individual sprite

    while True:
        # FPS (Frames per second)
        fps = 20

        # Returns a dicitonary with True value for all the keys that are pressed,
        # helps with multiple key presses

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if keys[pygame.K_q]: sys.exit()
        player1.player_key_handler(pygame, event, keys)

        # Draws the current temporary background on to the screen
        screen.blit(background, (0, 0))
        # Draws the player onto the screen
        screen.blit(player1.get_player_image(), player1.player_position())
        pygame.display.flip()
        player1.update()
        clock.tick(fps)




if __name__ == '__main__':
    game()
