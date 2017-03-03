import sys, pygame, time
import os
import player

def game():
    pygame.init()
    player1 = player.Player(0, 140, 'gun-stand')

    size = width, height = 500, 500

    black = 0, 0, 0

    screen = pygame.display.set_mode(size)
    cowboy_sprite = pygame.image.load(os.path.abspath('assets/cowboy.png'))

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q and player1.y<500:
                    sys.exit()
                elif event.key == pygame.K_LEFT and player1.x>0:
                    player1.direction = 'left'                  #set direction of player left  
                elif event.key == pygame.K_RIGHT:
                    player1.direction = 'right'
                elif event.key == pygame.K_UP:
                    player1.direction = 'up'
                elif event.key == pygame.K_DOWN:
                    player1.direction = 'down'
            
            elif event.type == pygame.KEYUP:
                player1.direction = 'None'   #if key is not pressed then direction will be set to none that is player will not move.
        
        if player1.direction == 'right':
            player1.move_right()    #if player1.direction  is right then move player right
        elif player1.direction == 'left':
            player1.move_left()
        elif player1.direction == 'up':
        	player1.move_up()
        elif player1.direction == 'down':
        	player1.move_down()
            
        # Fills the screen with black colour
        # TODO: Remove this and add background
        screen.fill(black)

        # The surface object for player 1 cowboy
        player1_surface = pygame.Surface((90, 90))

        # This is the area of image that we want to excerpt from the image cowboy.png
        area_of_image = (player1.sprite_x, player1.sprite_y, 45, 45)
        # Draws the image of cowboy surface object for player 1
        player1_surface.blit(cowboy_sprite, (0, 0), area_of_image)
        # Scaling the player 1's image
        player1_surface = pygame.transform.scale(player1_surface, (180, 180))
        # Destination of the image to be drawn on main window
        dest = (player1.x, player1.y)
        # Draws the image that surface player1_surface contains onto the screen
        screen.blit(player1_surface, dest)
        pygame.display.flip()



if __name__ == '__main__':
    game()
