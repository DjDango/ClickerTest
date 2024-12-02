from tkinter import *
count = 0

def click():
  count +=1

root = Tk()
root.size(500x500)
root.title('ClickerTest')

Lbl = Label(root, font=('Monospace'), 50, fg='black', bg='white', text=count)
Lbl.pack()

root.mainloop()


