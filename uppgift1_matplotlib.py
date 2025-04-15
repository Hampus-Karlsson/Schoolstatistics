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