#Podle tutorialu https://www.youtube.com/watch?v=nbRpDXV7QDM
import tkinter as tk

def set_tile(row, column):
    global curr_player

    if (game_over):
        return

    if board[row][column]["text"] != "":
        return
    
    board[row][column]["text"] = curr_player
    
    if curr_player == playerO:
        curr_player = playerX
    else:
        curr_player = playerO
    
    label["text"] = curr_player+"'s turn"

    check_winner()

def check_winner():
    global turns, game_over
    turns += 1

    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] 
            and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"]+" is the winner", foreground=color_yellow)
            for column in range (3):
                board[row][column].config(foreground=color_yellow)
            game_over = True
            return
    
    for column in range (3):
        if (board[0][column]["text"] == board [1][column]["text"] ==board[2][column]["text"]
            and board [0][column]["text"] != ""):
            label.config(text=board[0][column]["text"]+" is the winner, foreground=color_yellow")
            for column in range (3):
                board[row][column].config(foreground=color_yellow)
            game_over = True
            return

def new_game():
    pass
    
playerX = "X"
playerO = "O"
curr_player = playerX
board = [[0, 0, 0], 
         [0, 0, 0], 
         [0, 0, 0]]

color_black = "#000000"
color_dark_blue = "#123CF8"
color_yellow = "#DAFD15"
color_light_blue = "#ADD8E6"

turns = 0
game_over = False

#window
window = tk.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tk.Frame(window)
label = tk.Label(frame, text=curr_player+"'s turn", font=("Calibri", 20), background=color_black, foreground="white")

label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tk.Button(frame, text="", font=("Calibri", 50, "bold"), background=color_black, foreground=color_dark_blue, width=4, height=1, command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1,column=column)

button = tk.Button(frame, text="restart", font=("Calibri", 20), background=color_black, foreground="white", command=new_game)
button.grid(row=4, column=0, columnspan = 3, sticky="we")

frame.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()


window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

"format (h)x(w)+(x)+(y)"

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")


window.mainloop()