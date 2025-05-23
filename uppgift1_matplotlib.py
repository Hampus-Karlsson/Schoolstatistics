import pandas as pd
import matplotlib.pyplot as plt
import os

# Skapa mapp om den inte finns
os.makedirs("visualiseringar", exist_ok=True)

# Läs in Excelfilen och blad
file = "data/riket2023_åk9_np.xlsx"
sheet_names = ["Engelska", "Matematik", "Svenska", "Svenska som andraspråk"]

# Läs in data till en lista med DataFrames
dataframes = [pd.read_excel(file, sheet_name=sheet) for sheet in sheet_names]

# Ämnesrubriker
subjects = ["Engelska", "Matematik", "Svenska", "Svenska som andraspråk"]

# Sätt kolumnnamn
for df in dataframes:
    df.columns = [
        "Region",
        "Operator",
        "Total (A-F)",
        "Girls (A-F)",
        "Boys (A-F)",
        "Total (A-E)",
        "Girls (A-E)",
        "Boys (A-E)",
        "Total (points)",
        "Girls (points)",
        "Boys (points)",
    ]

# Skapa subplots
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
axs = axs.ravel()

# Gå igenom varje ämne och rita stapeldiagram
for i, df in enumerate(dataframes):
    # Rensa bort rader med saknade eller ogiltiga värden
    df_clean = df.dropna(subset=["Operator", "Total (points)"].copy())

    # Filtrera bort icke-strängar (ibland är float med som 'Operator')
    df_clean["Operator"] = df_clean["Operator"].astype(str)

    # Ta bort rader som innehåller "nan" eller är rubriker
    df_clean = df_clean[~df_clean["Operator"].str.contains("nan", case=False)]
    df_clean = df_clean[~df_clean["Operator"].str.contains("Typ av huvudman", case=False)]

    df_clean["Total (points)"] = pd.to_numeric(df_clean["Total (points)"], errors="coerce")

    df_clean = df_clean.dropna(subset=["Total (points)"])
    operators = df_clean["Operator"]
    points = df_clean["Total (points)"]


    print(f"Ämne: {subjects[i]}")
    print("Operatorer:", operators.tolist())
    print("Poäng:", points.tolist())
    print("Antal operatorer:", len(operators), "Antal poäng:", len(points))

    axs[i].bar(operators, points, color='skyblue')
    axs[i].set_title(f"Total points per Operator – {subjects[i]}")
    axs[i].set_ylabel("Points")
    axs[i].set_xlabel("Operator")
    axs[i].tick_params(axis='x', rotation=15)
    axs[i].set_ylim(0, max(points) + 2)

# Snygg layout
plt.tight_layout()
plt.savefig("visualiseringar/uppgift1_total_points_by_subject.png")
plt.show()



