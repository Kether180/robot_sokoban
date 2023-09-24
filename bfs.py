from copy import deepcopy


def print_results(board):
    print("Solution: " + board.getDirections())


def search(board):
    if board.is_win():
        print_results(board)
        return board
    initial_node = deepcopy(board)  # copy of initial node
    frontier = []  # a list used as a queue that will act as a stack
    frontier.append(initial_node)
    explored = set()  # a set to keep track of states already evaluated.
    keep_searching = True
    while keep_searching:
        if len(frontier) == 0:
            print("Solution not found")
            return
        else:  # if there are still nodes to explore, it takes the latest board from frontier
            current_node = frontier.pop()
            # adds the current state to the explored set
            moves = current_node.moves_available()
            current_node.fdiamonds = frozenset(current_node.diamonds)
            explored.add(current_node)
# earch continues in this manner, exploring deeper into the game tree before backtracking,DFS
            for move in moves:
                child_node = deepcopy(current_node)
                child_node.move(move)
                if child_node not in explored:
                    if child_node.is_win():
                        print_results(child_node)
                        return child_node
                    frontier.append(child_node) ## new nodes are added to the back.

