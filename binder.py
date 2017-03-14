import sys, pygame, time
import os
import player.player as player, brick

SIZE = WIDTH, HEIGHT = 500, 500

def game():
    pygame.init()
    player1 = player.Player(0, 140)

    screen = pygame.display.set_mode(SIZE)
    background = pygame.image.load(os.path.abspath('assets/game-background-images-10.jpg'))
    # Added clock to limit the frequecy of execution to some fps
    clock = pygame.time.Clock()
    # Width of each individual sprite

    test = brick.Brick(300, 415)
    test1 = brick.Brick(150, 350)
    bricks = pygame.sprite.Group(test, test1)
    s = 1
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
        white = 255, 255, 255
        # screen.fill(white, rect = player1.rect)
        screen.blit(player1.get_player_image(), player1.draw_rect)
        screen.blit(test.image, test.rect)
        screen.blit(test1.image, test1.rect)
        pygame.display.flip()
        player1.jump_equation()

        # for collide in pygame.sprite.spritecollide(player1, bricks, False):




                # player1.dy != 7 is a hack that I got by tweaking in the code,
                # if someone can make it concrete please take up this issue
        #         if player1.action == 'jump' and player1.dy != 7:
        #             print('Hi')
        #             player1.break_jump(collide.rect.top)
        # s += 1
        # if not player1.on_top_of_brick() and not player1.is_jump:
        #     player1.go_down()
        #     if player1.draw_rect.bottom >= HEIGHT:
        #         player1.break_jump(HEIGHT)
        #         print('lol')

        clock.tick(fps)



if __name__ == '__main__':
    game()
