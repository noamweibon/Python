import tkinter as tk  
from tkinter import messagebox  
import os


#IMPORTANT 
#TO ADD
#STATT
#OPENNINGS
#COLORS 
#BEST ELO

def calculate_and_save():
    try:
        user_name = entry_name.get()
        date = entry_date.get()
        wins = int(entry_wins.get())
        losses = int(entry_losses.get())
        
        total_games = wins + losses
        
        if total_games > 0:
            win_percentage = (wins / total_games) * 100  
        else:
            win_percentage = 0
        
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        file_path = os.path.join(desktop, "results.txt")
        
        with open(file_path, "a") as file:
            file.write(f"Name: {user_name}, Date: {date}, Wins: {wins}, Losses: {losses}, Win Percentage: {win_percentage:.2f}%\n")
        
        messagebox.showinfo("Success", f"Win percentage recorded: {win_percentage:.2f}%\nFile saved at: {file_path}")
        
        entry_name.delete(0, tk.END)
        entry_date.delete(0, tk.END)
        entry_wins.delete(0, tk.END)
        entry_losses.delete(0, tk.END)
        
    except ValueError:
        messagebox.showerror("Error", "Please enter valid values.")

window = tk.Tk()
window.title("Win Percentage Calculator")

label_name = tk.Label(window, text="User Name:")
label_name.pack()
entry_name = tk.Entry(window)
entry_name.pack()

label_date = tk.Label(window, text="Date (DD/MM/YYYY):")
label_date.pack()
entry_date = tk.Entry(window)
entry_date.pack()

label_wins = tk.Label(window, text="Number of Wins:")
label_wins.pack()
entry_wins = tk.Entry(window)
entry_wins.pack()

label_losses = tk.Label(window, text="Number of Losses:")
label_losses.pack()
entry_losses = tk.Entry(window)
entry_losses.pack()

button = tk.Button(window, text="Calculate and Save", command=calculate_and_save)
button.pack()

window.mainloop()
