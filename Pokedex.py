import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("pokemon_data.csv")

print(df.info("Sylveon"))

print("Amount of pokemon is:", len(df))

# df["Type 1"].value_counts().plot(kind="bar")
# plt.title("Pokemon Type")
# plt.show()
