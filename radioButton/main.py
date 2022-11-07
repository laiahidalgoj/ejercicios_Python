
import tkinter
from tkinter import ttk, W

window = tkinter.Tk()

def makeClick():
    print('Click')

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

button = ttk.Button(window, text='Restart')
button.pack(anchor=W)

window.mainloop()