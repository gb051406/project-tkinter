import tkinter as tk

#functions
def compute():
    try:
        tanAcc = (float(txtradius.get()))*(float(txtacc.get())) #calculations
        centrip = (float(txtspeed.get())**2)/(float(txtradius.get()))
        lblsolutionOne.config(text="Tangential Acceleration = "+str(tanAcc)) #changes solution text to solution
        lblsolutionTwo.config(text="Centripetal Acceleration = "+str(centrip))
    except ValueError: #allows for no stopage when entering numbers
        lblsolutionOne.config(text="ERROR: enter only numbers")
#window config
canvas = tk.Tk()
canvas.geometry("400x400")
canvas.title("something")
canvas.config(bg = "light blue")
#labels
lblradii = tk.Label(canvas, text="Enter radius:")
lblvelocity = tk.Label(canvas, text="Enter velocity:")
lblacceleration = tk.Label(canvas, text="Enter acceleration:")
lblsolutionOne = tk.Label(canvas, text="")
lblsolutionTwo = tk.Label(canvas, text="")
#text
txtradius = tk.Entry(canvas)
txtspeed = tk.Entry(canvas)
txtacc = tk.Entry(canvas)

#button
btncalc = tk.Button(canvas, text="Calculate", command=compute)

#GUI
lblradii.grid(row=0,column=0,padx=10,pady=10)
txtradius.grid(row=0,column=1,padx=10,pady=10)
lblvelocity.grid(row=1,column=0,padx=10,pady=10)
txtspeed.grid(row=1,column=1,padx=10,pady=10)
lblacceleration.grid(row=2,column=0,padx=10,pady=10)
txtacc.grid(row=2,column=1,padx=10,pady=10)
btncalc.grid(row=3,column=0,padx=10,pady=10)
lblsolutionOne.grid(row=3,column=1,padx=10,pady=10)
lblsolutionTwo.grid(row=4,column=1,padx=10,pady=10)
#run
canvas.mainloop()