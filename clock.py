import tkinter as tk
from time import strftime
def time():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)
root = tk.Tk()
root.title("Digital Clock")
label = tk.Label(root, font=('DS-DIGITAL', 47), background='light green', foreground='#593e2c',padx=20,pady=20)
label.pack(anchor='center')
time()
root.mainloop()