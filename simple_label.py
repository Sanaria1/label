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

***********************************
To add an image to the label: 
  
  
from tkinter import *



window = Tk()

photo = PhotoImage(file= "Python") #put the image path in this section " " 

label = Label(window,
              text="Hello Python",
              font=("Aril", 40, "bold"),
              fg="pink",
              bg="black",
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound="bottom") #to place the image in the bottom of the label. 
label.pack()
#label.place(x=0,y=0) 

window.mainloop()
  
  
