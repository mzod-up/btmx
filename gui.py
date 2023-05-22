import tkinter as tk
import tkinter.font as font
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
import time, os
from tabreader import process_tab

def ImportTab(event=None):
    filename = askopenfilename(filetypes=(("Text Files", "*.txt"),))
    if(filename):
        info_label.config(text=process_tab(filename))
    else:
        info_label.config(text = "Import cancelled.")
        print("Import cancelled.")
    window.after(4000,lambda:info_label.config(text=''))

window = tk.Tk()
window.resizable(False, False)
window.geometry("600x500")
window.title("BTMX: Bass Tabs to MusicXML Converter")
window['background']='#121315'

frame = tk.Frame(window, width=200, height=200)
frame.pack()
frame.place(relx=0.5, rely=0.5, anchor='w')
img = ImageTk.PhotoImage(Image.open("resources/betamax.jpg"))
label = tk.Label(frame, image=img, borderwidth=0, highlightthickness=0)
label.pack()

import_buttonfont = font.Font(family='Mono', size=10, weight='bold')
info_labelfont = font.Font(family='Mono', size=8)
import_button = tk.Button(window,
                            text="Import Bass Tab",
                            relief='groove',
                            fg='white',
                            font=import_buttonfont,
                            bg='#1F1F1D',
                            command=ImportTab)
import_button.pack()
import_button.place(relx=0.25, rely=0.5, anchor='center')

text_frame = tk.Frame(window, width=100, height=100, bg='#121315')
text_frame.pack()
text_frame.place(relx=0.25, rely=0.60, anchor='center')
info_label = tk.Label(text_frame, text='', font=info_labelfont, wraplength=200, fg='white', bg='#121315')
info_label.pack()


window.mainloop()
