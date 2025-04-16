import pandas as pd
import plotly.graph_objects as go
import os

#Create HTML folder
os.makedirs("visualiseringar", exist_ok=True)

# Find and read file
file_path = "data/betyg_o_prov_riksnivå.xlsx"
df = pd.read_excel(file_path, sheet_name="Betyg och prov")