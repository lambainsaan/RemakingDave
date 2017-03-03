import sys, pygame, time
import os
import player

def game():
    pygame.init()
    player1 = player.Player(0, 400, 'stand')

    size = width, height = 850, 500

    black = 0, 0, 0
    # blue  = 12,34,56

    screen = pygame.display.set_mode(size)
    cowboy_sprite = pygame.image.load(os.path.abspath('assets/cowboy.png'))

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                 sys.exit()
                if event.key == pygame.K_LEFT:
                    player1.move_left()
                if event.key == pygame.K_RIGHT:
                    player1.move_right()
                if event.key == pygame.K_UP:
                    player1.move_up()
                if event.key == pygame.K_DOWN:
                    player1.move_down()

        # Fills the screen with black colour
        # TODO: Remove this and add background
        screen.fill(black)

        # The surface object for player 1 cowboy
        player1_surface = pygame.Surface((45, 45))

        # This is the area of image that we want to excerpt from the image cowboy.png
        area_of_image = (player1.sprite_x, player1.sprite_y, 45, 45)
        # Draws the image of cowboy surface object for player 1
        player1_surface.blit(cowboy_sprite, (0, 0), area_of_image)
        # Destination of the image to be drawn on main window
        dest = (player1.x, player1.y)
        # Draws the image that surface player1_surface contains onto the screen
        screen.blit(player1_surface, dest)
        pygame.display.flip()



if __name__ == '__main__':
    game()
