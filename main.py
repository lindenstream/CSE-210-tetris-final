import pygame
import constants
from tetris import Tetris

def main():
    # Initialize the game engine
    pygame.init()

    # set window display size
    screen_width = 400
    screen_height = 500
    size = (screen_width, screen_height)
    screen = pygame.display.set_mode(size)

    # set window title
    pygame.display.set_caption("Tetris - CSE-210 Final Project")

    # set up the game
    done = False
    clock = pygame.time.Clock()
    fps = 25
    game = Tetris(20, 10)
    counter = 0

    pressing_down = False

    # while loop to keep the game going
    while not done:
        if game.figure is None:
            game.new_figure()
        counter += 1
        if counter > 100000:
            counter = 0

        if counter % (fps // game.level // 2) == 0 or pressing_down:
            if game.state == "start":
                game.go_down()

        # manage key press events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.rotate()
                if event.key == pygame.K_DOWN:
                    pressing_down = True
                if event.key == pygame.K_LEFT:
                    game.go_side(-1)
                if event.key == pygame.K_RIGHT:
                    game.go_side(1)
                if event.key == pygame.K_SPACE:
                    game.go_space()
                if event.key == pygame.K_ESCAPE:
                    game.__init__(20, 10)

        if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    pressing_down = False

        # set the window background color
        screen.fill(constants.BLACK)

        # draw a grid on the screen
        for i in range(game.height):
            for j in range(game.width):
                pygame.draw.rect(screen, constants.GRAY, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
                if game.field[i][j] > 0:
                    pygame.draw.rect(screen, constants.COLORS[game.field[i][j]],
                                    [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

        # draws the pieces on the game screen
        if game.figure is not None:
            for i in range(4):
                for j in range(4):
                    p = i * 4 + j
                    if p in game.figure.image():
                        pygame.draw.rect(screen, constants.COLORS[game.figure.color],
                                        [game.x + game.zoom * (j + game.figure.x) + 1,
                                        game.y + game.zoom * (i + game.figure.y) + 1,
                                        game.zoom - 2, game.zoom - 2])

        # set font attributes for score and game over text
        font = pygame.font.SysFont('Tahoma', 15, True, False)
        font1 = pygame.font.SysFont('Tahoma', 45, True, False)
        font3 = pygame.font.SysFont('Tahoma', 25, True, False)
        score_text = font3.render("Score: " + str(game.score), True, constants.WHITE)
        single_text = font.render("Single x " + str(game.single), True, constants.WHITE)
        double_text = font.render("Double x " + str(game.double), True, constants.WHITE)
        triple_text = font.render("Triple x " + str(game.triple), True, constants.WHITE)
        tetris_text = font.render("Tetris x " + str(game.quad), True, constants.WHITE)
        text_game_over = font1.render("Game Over", True, constants.WHITE)
        text_game_over1 = font.render("Press ESC to Start a New Game", True, constants.WHITE)

        # print text to display
        screen.blit(score_text, [0, 0])
        screen.blit(single_text, [0, 35])
        screen.blit(double_text, [0, 55])
        screen.blit(triple_text, [0, 75])
        screen.blit(tetris_text, [0, 95])
        if game.state == "gameover":
            screen.blit(text_game_over, [screen_width/2 - 128, 200])
            screen.blit(text_game_over1, [screen_width/2 - 115, 265])

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()

# call to main to start the program
main()