import sys, pygame, time
import os
import player

SIZE = WIDTH, HEIGHT = 500, 500

def game():
    pygame.init()
    player1 = player.Player(0, 140, 'gun-stand')

    white = 255, 255, 255 # TODO: Remove white background and add some background

    screen = pygame.display.set_mode(SIZE)
    cowboy_sprite = pygame.image.load(os.path.abspath('assets/cowboy.png')).convert_alpha()
    # Added clock to limit the frequecy of execution to 50 fps
    clock = pygame.time.Clock()

    while True:
        fps = 10
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q: sys.exit()
        player1.player_key_handler(pygame, event, keys)

        # Fills the screen with white colour
        # TODO: Remove this and add background
        screen.fill(white)
        # The surface object for player 1 cowboy
        player1_surface = pygame.Surface((90, 90))
        player1_surface.fill(white)
        # player1.gravity()

        # This is the area of image that we want to excerpt from the image cowboy.png
        area_of_image = (player1.sprite_x, player1.sprite_y, 45, 45)
        # Draws the image of cowboy surface object for player 1
        player1_surface.blit(cowboy_sprite.convert_alpha() , (0, 0), area_of_image)
        # Scaling the player 1's image
        player1_surface = pygame.transform.scale(player1_surface, (180, 180))
        # Destination of the image to be drawn on main window
        dest = (player1.x, player1.y)

        if player1.left == True:
            player1_surface = pygame.transform.flip(player1_surface, True, False)
            dest = (player1.x - 90, player1.y)

        # Draws the image that surface player1_surface contains onto the screen
        screen.blit(player1_surface.convert_alpha(), dest)
        pygame.display.flip()
        player1.update()
        clock.tick(fps)




if __name__ == '__main__':
    game()
