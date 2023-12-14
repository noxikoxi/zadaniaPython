import random
import tkinter as tk
from tkinter import ttk  # themed widgets

WIDTH, HEIGHT = 490, 300
BUTTON_WIDTH, BUTTON_HEIGHT = 22, 6

root = tk.Tk()
root.resizable(False, False)
root.geometry(f'{WIDTH}x{HEIGHT}')
root.title('rock_paper_scissors')


def play(choice):
    opponent = random.choice(['rock', 'paper', 'scissors'])
    opponentChoice['text'] = f'{opponent}'
    yourChoice['text'] = f'{choice}'
    if ((choice == 'rock' and opponent == 'scissors') or
            (choice == 'paper' and opponent == 'rock') or
            (choice == 'scissors' and opponent == 'paper')):
        winning['text'] = "You Won"

        t_splitted = statisticsValue['text'].split('/')
        statisticsValue['text'] = f'{int(t_splitted[0])+1}/{t_splitted[1]}/{t_splitted[2]}'
    elif choice == opponent:
        winning['text'] = "Draw"
        t_splitted = statisticsValue['text'].split('/')
        statisticsValue['text'] = f'{t_splitted[0]}/{t_splitted[1]}/{int(t_splitted[2])+1}'
    else:
        winning['text'] = "You Lost"
        t_splitted = statisticsValue['text'].split('/')
        statisticsValue['text'] = f'{t_splitted[0]}/{int(t_splitted[1])+1}/{t_splitted[2]}'


frameUpper = tk.Frame(root)

rock = tk.Button(frameUpper, text="rock", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=lambda: play('rock'))
rock.grid(row=1, column=0)

paper = tk.Button(frameUpper, text="paper", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=lambda: play('paper'))
paper.grid(row=1, column=1)

scissors = tk.Button(frameUpper, text="scissors", width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                     command=lambda: play('scissors'))
scissors.grid(row=1, column=2)


winning = ttk.Label(root, text="Press button to play...", font='Times 20 bold')
winning.grid(row=2)

yourChoiceLabel = ttk.Label(root, text="Your Choice:", font='Times 18')
yourChoiceLabel.grid(row=3, column=0, sticky=tk.W)

yourChoice = ttk.Label(root, text="", font='Times 20 italic')
yourChoice.grid(row=3, column=0)

opponentChoice = ttk.Label(root, text="Opponent Choice:", font='Times 18')
opponentChoice.grid(row=4, column=0, sticky=tk.W)

opponentChoice = ttk.Label(root, text="", font='Times 20 italic')
opponentChoice.grid(row=4, column=0)

statistics = ttk.Label(root, text="Statistics(W,L,D):", font='Times 16')
statistics.grid(row=5, column=0, sticky=tk.W)

statisticsValue = ttk.Label(root, text="0/0/0", font='Times 18')
statisticsValue.grid(row=5, column=0)

frameUpper.grid(row=1)
root.mainloop()
