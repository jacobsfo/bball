#part1
import random
import time
# map each letter to the move using a map
import tkinter as tk
from tkinter import messagebox
multiarr=[]
def generate_permutations(arr, current, used, L,multiarr):
    #if curr seq = length L print sequence
    if len(current)==L:
        multiarr.append(current.copy())
        return

    for i in range(len(arr)):
        if(used[i]):
            continue
        used[i]=True
        current.append(arr[i])
        generate_permutations(arr,current,used,L,multiarr)
        used[i]=False
        current.pop()
#scene function
'''
    
    scene2:
    create a gui interface(Tk)
    output each combo to gui
    set counter for 32 seconds for each combo
    update interface to next combo
    return to scene1 after all combos are displayed
'''
combo_index = 0
move_index = 0
def show_next_move(self):
    # Get the current combo and move
    current_combo = multiarr[combo_index]
    current_move = current_combo[move_index]
    
    # Update the label to display the current move
    label = tk.Label(root, text=current_move, font=("Helvetica", 16))
    label.pack(pady=20)

    
    # Update indices for next move
    move_index += 1
    
    # If we have shown all moves in the current combo, move to the next combo
    if move_index >= len(current_combo):
        move_index = 0
        combo_index += 1
    
    # If we have shown all combos, start again from the first combo
    if combo_index >= len(multiarr):
        combo_index = 0
    
    # Schedule the next move to display after 8000 milliseconds (8 seconds)
    root.after(8000, self.show_next_move)

def singleplayer():
    root=tk.Tk()
    root.title("Game Scene")
    root.geometry("800x800")
    # Create a label widget
    show_next_move()
   

    
    button3 = tk.Button(root, text="Quit", command=root.quit, width=15, height=2)
    button3.pack(pady=10)
    root.mainloop()

class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Scene")
        self.root.geometry("800x800")
        
        # Initialize variables
        self.combo_index = 0
        self.move_index = 0
        
        # Label to display the moves
        self.label = tk.Label(self.root, text="", font=("Helvetica", 24))
        self.label.pack(pady=50)
        
        # Quit button
        self.button_quit = tk.Button(self.root, text="Quit", command=self.root.quit, width=15, height=2)
        self.button_quit.pack(pady=20)
        
        # Start the move display
        self.show_next_move()

    def show_next_move(self):
        # Get the current combo and move
        current_combo = multiarr[self.combo_index]
        current_move = current_combo[self.move_index]
        
        # Update the label to display the current move
        self.label.config(text=current_move)
        
        # Update indices for next move
        self.move_index += 1
        
        # If we have shown all moves in the current combo, move to the next combo
        if self.move_index >= len(current_combo):
            self.move_index = 0
            self.combo_index += 1
        
        # If we have shown all combos, start again from the first combo
        if self.combo_index >= len(multiarr):
            self.combo_index = 0
        
        # Schedule the next move to display after 8000 milliseconds (8 seconds)
        self.root.after(8000, self.show_next_move)

# Start screen to launch the GameApp on button click
def main():
    arr=["LAYUP","FLOATER","MIDDY","THREE"]
    L=4
    current=[]
    used=[False]*len(arr)
# get all combos of [l,m,f,t] and store them in a 2d array
    generate_permutations(arr,current,used,L,multiarr)
# shuffle array and then using the map display each move in a gui
    random.shuffle(multiarr)
    
    '''
    scene1:
    start
    quit
    '''

    root=tk.Tk()
    root.title("Home Scene")
    # Create a label widget
    label = tk.Label(root, text="Welcome to the Home Screen", font=("Helvetica", 16))
    label.pack(pady=20)

   

   # Start Game button
    start_button = tk.Button(root, text="Start Game", command=lambda: start_game(root), width=15, height=2)
    start_button.pack(pady=20)

    button3 = tk.Button(root, text="Exit", command=root.quit, width=15, height=2)
    button3.pack(pady=10)

    # Start the GUI event loop
    root.mainloop()
   

def start_game(root):
    # Close the start screen window
    root.destroy()
    
    # Create a new window for the game
    game_window = tk.Tk()
    
    # Instantiate the GameApp in the new window
    app = GameApp(game_window)
    
    # Start the game event loop
    game_window.mainloop()

        
    
        
if __name__ == "__main__":
    main()