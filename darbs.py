import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from PIL import Image, ImageTk

logs=Tk()# loga objekts
logs.title("Datora remonts")
logs.geometry("1000x600")
logs.configure(background="#F5EAD4")

#trīs kolunas
foto_frame=tk.Frame(logs, background='#F5EAD4')
foto_frame.grid(row=0, column=0)
foto_image=Image.open("logo.png")
resized_foto=foto_image.resize((170,170))
foto = ImageTk.PhotoImage(resized_foto)
foto_label=ttk.Label(foto_frame,image=foto, background='#F5EAD4')
foto_label.pack(pady=10, padx=10)

ttk.Label(logs, text="Datora remonts", font='Arial 32 bold',background='#F5EAD4').grid(row=0, column=2, pady=10, padx=50)

ttk.Label(logs, text="Kāds dators Jums ir \n(stacionārais vai portatīvais dators)?", font='Arial 12 bold',background='#F5EAD4').grid(row=1, column=0, pady=10, padx=10)
dators = ttk.Combobox(logs, values=["Stacionārais","Portatīvais"])
dators.grid(row=2, column=0, pady=10, padx=10)

def izvele_dators():
    dators_izveletais = dators.get()
    print(dators_izveletais)

datorspoga = tk.Button(logs, text="Izvēlēties", font=("Arial",8,"bold"), bd=3,command=izvele_dators)
datorspoga.grid(row=3, column=0, pady=10, padx=10)

ttk.Label(logs, text="Kāds pakalpojums Jums ir nepieciešams?", font='Arial 12 bold',background='#F5EAD4').grid(row=1, column=2, pady=10, padx=10)




logs.mainloop()