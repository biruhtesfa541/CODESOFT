import math
import random

def table_printer(table):
    for row in table:
        print(" | ".join(row))
        print("-" * 9)

def identify_the_winner(table, player):
    #identifying rows and columns
    for i in range(3):
        identify_rows= True
        identify_columns=True
        for j in range(3):
            if table[i][j] != player:
                identify_rows = False
            if table[j][i] != player:
                identify_columns = False
        if identify_rows or identify_columns:
            return True
    #identify diagonals
    identify_dig1 = True
    identify_dig2 = True
    for i in range(3):
        if table[i][i] != player:
            identify_dig1 = False
        if table[i][2 - i] != player:
            identify_dig2 = False
    if identify_dig1 or identify_dig2:
        return True
    return False

def is_it_full(table):
    for row in table:
        for cell in row:
            if cell == " ":
                return False
    return True

def ai_minimax(table, depth, is_maximizing, alpha, beta):
    if identify_the_winner(table, "X"):
        return -1
    if identify_the_winner(table, "O"):
        return 1
    if is_it_full(table):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if table[i][j] == " ":
                    table[i][j] = "O"
                    score = ai_minimax(table, depth + 1, False, alpha, beta)
                    table[i][j] = " "
                    best_score = max(score, best_score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if table[i][j] == " ":
                    table[i][j] = "X"
                    score = ai_minimax(table, depth + 1, True, alpha, beta)
                    table[i][j] = " "
                    best_score = min(score, best_score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score

def ai_best_move(table):
    best_score = -math.inf
    moves = []
    for i in range(3):
        for j in range(3):
            if table[i][j] == " ":
                table[i][j] = "O"
                score = ai_minimax(table, 0, False, -math.inf, math.inf)
                table[i][j] = " "
                if score > best_score:
                    best_score = score
                    moves = [(i, j)]
                elif score == best_score:
                    moves.append((i, j))
    return random.choice(moves)

def tic_tac_toe():
    table = [[" "] * 3 for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    
    while True:
        table_printer(table)
        player = players[turn % 2]
        print(f"Player {player}'s turn.")
        
        if player == "X":
            try:
                row, col = map(int, input("Enter row and column (0-2) separated by space: ").split())
                if table[row][col] != " ":
                    print("Cell already occupied. Try again.")
                    continue
            except (ValueError, IndexError):
                print("Invalid input. Enter numbers between 0 and 2.")
                continue
        else:
            print("AI (O) is thinking...")
            row, col = ai_best_move(table)
        
        table[row][col] = player
        
        if identify_the_winner(table, player):
            table_printer(table)
            print(f"Player {player} wins!")
            break
        
        if is_it_full(table):
            table_printer(table)
            print("It's a draw!")
            break
        
        turn += 1

tic_tac_toe()