import sys, pygame, time
import os
import objects.brick as brick
import objects.player as player
import objects.helper

SIZE = WIDTH, HEIGHT = 500, 500

test = brick.Brick(300, 400)
test1 = brick.Brick(100, 350)
bricks = pygame.sprite.Group(test, test1)
clock = pygame.time.Clock()

def game():
    pygame.init()
    player1 = player.Player(50, 140)

    screen = pygame.display.set_mode(SIZE)
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

        player1.player_key_handler(pygame, event, keys)
        player1.next_cord()

        white = 255, 255, 255
        black = 0, 0, 0
        player1.rect = player1.calc_rect()
        # Draws the current temporary background on to the screen
        screen.blit(background, (0, 0))
        if player1.bullet != None:
            screen.blit(player1.bullet.image, player1.bullet.rect)
            player1.bullet.next_cord()
            if player1.bullet.rect.right >= WIDTH + 30 or player1.bullet.rect.left <= -40:
                player1.shoot = False
            if pygame.sprite.spritecollide(player1.bullet, bricks, False):
                player1.bullet = None
                player1.shoot = False

        # Draws the player onto the screen
        screen.blit(player1.get_player_image(), player1.draw_rect)
        screen.blit(test.image, test.rect)
        screen.blit(test1.image, test1.rect)
        pygame.display.flip()

        clock.tick(fps)



if __name__ == '__main__':
    game()
