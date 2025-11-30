import random
import os


stats = "stats_game.txt"

def save_result(winner, board_size):
    with open(stats, "a", encoding="utf-8") as f:
        result = winner if winner else "Ничья"
        f.write(f"Поле {board_size}x{board_size}\n Исход игры: {result}\n")

def show_stats():
    if not os.path.exists(stats):
        print("Статистика пока пуста")
        return
    
    print()
    print("СТАТИСТИКА ИГР")
    print()
    
    with open(stats, "r", encoding="utf-8") as f:
        games = f.readlines()
    
    print(f"Всего игр: {len(games) // 2}")
    
    x_count_win = o_count_win = draws = 0
    for game in games:
        if "X" in game:
            x_count_win += 1
        elif "O" in game:
            o_count_win += 1
        elif "Ничья" in game:
            draws += 1
    
    print(f"Побед X: {x_count_win}")
    print(f"Побед O: {o_count_win}")
    print(f"Ничьих: {draws}")

def board_size():
    while True:
        try:
            size = int(input("Введите размер поля (3-9):"))
            if 3 <= size <= 9:
                return size
            else:
                print("Неверный размер. Попробуйте еще раз")
        except ValueError:
            print("Пожалуйста введите целое число")
            
def empty_board(size):
    board = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append('.')
        board.append(row)
    return board



def game(board, size):
    player = random.choice(['X', 'O'])
    game_over = False
    
    print(f"Первым ходит: {player}")
    while not game_over:
        
        row, col = player_move(board, player, size)
        
        board[row][col] = player
        
        if check_win(board, player, size):
            print_board(board, size)
            print(f"Игрок {player} победил!")
            save_result(player, size)
            game_over = True
        elif game_tie(board, size):
            print_board(board, size)
            print("Борьба была жесткая. НИЧЬЯ!")
            save_result(None, size)
            game_over = True
        else:
            if player == 'X':
                player = 'O'
            else:
                player = 'X'
            
            
    
def check_win(board, player, size):
    for row in range(size):
        if all(board[row][col] == player for col in range(size)):
            return True
        
    for col in range(size):
        if all(board[row][col] == player for row in range(size)):
            return True

    if all(board[i][i] == player for i in range(size)):
        return True
    
    if all(board[i][size - 1 - i] == player for i in range(size)):
        return True
    
    return False
        
def game_tie(board, size):
    for row in range(size):
        for col in range(size):
            if board[row][col] == '.':
                return False
    return True

def player_move(board, player, size):
    while True:
        print_board(board, size)
        try:
            coordinates = input(f"Ход игрока {player}. Введите строку и столбец: ")
            row, col = map(int, coordinates.split())
            
            if not(1 <= row <= size and 1 <= col <= size):
                print(f"Диапазон должен составлять от 1 до {size}")
                continue
            
            row_index = row - 1
            col_index = col - 1
            
            if board[row_index][col_index] != '.':
                print("Извините. Эта клетка уже занята")
                continue
            
            return row_index, col_index
        
        except ValueError:
            print("Нужно ввести два числа через пробел")   

def print_board(board, size):
    print("Текущее поле:")
    for row in board:
        print(' '.join(row))   

def play_again():
    while True:
        answer = input("Хотите сыграть еще раз? (да/нет): ").lower()
        if answer in ['да', 'д', 'yes', 'y']:
            return True
        elif answer in ['нет', 'н', 'no', 'n']:
            return False
        else:
            print("Пожалуйста, введите 'да' или 'нет'")
                        
def main():
    print("------------------------------------------------------------------------")
    print("Добро пожаловать в игру Крестики-Нолики!")
    print("------------------------------------------------------------------------")
    while True:
        print("\n1 - Новая игра")
        print("2 - Показать статистику")
        print("3 - Выйти")
        
        choice = input("Выберите действие: ")

        match choice:
            case "1":
                while True:
                    size = board_size()
                    board = empty_board(size)
                    print(f"Поле размером {size}x{size}:")
                    game(board, size)
                    if not play_again():
                        break
                    print("НОВАЯ ИГРА:")
                    print()
            case "2":
                show_stats()
            case "3":
                print("Спасибо за игру! До свидания!")
                return
            case _:
                print("Неверный выбор. Введите 1, 2 или 3")
main()
