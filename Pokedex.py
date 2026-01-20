from tkinter import Frame

import pandas as pd
import matplotlib.pyplot as plt
import customtkinter as ctk

ctk.set_appearance_mode("system")

root = ctk.CTk()

frame = ctk.CTkFrame(master=root, width=200, height=200)

df = pd.read_csv("pokemon_data.csv")

df.info()

print("Amount of pokemon is:", len(df))

df["Name"].value_counts().plot(kind="bar")
plt.title("Pokemon Type")
plt.show()

pokemon = {
    "Name": 'Pikachu',
    "Type": 'Electric',
    "Generation": 'Gen 1',
    "Moveset": 'Electrocute, Zap',
    "Special": 'Evolution'
}

df = pd.DataFrame([pokemon], index=["Type Distribution"])

print(df.loc['Type Distribution'])

df["Name"].value_counts().plot(kind="bar")
plt.title("Pokemon Distribution")
plt.show()


class App():
    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = MyFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


app = App()
app.mainloop()
