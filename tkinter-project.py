import tkinter as tk

#functions
def compute():
    try:
        tanAcc = (radius.get())*(acc.get())
        centrip = (speed**2)/(radius)
    except ValueError:
        
#window config
canvas = tk.Tk()
canvas.geometry("400x400")
canvas.title("something")
canvas.config(bg = "light blue")
#labels
radii = tk.Label(canvas, text="Enter radius:")
velocity = tk.Label(canvas, text="Enter velocity:")
acceleration = tk.Label(canvas, text="Enter acceleration:")
#text
radius = tk.Entry(canvas)
speed = tk.Entry(canvas)
acc = tk.Entry(canvas)

#button
clac = tk.Button(canvas, text="Calculate", command=compute)

#GUI


#run
canvas.mainloop()