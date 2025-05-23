import pandas as pd
import plotly.graph_objects as go
import os

# Skapa mapp för HTML-filer
os.makedirs("visualiseringar", exist_ok=True)

# Läs in Excel-filen och hoppa över inledande rader
file_path = "data/betyg_o_prov_riksnivå.xlsx"
df = pd.read_excel(file_path, sheet_name="Tabell 1A", skiprows=6)


# Testa att visa de första raderna i datan för att hitta rätt struktur


# print(df.columns.tolist())

# Filtrera på relevanta läsår
df = df[df["Unnamed: 0"].astype(str).str.contains("18|19|20|21|22|23")]

#Tydliggör kolumnnamn
df.rename(columns={
    'Unnamed: 0': 'Läsår',
    'Totalt' : 'Andel utan godkänt betyg Totalt',
    'Flickor': 'Andel utan godkänt betyg Flickor',
    'Pojkar' : 'Andel utan godkänt betyg Pojkar'
},inplace= True)

# Diagram 1: Andel utan godkänt betyg
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df["Läsår"],
    y=df["Andel utan godkänt betyg Totalt"],
    mode='lines+markers',
    name='Totalt'
))

fig.add_trace(go.Scatter(
    x=df["Läsår"],
    y=df["Andel utan godkänt betyg Flickor"],
    mode='lines+markers',
    name='Flickor'
))

fig.add_trace(go.Scatter(
    x=df["Läsår"],
    y=df["Andel utan godkänt betyg Pojkar"],
    mode='lines+markers',
    name='Pojkar'
))

fig.update_layout(
    title="Andel elever utan godkänt betyg i minst ett ämne (2018–2023)",
    xaxis_title="Läsår",
    yaxis_title="Procent (%)",
    template="plotly_white"
)

fig.write_html("visualiseringar/uppgift2a_missing_grades.html")
fig.show()

# Diagram 2: Meritvärde
fig2 = go.Figure()

fig2.add_trace(go.Scatter(
    x=df["Läsår"],
    y=df["Meritvärde 16 ämnen Totalt"],
    mode='lines+markers',
    name='Totalt'
))

fig2.add_trace(go.Scatter(
    x=df["Läsår"],
    y=df["Meritvärde 16 ämnen Flickor"],
    mode='lines+markers',
    name='Flickor'
))

fig2.add_trace(go.Scatter(
    x=df["Läsår"],
    y=df["Meritvärde 16 ämnen Pojkar"],
    mode='lines+markers',
    name='Pojkar'
))

fig2.update_layout(
    title="Meritvärde (16 ämnen), 2018–2023",
    xaxis_title="Läsår",
    yaxis_title="Poäng",
    template="plotly_white"
)

fig2.write_html("visualiseringar/uppgift2b_merit_value.html")
fig2.show()
