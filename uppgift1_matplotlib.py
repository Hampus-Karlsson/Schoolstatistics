import pandas as pd
import matplotlib.pyplot as plt
import os

# Create file if not already exist
os.makedirs("visualiseringar", exist_ok=True)

# Read from arcs
file = "data/riket2023_åk9_np.xlsx"
arc_name = ["english", "math", "swedish", "swedish as secondlanguage"]

# Store all dataframes in list
dataframes = [pd.read_excel(file, sheet_name=sheet) for sheet in arc_name]

# Subjects (Headings)
subjects = ["English", "Math", "SWedish", "Swedish as secondlanguage"]

# Rename sheets to match all
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

# Create subplot
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
axs = axs.ravel()

# Cicle through subjects
for i, df in enumerate(dataframes): 
    # Filter only by prinipal
    principal = df["Principal"]
    points = df["Total (points)"]

    axs[i].bar(principal, points, color='skyblue')
    axs[i].set_title(f"Total points for principal – {subjects[i]}")
    axs[i].set_ylabel("Points")
    axs[i].set_xlabel("principal")
    axs[i].set_ylim(0, max(points) + 2)
    axs[i].tick_params(axis='x', rotation=15)

plt.tight_layout()
plt.savefig("visualiseringar/uppgift1_total_points_by_subject.png")
plt.show()