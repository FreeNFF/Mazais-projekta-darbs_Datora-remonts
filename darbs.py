#nepieciešamās bibliotēkas
import tkinter as tk
from tkinter import ttk
import csv
from PIL import Image, ImageTk

#loga izveide
logs = tk.Tk()
logs.title("Datora remonts")
logs.geometry("720x650")
logs.configure(background="#F5EAD4")

#attēla pievienošana
foto_frame = tk.Frame(logs, background='#F5EAD4')
foto_frame.grid(row=0, column=0)
foto_image = Image.open("logo.png")
resized_foto = foto_image.resize((170, 170))
foto = ImageTk.PhotoImage(resized_foto)
foto_label = ttk.Label(foto_frame, image=foto, background='#F5EAD4')
foto_label.pack(pady=10, padx=10)

#virsraksta pievienošana
ttk.Label(logs, text="Datora remonts", font='Arial 32 bold', background='#F5EAD4').grid(row=0, column=2, pady=10, padx=50)

#mainīgo ieviešana
kop_summ = 0.0
kop_summ_pvn = 0.0
kop_stundas = 0.0
dators_izveletais = ""

#teksta ievietošana un izvēles ievietošana
ttk.Label(logs, text="Kāds dators Jums ir \n(stacionārais vai portatīvais)?", font='Arial 12 bold', background='#F5EAD4').grid(row=1, column=0, pady=10, padx=10)
dators = ttk.Combobox(logs, values=["Stacionārais", "Portatīvais"], state='readonly')
dators.grid(row=2, column=0, pady=10, padx=10)

#teksta ievietošana un izvēles ievietošana
ttk.Label(logs, text="Kāds pakalpojums Jums ir nepieciešams?", font='Arial 12 bold', background='#F5EAD4').grid(row=1, column=2, pady=10, padx=10)
pakalpojums = ttk.Combobox(logs, state='readonly', width=50)
pakalpojums.grid(row=2, column=2, pady=10, padx=10)

#izvēlētā datoru pakalpojumu veidu izvēle
def izvele_dators():
    global dators_izveletais
    dators_izveletais = dators.get()
    pakalpojumi = []
    #atver csv failu, kurā rakstīti datora veidi, paklpojumi un cenas, ievieto to Comboboxā
    with open("pakalpojumi.csv", mode='r', encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row["Veids"] == dators_izveletais:
                pakalpojumi.append(row["Pakalpojums"])
    
    pakalpojums.set('')#kad tiek izvēlēts paklpojums, tad paklpojuma logs iestadīts sākotnējā stadijā
    pakalpojums['values'] = pakalpojumi#izvēlētais pakolpojums tiek ievietots sarakstā

#pievieno pogu
datorspoga = tk.Button(logs, text="Izvēlēties", font=("Arial", 8, "bold"), bd=3, command=izvele_dators)
datorspoga.grid(row=3, column=0, pady=10, padx=10)

#datora veida, pakalpojumu un cenas izvades logs
izvade = tk.Listbox(logs, width=110, bg="#505050", fg="white", bd=5)
izvade.grid(row=5, columnspan=3, pady=10, padx=25)

#funkcija ar kuru var pievienot vairākus pakalpojumus, izrēķina kopīgo cenu, viss tiek reģistrēts izvades logā
def pievienot_pakalpojumu():
    global kop_summ, dators_izveletais,kop_stundas,kop_summ_pvn

    izveletais_pak = pakalpojums.get()
    if not dators_izveletais or not izveletais_pak:#ja nav ne izvēlēts dators, ne izvēlēts pakalpojums, tālāk neko nedarīt
        return
#atver csv failu ar visiem datiem par pakalpojumiem
    with open("pakalpojumi.csv", mode='r', encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)
        #funkcija, lai izvadītu kaut ko izvades logā, tad pārbauda vai visi izvēlētie dati sakrīt ar csv failu, ja sakrīt, tad tiek izvadīts datora veids, pakalpojums, cena un ilgums
        for row in csv_reader:
            if row["Veids"] == dators_izveletais and row["Pakalpojums"] == izveletais_pak:
                cena = row["Cena"]
                stundas=row["Laiks"]
                try:
                    cena_float = float(cena)
                    pvncena = float(cena_float*1.21)
                    stundas_float = float(stundas)
                    kop_summ += cena_float
                    kop_summ_pvn += pvncena
                    kop_stundas += stundas_float
                    izvade.insert(tk.END, f"Datora veids: {dators_izveletais}")
                    izvade.insert(tk.END, f"Pakalpojums: {izveletais_pak}")
                    izvade.insert(tk.END, f"Cena bez PVN: {cena} EUR")
                    izvade.insert(tk.END, f"Cena ar PVN: {pvncena} EUR")
                    izvade.insert(tk.END, f"Ilgums: {stundas} h")
                    izvade.insert(tk.END, "-"*80)
                    izvade.insert(tk.END, f"Kopējā summa bez PVN: {kop_summ:.2f} EUR")
                    izvade.insert(tk.END, f"Kopējā summa ar PVN: {kop_summ_pvn:.2f} EUR")
                    izvade.insert(tk.END, f"Kopējais ilgums: {kop_stundas:.2f} h")
                    izvade.insert(tk.END, "-"*80)
                except:
                    pass
                break

    pakalpojums.set('')#kad tiek izvēlēts paklpojums, tad paklpojuma logs iestadīts sākotnējā stadijā

#pievieno pogu
pakalpojumspoga = tk.Button(logs, text="Pievienot pakalpojumu", font=("Arial", 8, "bold"), bd=3, command=pievienot_pakalpojumu)
pakalpojumspoga.grid(row=3, column=2, pady=10)


# izdzēš visu, kas ir izvades logā
def delete():
    global kop_summ
    izvade.delete(0, tk.END)
    kop_summ = 0.0

#pogas pievienošana
izdzest = tk.Button(logs, text="Izdzēst visu", font=("Arial", 8, "bold"), bd=3, command=delete)
izdzest.grid(row=6, columnspan=3, pady=10)

#saglabā visu teksta failā, kas ir izvades logā
def saglabat_uz_failu():
    with open("Pieteikumi.txt", mode="w", encoding="utf-8") as file:
        for i in range(izvade.size()):
            rindina = izvade.get(i)
            file.write(rindina + "\n")

#poga pievienošana
saglabat_poga = tk.Button(logs, text="Saņemt paklpojumu", font=("Arial", 8, "bold"), bd=3, command=saglabat_uz_failu)
saglabat_poga.grid(row=7, columnspan=3, pady=10)

logs.mainloop()