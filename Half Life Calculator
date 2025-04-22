import tkinter as tk  
from tkinter import messagebox

def remaining():
    try:  
        half_life = float(entry_half_life.get())
        last = float(entry_last.get())
        timepass = last 
        pass_half_time = last / half_life 
        remaining = max(0, 100 * (0.5 ** pass_half_time))
        
        
        messagebox.showinfo("Remaining", f"Remaining : {remaining:.2f}%")
    except ValueError:
        messagebox.showerror("Error")

  
fenetre = tk.Tk()
fenetre.title("Half_life_calcul")

# Créer les champs de saisie  
label_half_life = tk.Label(fenetre, text="Half-life (heures) :")
label_half_life.pack()

entry_half_life = tk.Entry(fenetre)
entry_half_life.pack()

label_last = tk.Label(fenetre, text="Last :")
label_last.pack()

entry_last = tk.Entry(fenetre)
entry_last.pack()


button = tk.Button(fenetre, text="Calculer", command=calculer_pourcentage)
button.pack()

# Lancer la boucle principale  
fenetre.mainloop()
