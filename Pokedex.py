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
        self.geometry("1000x910")
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

        self.pokemon_info = ctk.CTkLabel(master=scrollable_frame, text="Search for a Pokemon...")
        self.pokemon_info.pack()

        self.entry = ctk.CTkEntry(master=self, placeholder_text="Search Pokemon")
        self.entry.pack(padx=10, pady=10)

        button = ctk.CTkButton(master=self, text="Search", command=self.search_pokemon)
        button.pack()

        check_box = ctk.CTkCheckBox(master=self, text="Type")
        check_box.pack(pady=10, padx=10)

    def search_pokemon(self):
        search_text = self.entry.get()
        print(f"Searching for {search_text}...")

        get_text = df.loc[df["Name"] == search_text]
        print(get_text)

        if get_text.empty:
            self.pokemon_info.configure("Pokemon not found.")

        else:
            pokemon = get_text.iloc[0]
            info_text = f"Name: {pokemon["Name"]}\nType: {pokemon['Type 1']}\nHP: {pokemon['HP']}\nGeneration: {pokemon['Generation']}\nSpeed: {pokemon['Speed']}\nSp. Atk: {pokemon['Sp. Atk']}"
            self.pokemon_info.configure(text=info_text)




app = App()
app.mainloop()
