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
        ax = fig.add_subplot(111)
        df["Type 1"].value_counts().plot(kind="bar", ax=ax)
        ax.set_title("Pokemon Type")
        ax.set_xlabel("Pokemon Type")
        ax.set_ylabel("Number of Pokemon")

        canvas = FigureCanvasTkAgg(fig, master=self.my_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

app = App()
app.mainloop()


