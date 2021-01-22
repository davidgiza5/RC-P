#interfata pentr files browsing

from tkinter import *
from tkinter import filedialog
def selectfile():
    numefisier = filedialog.askopenfilename(initialdir="/", title="Selecteaza un fisier",filetypes=(("Text files","*.txt*"),("all files","*.*")))


    label_file_explorer.configure(text="Fisier deschis: " + numefisier)

window = Tk()

window.title('Gestionare fisiere')

window.geometry("500x500")

window.config(background="white")

label_file_explorer = Label(window, text="Browser FS", width=100, height=4, fg="red")

button_explore = Button(window, text="Cauta un fisier", command=selectfile)

button_exit = Button(window, text="Iesire", command=exit)

label_file_explorer.grid(column=1, row=1)

button_explore.grid(column=1, row=2)

button_exit.grid(column=1, row=3)

window.mainloop()