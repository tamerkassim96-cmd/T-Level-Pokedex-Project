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
        self.geometry("1400x900")
        self.title("Pokedex")

        # Pokedex title
        pokedex_titlelabel = ctk.CTkLabel(master=self, text="Pokedex", font=("Arial", 24, "bold"))
        pokedex_titlelabel.pack(pady=15)

        # Main layout frame for the GUI
        self.layout_frame = ctk.CTkFrame(master=self)
        self.layout_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Frame for the left side used for generation filters, type filters etc
        self.left_side_frame = ctk.CTkFrame(master=self.layout_frame)
        self.left_side_frame.pack(side="left", fill="y", padx=(0, 10), pady=10)
        self.left_side_frame.pack_propagate(False)
        self.left_side_frame.configure(width=400)

        # Displays the amount of total pokemon
        pokedex_infolabel = ctk.CTkLabel(master=self.left_side_frame,text=f"Total Pokemon: {len(df)}",font=("Arial", 14, "bold"))
        pokedex_infolabel.pack(pady=(10, 15))

        # Search section
        search_label = ctk.CTkLabel(master=self.left_side_frame,text="Search Pokemon",font=("Arial", 13, "bold"))
        search_label.pack(pady=(5, 5))

        pokedex_searchframe = ctk.CTkFrame(master=self.left_side_frame)
        pokedex_searchframe.pack(pady=5, padx=15, fill="x")

        self.entry = ctk.CTkEntry(master=pokedex_searchframe,placeholder_text="Enter Pokemon name...",width=250)
        self.entry.pack(side="left", padx=5, expand=True, fill="x")

        button = ctk.CTkButton(master=pokedex_searchframe,text="Search",command=self.search_pokemon,width=80)
        button.pack(side="left", padx=5)

        # Pokemon info display
        self.pokemon_info = ctk.CTkLabel(master=self.left_side_frame,text="Search for a Pokemon...",font=("Arial", 11),wraplength=350,justify="left")
        self.pokemon_info.pack(pady=15, padx=10)

        # Separator, creates lines in between the filters to make it look more clean
        separator1 = ctk.CTkFrame(master=self.left_side_frame, height=2, fg_color="gray30")
        separator1.pack(fill="x", padx=20, pady=10)

        # Generation filter
        pokedex_generation_filter_label = ctk.CTkLabel(master=self.left_side_frame,text="Filter by Generation",font=("Arial", 13, "bold"))
        pokedex_generation_filter_label.pack(pady=(5, 5))

        self.pokemon_generation_menu = ctk.CTkOptionMenu(master=self.left_side_frame,values=["All", "1", "2", "3", "4", "5", "6"],
        command=self.pokemon_generation_filter,width=200)
        self.pokemon_generation_menu.set("All")
        self.pokemon_generation_menu.pack(pady=5)

        # Type filter
        pokemon_typefilter = ctk.CTkLabel(master=self.left_side_frame,text="Filter by Type",font=("Arial", 13, "bold"))
        pokemon_typefilter.pack(pady=(15, 5))

        self.pokemon_type_menu = ctk.CTkOptionMenu(master=self.left_side_frame,values=["All", "Fire", "Water", "Grass", "Electric", "Ice", "Psychic",
        "Dark", "Dragon", "Fairy", "Fighting", "Normal", "Flying","Poison", "Rock", "Ground", "Bug", "Ghost", "Steel"],command=self.pokemon_typefilter,width=200)
        self.pokemon_type_menu.set("All")
        self.pokemon_type_menu.pack(pady=5)

        # 2nd Separator, creates lines in between the filters to make it look more clean
        separator2 = ctk.CTkFrame(master=self.left_side_frame, height=2, fg_color="gray30")
        separator2.pack(fill="x", padx=20, pady=15)

        # Random pokemon button
        random_pokemon = ctk.CTkButton(master=self.left_side_frame,text="Random Pokemon",command=self.random_pokemon,width=200,height=35,
        font=("Arial", 13, "bold"))
        random_pokemon.pack(pady=10)

        # Right side frame for main graphs and charts to be displayed on the right side of the GUI
        self.right_side_frame = ctk.CTkFrame(master=self.layout_frame)
        self.right_side_frame.pack(side="right", fill="both", expand=True, padx=(10, 0), pady=10)

        # Stats frame (top half)
        stats_label = ctk.CTkLabel(master=self.right_side_frame,text="Pokemon Statistics",font=("Arial", 16, "bold"))
        stats_label.pack(pady=(10, 5))

        self.stats_frame = ctk.CTkFrame(master=self.right_side_frame, height=350)
        self.stats_frame.pack(fill='both', expand=True, padx=15, pady=(5, 15))

        # Initial message before searching pokemon in stats frame
        initial_stats_label = ctk.CTkLabel(master=self.stats_frame,text="Select a Pokemon to view its stats",font=("Arial", 14),text_color="gray50")
        initial_stats_label.pack(expand=True)

        # Type distribution frame (bottom half)
        pokemon_type_chart_label = ctk.CTkLabel(master=self.right_side_frame,text="Overall Type Distribution",font=("Arial", 16, "bold"))
        pokemon_type_chart_label.pack(pady=(10, 5))

        self.type_chart_frame = ctk.CTkFrame(master=self.right_side_frame, height=350)
        self.type_chart_frame.pack(fill="both", expand=True, padx=15, pady=(5, 15))
        self.type_chart_frame.pack_propagate(False)

        self.create_type_distribution_chart()

    def create_type_distribution_chart(self):
        fig = Figure(figsize=(8, 4), facecolor="#2b2b2b")
        ax = fig.add_subplot(111, facecolor="#2b2b2b")

        df["Type 1"].value_counts().plot(kind="bar", ax=ax, color="steelblue")
        ax.set_title("Pokemon Type Distribution", color="white", fontsize=12, weight="bold")
        ax.set_xlabel("Type", color="white")
        ax.set_ylabel("Count", color="white")
        ax.tick_params(colors="white")
        plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha="right")
        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=self.type_chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    # Allows the user to search for a specific pokemon
    def search_pokemon(self):
        for widget in self.stats_frame.winfo_children():
            widget.destroy()

        search_text = self.entry.get().lower()

        if not search_text:
            self.pokemon_info.configure(text="Please enter a Pokemon name") # configure just updates
            return

        get_text = df.loc[df["Name"].str.lower() == search_text]

        if get_text.empty:
            self.pokemon_info.configure(text="Pokemon not found. Try another name.")

            # This creates a "not found" message in the stats frame
            not_found_message_label = ctk.CTkLabel(master=self.stats_frame,text="Pokemon not found",font=("Arial", 14),text_color="gray50")
            not_found_message_label.pack(expand=True)
        else:
            pokemon = get_text.iloc[0]

            pokemon_info = (f"Name: {pokemon['Name']}\n"
                            f"Type: {pokemon['Type 1']}\n"
                            f"HP: {pokemon['HP']} | Attack: {pokemon['Attack']} | Defense: {pokemon['Defense']}\n"
                            f"Generation: {pokemon['Generation']} | Speed: {pokemon['Speed']}")
            self.pokemon_info.configure(text=pokemon_info)

            pokemon_stats = {
                "HP": pokemon['HP'],
                "Attack": pokemon['Attack'],
                "Defense": pokemon['Defense'],
                "Sp. Atk": pokemon['Sp. Atk'],
                "Sp. Def": pokemon['Sp. Def'],
                "Speed": pokemon['Speed'],
            }

            fig = Figure(figsize=(8, 4), facecolor="#2b2b2b")
            ax = fig.add_subplot(111, facecolor="#2b2b2b")
            ax.bar(pokemon_stats.keys(), pokemon_stats.values(), color="orange")
            ax.set_title(f"{pokemon['Name']} Stats", fontsize=14, weight="bold", color="white")
            ax.set_ylabel("Stat Value", color="white")
            ax.set_ylim(0, max(pokemon_stats.values()) + 20)
            ax.tick_params(colors="white")
            fig.tight_layout()

            canvas = FigureCanvasTkAgg(fig, master=self.stats_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill="both", expand=True)

    # Filters pokemon by their generation
    def pokemon_generation_filter(self, generation_choice):
        for widget in self.stats_frame.winfo_children():
            widget.destroy()

        if generation_choice == "All":
            filtered_pokemon_data = df
        else:
            filtered_pokemon_data = df[df["Generation"] == int(generation_choice)]

        self.pokemon_info.configure(
            text=f"Generation {generation_choice}: {len(filtered_pokemon_data)} Pokemon found"
        )

        fig = Figure(figsize=(8, 4), facecolor="#2b2b2b")
        ax = fig.add_subplot(111, facecolor="#2b2b2b")
        filtered_pokemon_data["Type 1"].value_counts().plot(kind="bar", ax=ax, color="green")
        ax.set_title(f"Generation {generation_choice} Type Distribution", color="white", fontsize=12, weight="bold")
        ax.set_xlabel("Type", color="white")
        ax.set_ylabel("Number of Pokemon", color="white")
        ax.tick_params(colors="white")
        plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha="right")
        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=self.stats_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    # Filters pokemon by their type like electric, fire etc.
    def pokemon_typefilter(self, type_choice):
        for widget in self.stats_frame.winfo_children():
            widget.destroy()

        if type_choice == "All":
            filtered_pokemon_data = df
        else:
            filtered_pokemon_data = df[df["Type 1"] == type_choice]

        self.pokemon_info.configure(
            text=f"Type: {type_choice} - {len(filtered_pokemon_data)} Pokemon found"
        )

        fig = Figure(figsize=(8, 4), facecolor="#2b2b2b")
        ax = fig.add_subplot(111, facecolor="#2b2b2b")
        filtered_pokemon_data["Generation"].value_counts().sort_index().plot(kind="bar", ax=ax, color="purple")
        ax.set_title(f"{type_choice} Type - Generation Distribution", color="white", fontsize=12, weight="bold")
        ax.set_xlabel("Generation", color="white")
        ax.set_ylabel("Number of Pokemon", color="white")
        ax.tick_params(colors="white")
        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=self.stats_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    # Displays a random pokemon when the button is clicked
    def random_pokemon(self):
        for widget in self.stats_frame.winfo_children():
            widget.destroy()

        random_pokemon = df.sample(1).iloc[0]

        self.pokemon_info.configure(text=f"Random Pokemon: {random_pokemon['Name']}\n"
        f"Type: {random_pokemon['Type 1']} | Generation: {random_pokemon['Generation']}")

        stats = {
            "HP": random_pokemon['HP'],
            "Attack": random_pokemon['Attack'],
            "Defense": random_pokemon['Defense'],
            "Sp. Atk": random_pokemon['Sp. Atk'],
            "Sp. Def": random_pokemon['Sp. Def'],
            "Speed": random_pokemon['Speed'],
        }

        fig = Figure(figsize=(8, 4), facecolor="#2b2b2b")
        ax = fig.add_subplot(111, facecolor="#2b2b2b")
        ax.bar(stats.keys(), stats.values(), color="red")
        ax.set_title(f"{random_pokemon['Name']} Stats", color="white", fontsize=14, weight="bold")
        ax.set_ylabel("Stat Value", color="white")
        ax.set_ylim(0, max(stats.values()) + 20)
        ax.tick_params(colors="white")
        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=self.stats_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)


app = App()
app.mainloop()
