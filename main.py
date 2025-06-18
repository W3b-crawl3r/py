import pygame
from game import *
from database import create_tables
from database import save_match

pygame.init()
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moroccan Checkers")

FPS = 60

def main():
    create_tables()

    print("Welcome to Moroccan Checkers!")
    print("1 - Player vs Player")
    print("2 - Player vs AI")
    mode = input("Select game mode (1 or 2): ")
    ai_mode = mode.strip() == '2'

    player1 = input("Enter Player 1 name: ")
    player2 = "AI" if ai_mode else input("Enter Player 2 name: ")

    clock = pygame.time.Clock()
    game = Game(WIN, is_ai=ai_mode)

    run = True
    while run:
        clock.tick(FPS)

        if game.turn == 'black' and ai_mode:
            game.ai_move()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = pos[1] // game.SQUARE_SIZE, pos[0] // game.SQUARE_SIZE
                game.select(row, col)

        game.update()

        winner = game.check_winner()
        if winner:
            save_match(player1, player2, winner)
            print(f"{winner} wins!")
            run = False

    pygame.quit()

if __name__ == '__main__':
    main()
