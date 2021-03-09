from game import Game

game = Game()
game.print_board()

while not game.check_finished():
    move = input('Enter the coordinates: ').split()

    if not game.make_move(move):
        continue

    game.print_board()
