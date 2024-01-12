import tkinter as tk

#functions
def compute():

#window config
canvas = tk.Tk()
canvas.geometry("400x400")
canvas.title("something")
canvas.config(bg = "light blue")
#labels
radii = tk.Label(canvas, text="Enter radius:")
velocity = tk.Label(canvas, text="Enter velocity:")
#text
radius = tk.Entry(canvas)
speed = tk.Entry(canvas)
acc = tk.Entry(canvas)

#button
clac = tk.Button(canvas, text="Calculate", command=compute)

#GUI


#run
canvas.mainloop()