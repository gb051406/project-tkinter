import tkinter as tk
from PIL import ImageTk, Image
import os
#functions
def compute():
    try:
        tanAcc = (float(txtRadius.get()))*(float(txtAcc.get())) #calculations
        centrip = (float(txtSpeed.get())**2)/(float(txtRadius.get()))
        lblSolutionOne.config(text="Tangential Acceleration = "+str(tanAcc)) #changes solution text to solution
        lblSolutionTwo.config(text="Centripetal Acceleration = "+str(centrip))
    except ValueError: #allows for no stopage when entering letters, not numbers
        lblSolutionOne.config(text="ERROR: enter only numbers")
#window config
canvas = tk.Tk()
canvas.geometry("630x460")
canvas.title("something")
canvas.config(bg = "light blue")
canvas.iconbitmap("physics.ico")#title image for window

#labels
lblTitle = tk.Label(canvas, text="Accelerations Converter")
lblDirections = tk.Label(canvas, text="Enter the radius length, the angular acceleration, and the speed of a rotating object")
lblRadius = tk.Label(canvas, text="Enter radius of the circle:")
lblVelocity = tk.Label(canvas, text="Enter angular velocity:")
lblAcceleration = tk.Label(canvas, text="Enter angular acceleration:")
lblSolutionOne = tk.Label(canvas, text="")
lblSolutionTwo = tk.Label(canvas, text="")

#text
txtRadius = tk.Entry(canvas)
txtSpeed = tk.Entry(canvas)
txtAcc = tk.Entry(canvas)

#button
btnCalc = tk.Button(canvas, text="Calculate", command=compute)

#image add
photo = ImageTk.PhotoImage(file="centripetal.jpg")
image = tk.Label(canvas, image=photo)
image.grid(row=7, column=1,padx=10)
#GUI

lblTitle.grid(row=0,column=0,padx=10,pady=10)
lblDirections.grid(row=0,column=1,padx=10,pady=10)
lblRadius.grid(row=2,column=0,padx=10,pady=10)
txtRadius.grid(row=2,column=1,padx=10,pady=10)
lblVelocity.grid(row=3,column=0,padx=10,pady=10)
txtSpeed.grid(row=3,column=1,padx=10,pady=10)
lblAcceleration.grid(row=4,column=0,padx=10,pady=10)
txtAcc.grid(row=4,column=1,padx=10,pady=10)
btnCalc.grid(row=5,column=0,padx=10,pady=10)
lblSolutionOne.grid(row=5,column=1,padx=10,pady=10)
lblSolutionTwo.grid(row=6,column=1,padx=10,pady=10)

#label, text, and button config, for background color
lblRadius.config(bg="light blue")
lblVelocity.config(bg="light blue")
lblAcceleration.config(bg="light blue")
lblSolutionOne.config(bg="light blue")
lblSolutionTwo.config(bg="light blue")
lblTitle.config(bg="light blue")
lblDirections.config(bg="light blue")

#builds the window
canvas.mainloop()