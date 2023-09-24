from board import Board
import bfs


class Sokoban:
    def new_board(self, filename):
        e = []
        b = Board(e)
        with open(filename, 'r') as f:
            read_data = f.read()
            lines = read_data.split('\n')
            x = 0
            y = 0
            for line in lines:
                for char in line:
                    if char == 'X':
                        b.add_wall(x, y)
                    elif char == '.':
                        b.add_goal(x, y)
                    elif char == '@':
                        b.set_player(x, y)
                    elif char == '$':
                        b.add_diamond(x, y)
                    elif char == '*':
                        b.add_diamond(x, y)
                        b.add_goal(x, y)
                    x += 1
                y += 1
                x = 0
            return b
            

    def bfs(self, board):
            bfs.search(board)