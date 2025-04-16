import pandas as pd
import plotly.graph_objects as go
import os

#Create HTML folder
os.makedirs("visualiseringar", exist_ok=True)

# Find and read file
file_path = "data/betyg_o_prov_riksnivå.xlsx"
df = pd.read_excel(file_path, sheet_name="Betyg och prov")

# Filter years (2018–2023)
df = df[df["Läsår"].astype(str).str.contains("18|19|20|21|22|23")]

# Plotting missing grades
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df["Läsår"],
    y=df["Andel utan godkänt betyg Totalt"],
    mode='lines+markers',
    name='Totla'
))

fig.add_trace(go.Scatter(
    x=df["Läsår"],
    y=df["Andel utan godkänt betyg Flickor"],
    mode='lines+markers',
    name='Girls'
))

fig.add_trace(go.Scatter(
    x=df["Läsår"],
    y=df["Andel utan godkänt betyg Pojkar"],
    mode='lines+markers',
    name='Boys'
))

fig.update_layout(
    title="Percentage of Students Without Passing Grades (One or More Subjects), 2018–2023",
    xaxis_title="School Year",
    yaxis_title="Percentage (%)",
    template="plotly_white"
)

# Save HTML
fig.write_html("visualisations/uppgift2a_missing_grades.html")
fig.show()