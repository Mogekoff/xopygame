play_array = [' ']*9
moves = 0
player1 = 'X'
player2 = 'O'
who = player1

def print_array():
    for i in 0,3,6:
        print(play_array[i] + ' | ' + play_array[i+1] + ' | ' + play_array[i+2])
        if i == 0 or i == 3:
            print('-'*9)


def move(char,move_cell):
    global moves
    if move_cell >= 0 and move_cell < 9 and play_array[move_cell] == ' ':
        play_array[move_cell] = char
        moves+=1
    else:
        return False
    return True    
        


def checkWin(char):
    if (play_array[0] == char and play_array[1] == char and play_array[2] == char or #xxx
        play_array[3] == char and play_array[4] == char and play_array[5] == char or #ooo
        play_array[6] == char and play_array[7] == char and play_array[8] == char or #xxx
        play_array[0] == char and play_array[4] == char and play_array[8] == char or #x-- -x- --x
        play_array[2] == char and play_array[4] == char and play_array[6] == char or #--x -x- x--
        play_array[0] == char and play_array[3] == char and play_array[6] == char or #o-- o-- o--
        play_array[1] == char and play_array[4] == char and play_array[7] == char or #-o- -o- -o-
        play_array[2] == char and play_array[5] == char and play_array[8] == char):  #--o --o --o
        return True
    else:
        return False


def main():
    global moves
    global who
    while(moves<9):
        try:
            move_cell = int(input('Введите номер клетки хода (1-9): '))
        except ValueError:
            print('Вы ввели неверный номер клетки.')
            continue

        if move(who,move_cell-1):
            print_array()
            if checkWin(who):
                print(f'Игрок {who} победил!')
                return
            if who == player1:
                who = player2
            else:
                who = player1
        else:
            print('Эта клетка уже занята.')
        

if __name__ == '__main__':
    main()