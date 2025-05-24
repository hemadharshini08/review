from tkinter import *
from PIL import ImageTk ,Image

base = Tk()
base.title('Start Button')
base.geometry("700x350")

img=ImageTk.PhotoImage(Image.open ("D:/nature.jpg"))
lab=Label(image=img)
lab.pack()

button=Button(base,text='exit',command=base.quit)
button.pack()
base.mainloop()