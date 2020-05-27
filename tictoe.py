from IPython.display import clear_output

def zero_record(): #Table reset
    global record
    record = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}

def update_rows(): #Updates table
    global row_one
    global row_two
    global row_thr    
    row_one = [record[7],record[8],record[9]]
    row_two = [record[4],record[5],record[6]]
    row_thr = [record[1],record[2],record[3]]
    
def print_table():
    print(*row_one, sep =' | ')
    print('__|___|__')
    print(*row_two,sep =' | ')
    print('__|___|__')
    print(*row_thr,sep =' | ')
    print('  |   |  ')  

def select_pl(): #SELECT PLAYER
    ch = True
    print('Please enter X or O to choose side you would like to play')
    side = input().upper()
    if side == 'X':
        ch = True
    elif side == 'O' or side == '0':
        ch = False
    else:
        clear_output()
        select_pl()
    return ch

def replay():
    print("Enter 'Yes' to start again.")
    decision = input()
    if decision == "Yes":
          game_start()
    else:
        pass

#win conditions
def win_check():
    if player1 == False:
        win = 'X'
    else:
        win = 'O'
    
    return (
    (record[1] == record[2] == record[3] == win) or
    (record[4] == record[5] == record[6] == win) or
    (record[7] == record[8] == record[9] == win) or
    (record[1] == record[5] == record[9] == win) or
    (record[7] == record[5] == record[3] == win) or
    (record[1] == record[4] == record[7] == win) or
    (record[2] == record[5] == record[8] == win) or
    (record[3] == record[6] == record[9] == win)    )

def game_round():   
    global coordinate
    global record
    global player1
    
    for i in range(1,10):
               
        empty = False
        while not empty:
            try:
                coordinate = int(input(f'Enter cell number (1-9):  '))
                if record[coordinate] == ' ':
                    empty = True
            except:
                print('Incorrect cell number')
                continue
                
        if player1 == True:
            record[coordinate] = 'X'
            player1 = False
        else:
            record[coordinate] = 'O'
            player1 = True
        
        clear_output()
        update_rows()
        print_table()
        
        if win_check() == True:
            if player1 == False:
                print('PLAYER X WINS')
            else:
                print('PLAYER O WINS')
            break
    replay()
    
def game_start(): #initiates game
    global player1
    player1 = select_pl()
    zero_record()

    print(f'Cell numbers are mirrored by Numpad')
    print(' 7 | 8 | 9\n-----------')
    print(' 4 | 5 | 6\n-----------')
    print(' 1 | 2 | 3')

    game_round()

game_start()
