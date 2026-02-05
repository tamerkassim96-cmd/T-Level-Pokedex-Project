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
        self.geometry("1200x900")
        self.title("Pokedex")

        title_label = ctk.CTkLabel(master=self, text="Pokedex", font=("Arial", 24, "bold"))
        title_label.pack(pady=15)

        info_label = ctk.CTkLabel(master=self, text=f"Total Pokemon: {len(df)}")
        info_label.pack()

        search_frame = ctk.CTkFrame(master=self)
        search_frame.pack(pady=10)

        self.entry = ctk.CTkEntry(master=search_frame, placeholder_text="Search Pokemon", width=300)
        self.entry.pack(side="left", padx=5)

        button = ctk.CTkButton(master=search_frame, text="Search", command=self.search_pokemon)
        button.pack(side="left", padx=5)

        self.pokemon_info = ctk.CTkLabel(master=self, text="Search for a Pokemon...", font=("Arial", 12))
        self.pokemon_info.pack(pady=10)

        self.stats_frame = ctk.CTkFrame(master=self, height=350)
        self.stats_frame.pack(fill="x", padx=20, pady=10)

        pokemon_type_chart_label = ctk.CTkLabel(master=self, text="Overall Type Distribution", font=("Arial", 14, "bold"))
        pokemon_type_chart_label.pack(pady=(20, 5))

        self.my_frame = ctk.CTkFrame(master=self, height=250)
        self.my_frame.pack(fill="x", padx=20, pady=10)
        self.my_frame.pack_propagate(False)

        fig = Figure(figsize=(10, 3))
        ax = fig.add_subplot(111)
        df["Type 1"].value_counts().plot(kind="bar", ax=ax, color='steelblue')
        ax.set_title("Pokemon Type Distribution")
        ax.set_xlabel("Type")
        ax.set_ylabel("Count")
        plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')

        canvas = FigureCanvasTkAgg(fig, master=self.my_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def search_pokemon(self):
        for widget in self.stats_frame.winfo_children():
            widget.destroy()

        search_text = self.entry.get().lower()

        if not search_text:
            self.pokemon_info.configure(text="Please enter a Pokemon name")
            return

        get_text = df.loc[df["Name"].str.lower() == search_text]

        if get_text.empty:
            self.pokemon_info.configure(text="Pokemon not found.")
        else:
            pokemon = get_text.iloc[0]

            info_text = (f"Name: {pokemon['Name']} |"
                         f"Type: {pokemon['Type 1']} |"
                         f"HP: {pokemon['HP']} |"
                         f"Generation: {pokemon['Generation']} |"
                         f"Speed: {pokemon['Speed']}")
            self.pokemon_info.configure(text=info_text)

            pokemon_stats = {
                "HP": pokemon['HP'],
                "Attack": pokemon['Attack'],
                "Defense": pokemon['Defense'],
                "Sp. Atk": pokemon['Sp. Atk'],
                "Sp. Def": pokemon['Sp. Def'],
                "Speed": pokemon['Speed'],
            }

            fig = Figure(figsize=(10, 4))
            ax = fig.add_subplot(111)
            ax.bar(pokemon_stats.keys(), pokemon_stats.values(), color='coral')
            ax.set_title(f"{pokemon['Name']} Stats", fontsize=14, fontweight='bold')
            ax.set_ylabel("Stat Value")
            ax.set_ylim(0, max(pokemon_stats.values()) + 20)

            canvas = FigureCanvasTkAgg(fig, master=self.stats_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill="both", expand=True)


app = App()
app.mainloop()
