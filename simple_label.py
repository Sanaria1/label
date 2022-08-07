from tkinter import *

window = Tk()

label = Label(window,
              text="Hello Python",
              font=("Aril", 40, "bold"),
              fg="pink",
              bg="black", relief=RAISED,
              bd=10,
              padx=20,
              pady=20)
label.pack()
#label.place(x=0,y=1)

window.mainloop()
