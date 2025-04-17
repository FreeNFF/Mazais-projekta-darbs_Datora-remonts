import tkinter as tk
from tkinter import ttk
import csv
from PIL import Image, ImageTk


logs = tk.Tk()
logs.title("Datora remonts")
logs.geometry("720x650")
logs.configure(background="#F5EAD4")


foto_frame = tk.Frame(logs, background='#F5EAD4')
foto_frame.grid(row=0, column=0)
foto_image = Image.open("logo.png")
resized_foto = foto_image.resize((170, 170))
foto = ImageTk.PhotoImage(resized_foto)
foto_label = ttk.Label(foto_frame, image=foto, background='#F5EAD4')
foto_label.pack(pady=10, padx=10)


ttk.Label(logs, text="Datora remonts", font='Arial 32 bold', background='#F5EAD4').grid(row=0, column=2, pady=10, padx=50)


kop_summ = 0.0
dators_izveletais = ""


ttk.Label(logs, text="Kāds dators Jums ir \n(stacionārais vai portatīvais)?", font='Arial 12 bold', background='#F5EAD4').grid(row=1, column=0, pady=10, padx=10)
dators = ttk.Combobox(logs, values=["Stacionārais", "Portatīvais"], state='readonly')
dators.grid(row=2, column=0, pady=10, padx=10)


ttk.Label(logs, text="Kāds pakalpojums Jums ir nepieciešams?", font='Arial 12 bold', background='#F5EAD4').grid(row=1, column=2, pady=10, padx=10)
pakalpojums = ttk.Combobox(logs, state='readonly', width=50)
pakalpojums.grid(row=2, column=2, pady=10, padx=10)


def izvele_dators():
    global dators_izveletais
    dators_izveletais = dators.get()
    pakalpojumi = []

    with open("pakalpojumi.csv", mode='r', encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row["Veids"] == dators_izveletais:
                pakalpojumi.append(row["Pakalpojums"])

    pakalpojums.set('')
    pakalpojums['values'] = pakalpojumi


datorspoga = tk.Button(logs, text="Izvēlēties", font=("Arial", 8, "bold"), bd=3, command=izvele_dators)
datorspoga.grid(row=3, column=0, pady=10, padx=10)


izvade = tk.Listbox(logs, width=110, bg="#505050", fg="white", bd=5)
izvade.grid(row=5, columnspan=3, pady=10, padx=25)


def pievienot_pakalpojumu():
    global kop_summ, dators_izveletais

    izveletais_pak = pakalpojums.get()
    if not dators_izveletais or not izveletais_pak:
        return

    with open("pakalpojumi.csv", mode='r', encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row["Veids"] == dators_izveletais and row["Pakalpojums"] == izveletais_pak:
                cena = row["Cena"]
                try:
                    cena_float = float(cena)
                    kop_summ += cena_float
                    izvade.insert(tk.END, f"Datora veids: {dators_izveletais}")
                    izvade.insert(tk.END, f"Pakalpojums: {izveletais_pak}")
                    izvade.insert(tk.END, f"Cena: {cena} EUR")
                    izvade.insert(tk.END, f"Kopējā summa: {kop_summ:.2f} EUR")
                    izvade.insert(tk.END, "-"*80)
                except:
                    pass
                break

    pakalpojums.set('')


pakalpojumspoga = tk.Button(logs, text="Pievienot pakalpojumu", font=("Arial", 8, "bold"), bd=3, command=pievienot_pakalpojumu)
pakalpojumspoga.grid(row=3, column=2, pady=10)



def delete():
    global kop_summ
    izvade.delete(0, tk.END)
    kop_summ = 0.0


izdzest = tk.Button(logs, text="Izdzēst visu", font=("Arial", 8, "bold"), bd=3, command=delete)
izdzest.grid(row=6, columnspan=3, pady=10)

def saglabat_uz_failu():
    with open("rezultati.txt", mode="w", encoding="utf-8") as file:
        for i in range(izvade.size()):
            rindina = izvade.get(i)
            file.write(rindina + "\n")

saglabat_poga = tk.Button(logs, text="Saņemt paklpojumu", font=("Arial", 8, "bold"), bd=3, command=saglabat_uz_failu)
saglabat_poga.grid(row=7, columnspan=3, pady=10)

logs.mainloop()