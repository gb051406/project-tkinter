import tkinter as tk

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
canvas.geometry("400x400")
canvas.title("something")
canvas.config(bg = "light blue")
#labels
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

#GUI
lblRadius.grid(row=0,column=0,padx=10,pady=10)
txtRadius.grid(row=0,column=1,padx=10,pady=10)
lblVelocity.grid(row=1,column=0,padx=10,pady=10)
txtSpeed.grid(row=1,column=1,padx=10,pady=10)
lblAcceleration.grid(row=2,column=0,padx=10,pady=10)
txtAcc.grid(row=2,column=1,padx=10,pady=10)
btnCalc.grid(row=3,column=0,padx=10,pady=10)
lblSolutionOne.grid(row=3,column=1,padx=10,pady=10)
lblSolutionTwo.grid(row=4,column=1,padx=10,pady=10)
#label, text, and button config, for background color
lblRadius.config(bg="light blue")
lblVelocity.config(bg="light blue")
lblAcceleration.config(bg="light blue")
lblSolutionOne.config(bg="light blue")
lblSolutionTwo.config(bg="light blue")
#builds the window
canvas.mainloop()