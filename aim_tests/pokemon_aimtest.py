from tkinter import *
import  random
from tkinter.ttk import *
from PIL import Image, ImageTk
complexity=5
root=Tk()
root.geometry("1500x800")
root.config(cursor="target")
style = Style()
counter=0
win=False


def selectingImage():
    global photo
    files=["avion.png","default.png","dragon.png"]
    image = Image.open("G:/teo/Programacion/python/modules/aim_tests/"+ random.choice(files))
    resized_photo=image.resize((15*complexity,15*complexity))
    photo=ImageTk.PhotoImage(resized_photo)
style.configure('W.TButton', font = ('Verdana', 10, 'bold', 'underline'),foreground = 'red')

def increment_counter(event):
    global counter
    global complexity
    global win
    counter+=1
    displayed_counter.config(text="Contador: "+ str(counter))
    print(counter)
    button.destroy()
    if (counter%4)==0:
        complexity=complexity-1
        print(complexity)    
    if (complexity==1):
        exit()
    selectingImage()
    gen_but(photo)


def gen_but(photo):
    global button
    button =Button(root, text="image", image = photo)
    button.grid(row = int(random.random()*15)+2, column =int(random.random()*10)+2, pady=random.random()*800, padx=random.random()*1500)
    button.bind("<Button-1>", increment_counter)

text=Label(root, text="Toca AL Pokemon!", style="W.TButton")

text.place(relx = 0.5, rely = 0.02,anchor = 'center')
displayed_counter=Label(root, text="Contador: "+ str(counter), style="W.TButton")
displayed_counter.place(relx = 0.5, rely = 0.06,anchor = 'center')

selectingImage()
gen_but(photo)

displayed_counter.mainloop()