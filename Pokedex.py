import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("pokemon_data.csv")

df.info()

print("Amount of pokemon is:", len(df))

df["Name"].value_counts().plot(kind="bar")
plt.title("Pokemon Type")
plt.show()

# pokemon = {
# "Name": 'Pikachu',
# "Type": 'Electric',
# "Generation": 'Gen 1',
# "Moveset": 'Electrocute, Zap',
# "Special":'Evolution'
# }
#
# df = pd.DataFrame([pokemon], index=["Type Distribution"])
#
# print(df.loc['Type Distribution'])

# df["Name"].value_counts().plot(kind="bar")
# plt.title("Pokemon Distribution")
# plt.show()
