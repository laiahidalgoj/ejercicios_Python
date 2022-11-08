import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=6)

language = ttk.Label(window, text='Select the languages: ')
language.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

languages = ['Java', 'Python', 'C++', 'JavaScript', 'Go']
languages_list = tkinter.StringVar(value=languages)

listbox = tkinter.Listbox(window, height=10, listvariable=languages_list)
listbox.grid(column=0, row=1, sticky=tkinter.W, padx=10, pady=5)

window.mainloop()