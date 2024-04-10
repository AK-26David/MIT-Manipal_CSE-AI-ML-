import random

def generate_random_board():
    """ Generate a random board configuration """
    return [random.randint(0, 7) for _ in range(8)]

def calculate_cost(board):
    """ Calculate the number of attacking pairs of queens """
    cost = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] == board[j] or abs(i - j) == abs(board[i] - board[j]):
                cost += 1
    return cost

def get_next_board(board):
    """ Generate all possible next board configurations """
    next_boards = []
    for col in range(8):
        for row in range(8):
            if board[col] != row:
                new_board = list(board)
                new_board[col] = row
                next_boards.append(new_board)
    return next_boards

def hill_climbing():
    """ Solve the 8 queens problem using hill climbing """
    current_board = generate_random_board()
    current_cost = calculate_cost(current_board)
    
    while current_cost > 0:
        next_boards = get_next_board(current_board)
        next_costs = [calculate_cost(board) for board in next_boards]
        
        min_cost = min(next_costs)
        if min_cost >= current_cost:
            break  # stuck at local minima
        
        # Move to the board that has the minimum cost
        min_index = next_costs.index(min_cost)
        current_board = next_boards[min_index]
        current_cost = min_cost
    
    return current_board

def print_board(board):
    """ Print the board configuration """
    for row in range(8):
        line = ""
        for col in range(8):
            if board[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

if __name__ == "__main__":
    solution = hill_climbing()
    print("Solution found:")
    print_board(solution)
