import tkinter as tk
from tkinter import *
from tkinter import ttk
import csv
from tkinter.font import BOLD
from PIL import Image, ImageTk

logs=Tk()# loga objekts
logs.title("Datora remonts")
logs.geometry("720x650")
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
dators = ttk.Combobox(logs, values=["Stacionārais","Portatīvais"],state='readonly')
dators.grid(row=2, column=0, pady=10, padx=10)
    
dators_izveletais = ""
izveletais_pak = ""

def izvele_dators():
    global dators_izveletais
    dators_izveletais = dators.get()
       
    pakalpojums.set('')
    
    if dators_izveletais == 'Stacionārais':
        csv_file = 'stacionarais.csv'
    elif dators_izveletais == 'Portatīvais':
        csv_file = 'portativais.csv'
    else:
        return 

   
    with open(csv_file, mode='r', newline='', encoding="utf-8") as file:
        csv_reader = csv.reader(file, delimiter=',')
        pakalpojumi = [row[0] for row in csv_reader]


    pakalpojums['values'] = pakalpojumi

datorspoga = tk.Button(logs, text="Izvēlēties", font=("Arial",8,"bold"), bd=3,command=izvele_dators)
datorspoga.grid(row=3, column=0, pady=10, padx=10)

ttk.Label(logs, text="Kāds pakalpojums Jums ir nepieciešams?", font='Arial 12 bold',background='#F5EAD4').grid(row=1, column=2, pady=10, padx=10)

pakalpojums = ttk.Combobox(logs, state='readonly',width=50)
pakalpojums.grid(row=2, column=2, pady=10, padx=10)

izvade= tk.Listbox(logs, width=110, bg="#505050", fg="white", bd=5)
izvade.grid(row=5,columnspan=3, pady=10)

    
def pakalpojuma_izvele():
    global izveletais_pak
    izveletais_pak= pakalpojums.get()


pakalpojumssagl = tk.Button(logs, text="Izvēlēties", font=("Arial",8,"bold"), bd=3, command=pakalpojuma_izvele)
pakalpojumssagl.grid(row=3, column=2, pady=10, padx=10)
    


def izvades_logs():
    global izveletais_pak
    izvele_dators()
    izvade.insert(tk.END, f"Datora veids: {dators_izveletais}")
    izvade.insert(tk.END, f"Pakalpojums: {izveletais_pak}")
    izvade.insert(tk.END, f"Cena:  EUR")

pakalpojumspoga = tk.Button(logs, text="Rādīt cenu", font=("Arial",8,"bold"), bd=3, command=izvades_logs)
pakalpojumspoga.grid(row=4, columnspan=3, pady=10, padx=0)

def delete():
   izvade.delete(0,END)

izdzest= tk.Button(logs, text="Izdzēst", font=("Arial",8,"bold"), bd=3, command=delete)
izdzest.grid(row=6, columnspan=3, pady=10, padx=0)

logs.mainloop()