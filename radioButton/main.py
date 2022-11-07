
import tkinter
from tkinter import ttk, W

def select():
    monitor.config(text='{}'.format(selected.get()))

def reset():
    selected.set(None)
    monitor.config(text='')

window = tkinter.Tk()
selected = tkinter.StringVar()
selected.set(None)


window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

selected = tkinter.StringVar()

radio_button = ttk.Radiobutton(window, text='Python', value='1', variable=selected)
radio_button2 = ttk.Radiobutton(window, text='Java', value='2', variable=selected)
radio_button3 = ttk.Radiobutton(window, text='Go', value='3', variable=selected)
radio_button4 = ttk.Radiobutton(window, text='JavaScript', value='4', variable=selected)
radio_button5 = ttk.Radiobutton(window, text='C++', value='5', variable=selected)

radio_button.pack(anchor=W)
radio_button2.pack(anchor=W)
radio_button3.pack(anchor=W)
radio_button4.pack(anchor=W)
radio_button5.pack(anchor=W)

monitor = tkinter.Label(window)
monitor.pack()
tkinter.Button(window, text='Restart', command=reset).pack()

window.mainloop()