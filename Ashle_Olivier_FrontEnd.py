from tkinter import *
import Ashle_Olivier_Backend as bck
root=Tk()

mylabel= Label(root, text='Your voice assitant',font='Helvetica 18 bold')
#Botton is red because red can be best seen by the visually impared 
#https://visionaware.org/everyday-living/home-modification/contrast-and-color/#:~:text=Bright%20colors%20are%20generally%20the,usually%20more%20visible%20than%20pastels.
mybotton= Button(root, text='Play',height= 8, width=30,font='Helvetica 15 bold',bg='RED',activebackground='GREEN',command=lambda :bck.Take_query())

mylabel.pack()

mybotton.pack()
root.geometry("800x600")
mybotton.place(x=200, y=200)
root.resizable(False, False)
def disable_event():
   pass


root.protocol("WM_DELETE_WINDOW", disable_event)
root.mainloop()