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

        pokedex_infolabel = ctk.CTkLabel(master=self, text=f"Total Pokemon: {len(df)}")
        pokedex_infolabel.pack()

        pokedex_titlelabel = ctk.CTkLabel(master=self, text="Pokedex", font=("Arial", 24, "bold"))
        pokedex_titlelabel.pack(pady=15)

        pokedex_searchframe = ctk.CTkFrame(master=self)
        pokedex_searchframe.pack(pady=10)

        self.entry = ctk.CTkEntry(master=pokedex_searchframe, placeholder_text="Search Pokemon", width=300)
        self.entry.pack(side="left", padx=5)

        button = ctk.CTkButton(master=pokedex_searchframe, text="Search", command=self.search_pokemon)
        button.pack(side="left", padx=5)

        self.pokemon_info = ctk.CTkLabel(master=self, text="Search for a Pokemon...", font=("Arial", 12))
        self.pokemon_info.pack(pady=10)

        self.pokemon_generation_menu = ctk.CTkOptionMenu(master=self, values=["All", "1", "2", "3", "4", "5", "6"],
        command=self.pokemon_generation_filter
        )
        self.pokemon_generation_menu.set("All")
        self.pokemon_generation_menu.pack(pady=5)

        pokedex_filterlabel = ctk.CTkLabel(master=self, text=f"Filter Pokemon by Generation:", font= ("Arial", 12, "bold"))
        pokedex_filterlabel.pack(pady=5)

        self.stats_frame = ctk.CTkFrame(master=self, width=300, height=300)
        self.stats_frame.pack(fill='x', padx=20, pady=10)

        pokemon_type_chart_label = ctk.CTkLabel(master=self, text="Overall Type Distribution", font=("Arial", 14, "bold"))
        pokemon_type_chart_label.pack(pady=(20, 5))

        self.my_frame = ctk.CTkFrame(master=self, height=350, width=700)
        self.my_frame.pack(fill='x',padx=20, pady=10)
        self.my_frame.pack_propagate(False)

        fig = Figure(figsize=(7, 4))
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
        # basically removes the old chart from the previous search
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

            pokemon_info = (f"Name: {pokemon['Name']} |"
                        f"Type: {pokemon['Type 1']} |"
                        f"HP: {pokemon['HP']} |"
                        f"Generation: {pokemon['Generation']} |"
                        f"Speed: {pokemon['Speed']}")
            self.pokemon_info.configure(text=pokemon_info)

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
            ax.bar(pokemon_stats.keys(), pokemon_stats.values(), color='orange')
            ax.set_title(f"{pokemon['Name']} Stats", fontsize=14, weight='bold')
            ax.set_ylabel("Stat Value")
            ax.set_ylim(0, max(pokemon_stats.values()) + 20)

            canvas = FigureCanvasTkAgg(fig, master=self.stats_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill="both", expand=True)


    def pokemon_generation_filter(self, generation_choice):

        for widget in self.stats_frame.winfo_children():
            widget.destroy()

        if generation_choice == "All":
            filtered_pokemon_data = df
        else:
            filtered_pokemon_data = df[df["Generation"] == int(generation_choice)]

        self.pokemon_info.configure(text=f"Pokemon Generation {generation_choice}: {len(filtered_pokemon_data)} Pokemon found")

        fig = Figure(figsize=(10, 4))
        ax = fig.add_subplot(111)
        filtered_pokemon_data["Type 1"].value_counts().plot(kind="bar", ax=ax, color="green")
        ax.set_title(f"Generation {generation_choice} Type Distribution")
        ax.set_ylabel("Number of Pokemon")

        canvas = FigureCanvasTkAgg(fig, master=self.stats_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

app = App()
app.mainloop()



