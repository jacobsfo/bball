#part1
import random
# map each letter to the move using a map
import tkinter as tk

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
def createscene():
    root=tk.Tk()
    root.title("Tkinter Scene")
def main():
    arr=["LAYUP","FLOATER","MIDDY","THREE"]
    L=4
    current=[]
    multiarr=[]
    used=[False]*len(arr)
# get all combos of [l,m,f,t] and store them in a 2d array
    generate_permutations(arr,current,used,L,multiarr)
# shuffle array and then using the map display each move in a gui
    random.shuffle(multiarr)
    print(multiarr)
    '''
    scene1:
    start
    quit
    scene2:
    create a gui interface(Tk)
    output each combo to gui
    set counter for 32 seconds for each combo
    update interface to next combo
    return to scene1 after all combos are displayed
    '''


        
    
        
if __name__ == "__main__":
    main()