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

        title_label = ctk.CTkLabel(master=self, text = "Pokedex", font=("Arial", 20, "bold"))
        title_label.pack(pady=10, padx=10)

        info_label = ctk.CTkLabel(master=self, text=f"Total Pokemon: {len(df)}")
        info_label.pack()

        scrollable_frame = ctk.CTkScrollableFrame(master=self, width=200, height=200)
        scrollable_frame.pack()


app = App()
app.mainloop()
