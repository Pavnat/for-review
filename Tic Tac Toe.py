{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  |   | X\n",
      "__|___|__\n",
      "O | X | O\n",
      "__|___|__\n",
      "X | O | X\n",
      "  |   |  \n",
      "PLAYER X WINS\n",
      "Enter 'Yes' to start again.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " n\n"
     ]
    }
   ],
   "source": [
    "from IPython.display import clear_output\n",
    "\n",
    "def zero_record(): #Table reset\n",
    "    global record\n",
    "    record = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}\n",
    "\n",
    "def update_rows(): #Updates table\n",
    "    global row_one\n",
    "    global row_two\n",
    "    global row_thr    \n",
    "    row_one = [record[7],record[8],record[9]]\n",
    "    row_two = [record[4],record[5],record[6]]\n",
    "    row_thr = [record[1],record[2],record[3]]\n",
    "    \n",
    "def print_table():\n",
    "    print(*row_one, sep =' | ')\n",
    "    print('__|___|__')\n",
    "    print(*row_two,sep =' | ')\n",
    "    print('__|___|__')\n",
    "    print(*row_thr,sep =' | ')\n",
    "    print('  |   |  ')  \n",
    "\n",
    "def select_pl(): #SELECT PLAYER\n",
    "    ch = True\n",
    "    print('Please enter X or O to choose side you would like to play')\n",
    "    side = input().upper()\n",
    "    if side == 'X':\n",
    "        ch = True\n",
    "    elif side == 'O' or side == '0':\n",
    "        ch = False\n",
    "    else:\n",
    "        clear_output()\n",
    "        select_pl()\n",
    "    return ch\n",
    "\n",
    "def replay():\n",
    "    print(\"Enter 'Yes' to start again.\")\n",
    "    decision = input()\n",
    "    if decision == \"Yes\":\n",
    "          game_start()\n",
    "    else:\n",
    "        pass\n",
    "\n",
    "#win conditions\n",
    "def win_check():\n",
    "    if player1 == False:\n",
    "        win = 'X'\n",
    "    else:\n",
    "        win = 'O'\n",
    "    \n",
    "    return (\n",
    "    (record[1] == record[2] == record[3] == win) or\n",
    "    (record[4] == record[5] == record[6] == win) or\n",
    "    (record[7] == record[8] == record[9] == win) or\n",
    "    (record[1] == record[5] == record[9] == win) or\n",
    "    (record[7] == record[5] == record[3] == win) or\n",
    "    (record[1] == record[4] == record[7] == win) or\n",
    "    (record[2] == record[5] == record[8] == win) or\n",
    "    (record[3] == record[6] == record[9] == win)    )\n",
    "\n",
    "def game_round():   \n",
    "    global coordinate\n",
    "    global record\n",
    "    global player1\n",
    "    \n",
    "    for i in range(1,10):\n",
    "               \n",
    "        empty = False\n",
    "        while not empty:\n",
    "            try:\n",
    "                coordinate = int(input(f'Enter cell number (1-9):  '))\n",
    "                if record[coordinate] == ' ':\n",
    "                    empty = True\n",
    "            except:\n",
    "                print('Incorrect cell number')\n",
    "                continue\n",
    "                \n",
    "        if player1 == True:\n",
    "            record[coordinate] = 'X'\n",
    "            player1 = False\n",
    "        else:\n",
    "            record[coordinate] = 'O'\n",
    "            player1 = True\n",
    "        \n",
    "        clear_output()\n",
    "        update_rows()\n",
    "        print_table()\n",
    "        \n",
    "        if win_check() == True:\n",
    "            if player1 == False:\n",
    "                print('PLAYER X WINS')\n",
    "            else:\n",
    "                print('PLAYER O WINS')\n",
    "            break\n",
    "    replay()\n",
    "    \n",
    "def game_start(): #initiates game\n",
    "    global player1\n",
    "    player1 = select_pl()\n",
    "    zero_record()\n",
    "\n",
    "    print(f'Cell numbers are mirrored by Numpad')\n",
    "    print(' 7 | 8 | 9\\n-----------')\n",
    "    print(' 4 | 5 | 6\\n-----------')\n",
    "    print(' 1 | 2 | 3')\n",
    "\n",
    "    game_round()\n",
    "\n",
    "game_start()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}