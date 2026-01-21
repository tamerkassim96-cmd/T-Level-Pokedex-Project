from tkinter import Frame

import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

ctk.set_appearance_mode("system")

df = pd.read_csv("pokemon_data.csv")
print("Amount of pokemon is:", len(df))


df["Type 1"].value_counts().plot(kind="bar")
plt.title("Pokemon Type")
plt.xlabel("Pokemon Type")
plt.ylabel("Number of Pokemon")
plt.show()

print(df.columns)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Pokedex")
        self.my_frame = ctk.CTkFrame(master=self)
        self.my_frame.pack(fill="both", expand=True, padx=20, pady=20)

        fig = Figure(figsize=(5, 5))
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget()
        canvas.draw()

app = App()
app.mainloop()


