import sys, pygame, time
import os
import player

def game():
    pygame.init()
    player1 = player.Player(50, 140, 'stand')

    size = width, height = 500, 500

    black = 0, 0, 0

    screen = pygame.display.set_mode(size)
    cowboy_sprite = pygame.image.load(os.path.abspath('assets/cowboy.png'))
    cowboy_sprite = pygame.transform.scale2x(cowboy_sprite)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_LEFT:
                    player1.move_left()
                if event.key == pygame.K_RIGHT:
                    player1.move_right()
        # Fills the screen with black colour
        # TODO: Remove this and add background
        screen.fill(black)

        # The surface object for player 1 cowboy
        player1_surface = pygame.Surface((75, 75))

        # This is the area of image that we want to excerpt from the image cowboy.png
        area_of_image = (player1.sprite_x * 3, player1.sprite_y *3 , 75, 75)
        # Draws the image of cowboy surface object for player 1
        player1_surface.blit(cowboy_sprite, (0, 0), area_of_image)
        # Destination of the image to be drawn on main window
        dest = (player1.x, player1.y)
        # Draws the image that surface player1_surface contains onto the screen
        screen.blit(player1_surface, dest)
        pygame.display.flip()



if __name__ == '__main__':
    game()
